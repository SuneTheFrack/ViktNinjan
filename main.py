from flask import Flask, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

app = Flask(__name__)

# Setup Google Sheets credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Öppna arket – byt till ditt eget ark-namn
sheet = client.open("ViktNinjan").sheet1

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
    return {"status": "OK", "rad": row}, 200

app.run(host='0.0.0.0', port=81)