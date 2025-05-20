from pydantic import BaseModel
from typing import List, Optional

class Patient(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    condition: str
    admitted_on: str  
    discharged: bool
    medications: List[str]
    notes: Optional[str] = None

class UpdatePatient(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    condition: Optional[str] = None
    admitted_on: Optional[str] = None
    discharged: Optional[bool] = None
    medications: Optional[List[str]] = None
    notes: Optional[str] = None
