from pydantic import BaseModel

class RecordCreate(BaseModel):
    name: str
    age: int
    score: float

class RecordOut(RecordCreate):
    id: int

    class Config:
        from_attributes = True
