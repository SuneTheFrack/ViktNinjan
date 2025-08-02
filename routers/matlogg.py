# matlogg.py
# FastAPI-router som tar emot måltidsdata och loggar det till fliken "Mat" i Google Sheets

from fastapi import APIRouter, HTTPException, Request
from services.sheets_writer import skriv_till_sheet
from tidutils import get_datum_tid

router = APIRouter()

@router.post("/logg")
async def logg_mat(request: Request):
    data = await request.json()
    if "person" not in data or "innehall" not in data or "kcal" not in data:
        raise HTTPException(status_code=400, detail="person, innehall och kcal krävs")

    datum, tid = get_datum_tid(data)
    person = data.get("person", "Henrik")

    rad = {
        "datum": datum,
        "tid": tid,
        "person": person,
        "mal": data.get("mal", ""),
        "innehall": data.get("innehall", ""),
        "kcal": data.get("kcal", 0),
        "protein": data.get("protein", 0),
        "fett": data.get("fett", 0),
        "mattat_fett": data.get("mattat_fett", 0),
        "kolhydrater": data.get("kolhydrater", 0),
        "salt": data.get("salt", 0),
        "fibrer": data.get("fibrer", 0),
        "vatska_ml": data.get("vatska_ml", 0)
    }

    skriv_till_sheet(rad, sheet_name="Mat")

    return {
        "status": "ok",
        "message": f"✅ Mat loggad för {person} kl. {tid}"
    }
