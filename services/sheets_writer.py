import logging
from utils.sheets_auth import get_sheets_service

def skriv_till_sheet(rad: list, blad_namn="Mat"):
    try:
        sh, sheet_id = get_sheets_service()
        worksheet = sh.worksheet(blad_namn)
        worksheet.append_row(rad)
        logging.info(f"✅ Skrev till blad '{blad_namn}': {rad}")
    except Exception as e:
        logging.error(f"❌ Kunde inte skriva till Google Sheet: {e}", exc_info=True)
        raise
