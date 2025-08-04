from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from services.sheets_writer import logga_data
from tidutils import get_datum_tid
import logging

router = APIRouter()

class MaltidsData(BaseModel):
    person: Optional[str] = "Henrik"
    mal: Optional[str] = ""
    innehall: str
    kcal: float
    protein: float
    fett: float
    mattat_fett: float
    kolhydrater: float
    salt: float
    fibrer: Optional[float] = 0
    vatska_ml: Optional[float] = 0

@router.post("/logg")
def logg_maltid(data: MaltidsData):
    try:
        data_dict = data.dict()

        datum, tid = get_datum_tid(data_dict)
        data_dict["datum"] = datum
        data_dict["tid"] = tid

        logging.info(f"➡️ Inkommande data: {data_dict}")
        logga_data(data_dict, blad_namn="Mat")

        return {
            "status": "ok",
            "message": f"✅ Mat loggad för {data.person} kl. {tid}"
        }

    except Exception as e:
        logging.error(f"❌ Fel vid loggning: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Fel vid loggning: {str(e)}")
