from fastapi import APIRouter, HTTPException
from services.sheets_reader import get_preferences

router = APIRouter()

@router.get("/preferenser")
def get_preferenser(person: str):
    prefs = get_preferences(person)
    if not prefs:
        raise HTTPException(status_code=404, detail="Person ej hittad")
    return prefs
