from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
import utils.selenium.get_session as get_session
from pydantic import BaseModel

router = APIRouter()

# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzb2MudXNlcjJAcGVsaW5kby5jby5pZCIsImV4cCI6MTcxNzkzOTQyMH0.xoPyhtYuLq8gxKtWmdyaOuwhov5a8VmomnrwtyfwIdc",
#   "token_type": "bearer"
# }

SECRET_KEY = "!secret"  # Replace with a secure key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str
    tm_token: str

class User(BaseModel):
    username: str

class LoginForm(BaseModel):
    username: str
    password: str

# Function to generate JWT token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to decode JWT token
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return User(username=username)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    
@router.post("/login/")
async def authLogin(login: LoginForm):
    return {"username": login.username, "password": login.password, "token":get_session.login(username=login.username,password=login.password)}


# Login route to generate JWT token
@router.post("/token", response_model=Token)
async def login(form: LoginForm):
    if form.username == "soc.user2@pelindo.co.id" and form.password == "P#lindo@2023":
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": form.username}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer", "tm_token":get_session.login(username=form.username,password=form.password)}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Protected route that requires JWT token in headers
@router.get("/check-session")
async def check_session(token: str = Depends(oauth2_scheme)):
    user = decode_access_token(token)
    return {"message": "Session valid", "username": user.username}

# Logout route to delete JWT token
@router.get("/logout")
async def logout():
    return {"message": "Logged out"}
