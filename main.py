
from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json

app = Flask(__name__)

# Google Sheets-auth från miljövariabel
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds_json = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(os.environ["SHEET_ID"]).sheet1

@app.route('/loggmaltid', methods=['POST'])
def logg_maltid():
    data = request.json
    datum = data.get("datum", "")
    tid = data.get("tid", "")
    person = data.get("person", "")
    mål = data.get("mål", "")
    innehåll = data.get("innehåll", "")
    kcal = data.get("kcal", "")
    fett = data.get("fett", "")
    mättat_fett = data.get("mättat_fett", "")
    salt = data.get("salt", "")
    fibrer = data.get("fibrer", "")

    row = [datum, tid, person, mål, innehåll, kcal, fett, mättat_fett, salt, fibrer]
    sheet.append_row(row)
    return jsonify({"status": "OK", "rad": row}), 200
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
