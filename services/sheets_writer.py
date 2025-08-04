import logging
from utils.sheets_auth import get_sheets_service
from fastapi import FastAPI

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

# ✍️ Enklare radskrivning om du redan har rätt lista
def skriv_till_sheet(rad: list, blad_namn="Mat"):
    try:
        sh, _ = get_sheets_service()
        worksheet = sh.worksheet(blad_namn)
        worksheet.append_row(rad)
        logging.info(f"✅ Skrev till blad '{blad_namn}': {rad}")
    except Exception as e:
        logging.error(f"❌ Kunde inte skriva till Google Sheet: {e}", exc_info=True)
        raise

# ✅ Flexibel loggning baserat på kolumnnamn i bladet
def logga_data(data: dict, blad_namn="Mat"):
    try:
        sh, _ = get_sheets_service()
        blad = sh.worksheet(blad_namn)

        # Hämtar rubriker från första raden
        kolumner = blad.row_values(1)

        # Matchar inkommande data mot rubrikerna
        rad = [data.get(k, "") for k in kolumner]

        blad.append_row(rad)
        logging.info(f"✅ Loggade till '{blad_namn}': {rad}")
    except Exception as e:
        logging.error(f"❌ Fel vid loggning till Google Sheet: {e}", exc_info=True)
        raise
