from fastapi import APIRouter, HTTPException
from services.sheets_writer import skriv_till_sheet
from tidutils import get_datum_tid

router = APIRouter()

@router.post("/logg")
def logg_maltid(data: dict):
    try:
        datum, tid = get_datum_tid(data)
        person = data.get("person", "Henrik")
        mal = data.get("mal", "")
        innehall = data.get("innehall", "")
        kcal = data.get("kcal", 0)
        protein = data.get("protein", 0)
        fett = data.get("fett", 0)
        mattat_fett = data.get("mattat_fett", 0)
        kolhydrater = data.get("kolhydrater", 0)
        salt = data.get("salt", 0)
        fibrer = data.get("fibrer", 0)
        vatska = data.get("vatska_ml", 0)

        rad = [
            datum, tid, person, mal, innehall,
            kcal, protein, fett, mattat_fett,
            kolhydrater, salt, fibrer, vatska
        ]

        skriv_till_sheet(rad, blad_namn="Mat")

        return {
            "status": "ok",
            "message": f"✅ Mat loggad för {person} kl. {tid}"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fel vid loggning: {str(e)}")
