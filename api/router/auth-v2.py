# main.py
from fastapi import APIRouter
from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel

router = APIRouter()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key="!secret",
    session_cookie="session",
)

class LoginForm(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(form: LoginForm, response: Response):
    if form.username == "user" and form.password == "password":
        response.set_cookie(key="session", value="valid-session", httponly=True)
        return JSONResponse(content={"message": "Logged in"})
    return JSONResponse(content={"message": "Invalid credentials"}, status_code=401)

@router.get("/check-session")
async def check_session(request: Request):
    session = request.cookies.get("session")
    if session == "valid-session":
        return JSONResponse(content={"message": "Session valid"})
    return JSONResponse(content={"message": "Session invalid"}, status_code=401)

@router.get("/logout")
async def logout(response: Response):
    response.delete_cookie(key="session")
    return RedirectResponse(url="/login")
