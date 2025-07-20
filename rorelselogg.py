# rorelselogg.py
# Tar emot rörelsedata och loggar det till fliken "Rorelse" i Google Sheets

from flask import request, jsonify
from auth import sheet

def logg_rorelse():
    data = request.json
    row = [
        data.get("datum", ""),
        data.get("tid", ""),
        data.get("person", ""),
        data.get("steg", ""),
        data.get("rorelsetid_min", ""),
        data.get("kalorier", "")
    ]
    
    sheet.worksheet("Rörelse").append_row(row)
    return jsonify({"status": "OK", "rad": row}), 200
