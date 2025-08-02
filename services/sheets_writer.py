from utils.sheets_auth import get_sheets_service
import logging

def skriv_till_sheet(rad: list, blad_namn="Mat"):
    try:
        service, sheet_id = get_sheets_service()
        sheet = service.worksheet(blad_namn)
        sheet.append_row(rad)
    except Exception as e:
        logging.error(f"Fel vid skrivning till Google Sheets: {e}")
        raise
