from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import openai
import os
from dotenv import load_dotenv

from database import SessionLocal, engine
import models, schemas, utils, logger

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.middleware("http")
async def log_requests(request, call_next):
    logger.log_request(request.method, request.url.path)
    return await call_next(request)

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        records = utils.validate_csv(file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    for record in records:
        db_record = models.Record(**record.dict())
        db.add(db_record)
    db.commit()
    return {"message": f"{len(records)} records added"}

@app.get("/records", response_model=List[schemas.RecordOut])
def get_records(db: Session = Depends(get_db)):
    return db.query(models.Record).all()

@app.get("/records/{record_id}", response_model=schemas.RecordOut)
def get_record(record_id: int, db: Session = Depends(get_db)):
    record = db.query(models.Record).filter(models.Record.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record
