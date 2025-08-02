# sheets_reader.py
# Läser preferenser från Google Sheets-bladet "Preferenser"

from utils.sheets_auth import get_sheets_service
import os

def get_preferences(person: str):
    service = get_sheets_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=os.environ["SHEET_ID"],
        range="Preferenser!A1:Z100"
    ).execute()

    rows = result.get("values", [])
    if not rows:
        return None

    headers = rows[0]
    for row in rows[1:]:
        if row[0].strip().lower() == person.strip().lower():
            return {headers[i]: row[i] if i < len(row) else "" for i in range(len(headers))}
    return None
