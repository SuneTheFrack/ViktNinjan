# viklogg.py – Loggar viktdata med fler kolumner till Google Sheet-bladet "Vikt"
from services.sheets_writer import skriv_till_sheet
from tidutils import get_datum_tid

def logg_vikt_intern(data):
    datum, tid = get_datum_tid(data)
    person = data.get("person", "Henrik")
    vikt = data.get("vikt", 0)
    muskelvikt = data.get("muskelvikt", 0)
    fettprocent = data.get("fettprocent", 0)
    vattenprocent = data.get("vattenprocent", 0)
    bmr = data.get("bmr", 0)

    rad = [
        datum,
        tid,
        person,
        vikt,
        muskelvikt,
        fettprocent,
        vattenprocent,
        bmr
    ]

    skriv_till_sheet(rad, blad_namn="Vikt")

    return {
        "status": "ok",
        "message": f"✅ Viktdata loggat för {person} ({vikt} kg)"
    }, 200
