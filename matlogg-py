# matlogg.py
# Tar emot måltidsdata och loggar det till fliken "Mat" i Google Sheets

from flask import request, jsonify
from auth import sheet

def logg_maltid():
    data = request.json

    # kallar på datum i utils
    datum, tid = get_datum_tid(data)

    row = [
        data.get("datum", ""),
        data.get("tid", ""),
        data.get("person", ""),
        data.get("mal", ""),
        data.get("innehall", ""),
        data.get("kcal", ""),
        data.get("protein", ""),
        data.get("fett", ""),
        data.get("mattat_fett", ""),
        data.get("kolhydrater", ""),
        data.get("salt", ""),
        data.get("fibrer", ""),
        data.get("vatska_ml", "")
    ]
    
    sheet.worksheet("Mat").append_row(row)
    return jsonify({"status": "OK", "rad": row}), 200
