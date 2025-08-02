import os
from utils.sheets_auth import get_sheets_service
import logging

def skriv_till_sheet(rad: list, blad_namn="Mat"):
    logging.info(f"Försöker skriva rad till blad '{blad_namn}': {rad}")
    try:
        service, sheet_id = get_sheets_service()
        logging.info(f"Service och Sheet-ID hämtat: {sheet_id}")
        sheet = service.worksheet(blad_namn)
        sheet.append_row(rad)
        logging.info("Rad tillagd i Sheet.")
    except Exception as e:
        logging.error(f"Fel vid skrivning till Google Sheets: {e}")
        raise
