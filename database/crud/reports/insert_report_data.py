from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from database.models.reports.reportModel import AttackData
from database.schemas.report_schemas import AttackDataSchemas

def insert_attack_data(db: Session, data: AttackDataSchemas):
    attack_data_reports = AttackData(id=data.id, sourceIp=data.sourceIp,destinationIp=data.destinationIp,rulename=data.rulename,indicators=data.indicators)
    db.add(attack_data_reports)
    db.commit()
    db.refresh(attack_data_reports)
    return attack_data_reports

# def insert_user(db: Session, username: str, email: str, hashed_password: str):
#     db_user = AttackData(username=username, email=email, hashed_password=hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
