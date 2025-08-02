import logging
from utils.sheets_auth import get_sheets_service
import logging
from fastapi import FastAPI
from utils.sheets_auth import get_sheets_service

app = FastAPI()

@app.get("/test-google-auth")
def test_google_auth():
    try:
        sh, sheet_id = get_sheets_service()
        logging.info(f"✅ Autentisering lyckades, ark-ID: {sheet_id}")
        return {"status": "ok", "message": f"✅ Google-auth lyckades. Sheet: {sheet_id}"}
    except Exception as e:
        logging.error(f"❌ Google-auth FEL: {e}", exc_info=True)
        return {"status": "error", "message": str(e)}


def skriv_till_sheet(rad: list, blad_namn="Mat"):
    try:
        sh, sheet_id = get_sheets_service()
        worksheet = sh.worksheet(blad_namn)
        worksheet.append_row(rad)
        logging.info(f"✅ Skrev till blad '{blad_namn}': {rad}")
    except Exception as e:
        logging.error(f"❌ Kunde inte skriva till Google Sheet: {e}", exc_info=True)
        raise
