# viktlogg.py
# Tar emot viktdata och loggar det till fliken "Vikt" i Google Sheets

from flask import request, jsonify
from auth import sheet

def logg_vikt():
    data = request.json
    row = [
        data.get("datum", ""),
        data.get("tid", ""),
        data.get("person", ""),
        data.get("vikt", "")
    ]
    
    sheet.worksheet("Vikt").append_row(row)
    return jsonify({"status": "OK", "rad": row}), 200

