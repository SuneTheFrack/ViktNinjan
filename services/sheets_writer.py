from utils.sheets_auth import get_sheets_service
import os

def skriv_till_sheet(data: dict, sheet_name="Matlogg"):
    service = get_sheets_service()
    sheet = service.spreadsheets()

    # Extrahera kolumner i rätt ordning
    headers = list(data.keys())
    values = list(data.values())

    # Sätt upp body som en ny rad
    body = {
        "values": [values]
    }

    # Bygg range (ex: Matlogg!A1)
    range_to_use = f"{sheet_name}!A1"

    # Lägg till raden
    result = sheet.values().append(
        spreadsheetId=os.environ["SHEET_ID"],
        range=range_to_use,
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()

    return result
