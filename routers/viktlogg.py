# viktlogg.py
# Tar emot viktdata och loggar det till fliken "Vikt" i Google Sheets

from services.sheets_writer import skriv_till_sheet
from tidutils import get_datum_tid

def logg_vikt_intern(data):
    datum, tid = get_datum_tid(data)
    person = data.get("person", "Henrik")
    vikt = data.get("vikt", 0)

    rad = {
        "datum": datum,
        "tid": tid,
        "person": person,
        "vikt": vikt
    }

    skriv_till_sheet(rad, sheet_name="Vikt")

    return {
        "status": "ok",
        "message": f"✅ Vikt loggad för {person}: {vikt} kg kl. {tid}"
    }, 200
