# rorelselogg.py
# Tar emot rörelsedata och loggar det till fliken "Rorelse" i Google Sheets

from services.sheets_writer import skriv_till_sheet
from tidutils import get_datum_tid

def logg_rorelse_intern(data):
    datum, tid = get_datum_tid(data)
    person = data.get("person", "Henrik")
    steg = data.get("steg", 0)
    rorelsetid = data.get("rorelsetid_min", 0)
    kalorier = data.get("kalorier", 0)

    rad = {
        "datum": datum,
        "tid": tid,
        "person": person,
        "steg": steg,
        "rorelsetid_min": rorelsetid,
        "kalorier": kalorier
    }

    skriv_till_sheet(rad, sheet_name="Rorelse")

    return {
        "status": "ok",
        "message": f"✅ Rörelse loggad för {person} ({steg} steg, {kalorier} kcal)"
    }, 200
