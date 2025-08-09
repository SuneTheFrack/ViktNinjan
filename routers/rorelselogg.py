from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import logging

from rorelselogg import logg_rorelse_intern

router = APIRouter()

# Modell för inkommande data
class RorelseData(BaseModel):
    person: Optional[str] = "Henrik"
    steg: Optional[int] = 0
    minuter: Optional[float] = 0
    kalorier: Optional[float] = 0

@router.post("/loggrorelse")
def loggrorelse(data: RorelseData):
    try:
        data_dict = data.dict()
        logging.info(f"➡️ Inkommande rörelsedata: {data_dict}")

        resultat, status = logg_rorelse_intern(data_dict)
        return resultat

    except Exception as e:
        logging.error(f"❌ Fel vid rörelselogging: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Fel vid loggning: {str(e)}")
