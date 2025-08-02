
from utils.sheets_auth import get_sheets_service

def skriv_till_sheet(rad, blad_namn="Mat"):
    print("📤 Försöker skriva rad till Google Sheet:")
    print("Blad:", blad_namn)
    print("Data:", rad)

    try:
        sheet = get_sheets_service()
        worksheet = sheet.worksheet(blad_namn)
        worksheet.append_row(rad, value_input_option="USER_ENTERED")
        print("✅ Skrivning lyckades")
    except Exception as e:
        print("❌ Fel vid skrivning till Google Sheet:", str(e))
        raise
