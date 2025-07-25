# matlogg.py
# Tar emot måltidsdata och loggar det till fliken "Mat" i Google Sheets

from flask import request, jsonify
from auth import sheet
from tidutils import get_datum_tid

def logg_maltid_intern(data):
    datum, tid = get_datum_tid(data)
    person = data.get("person", "Henrik")
    innehall = data.get("innehall", "")
    kcal = data.get("kcal", 0)
    fett = data.get("fett", 0)
    vatska = data.get("vatska_ml", 0)

    # Anpassa rad efter dina kolumner i bladet "Mat"
    rad = [datum, tid, person, innehall, kcal, fett, vatska]

    skriv_till_sheet(rad, blad_namn="Mat")

    return jsonify({
        "status": "ok",
        "message": f"✅ Mat loggad för {person} kl. {tid}"
    }), 200
