from fastapi import APIRouter, HTTPException
from .models import Patient, UpdatePatient
from .database import load_data, save_data

router = APIRouter()

@router.get("/")
def root():
    return {"message": "FastAPI Patient Manager is running"}

@router.get("/patients")
def get_all_patients():
    return load_data()

@router.get("/patients/{id}")
def get_patient(id: int):
    patients = load_data()
    for p in patients:
        if p["id"] == id:
            return p
    raise HTTPException(status_code=404, detail="Patient not found")

@router.post("/patients")
def add_patient(patient: Patient):
    patients = load_data()
    if any(p["id"] == patient.id for p in patients):
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    patients.append(patient.dict())
    save_data(patients)
    return {"message": "Patient added successfully"}

@router.put("/patients/{id}")
def update_patient(id: int, updated: UpdatePatient):
    patients = load_data()
    for index, p in enumerate(patients):
        if p["id"] == id:
            updated_data = {**p, **updated.dict(exclude_unset=True)}
            patients[index] = updated_data
            save_data(patients)
            return {"message": "Patient updated successfully"}
    raise HTTPException(status_code=404, detail="Patient not found")

@router.delete("/patients/{id}")
def delete_patient(id: int):
    patients = load_data()
    new_patients = [p for p in patients if p["id"] != id]
    if len(new_patients) == len(patients):
        raise HTTPException(status_code=404, detail="Patient not found")
    save_data(new_patients)
    return {"message": "Patient deleted successfully"}
