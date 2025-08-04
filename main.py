import logging
import sys
import os
from fastapi import FastAPI
from routers import matlogg, rorelselog, viktlogg
from utils.sheets_auth import get_sheets_service

# Loggning till stdout (för Railway logs)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

app = FastAPI()


# Registrera alla aktiva endpoints
app.include_router(matlogg.router)
app.include_router(rorelselog.router)
app.include_router(viktlogg.router)


@app.get("/")
def root():
    return {"message": "ViktNinjan API är igång"}

@app.get("/debug-env")
def debug_env():
    return {
        "SERVICE_ACCOUNT_JSON_exists": "SERVICE_ACCOUNT_JSON" in os.environ,
        "SHEET_ID_exists": "SHEET_ID" in os.environ
    }

@app.get("/test-google-auth")
def test_google_auth():
    try:
        sh, sheet_id = get_sheets_service()
        logging.info(f"✅ Autentisering lyckades, ark-ID: {sheet_id}")
        return {"status": "ok", "message": f"✅ Google-auth lyckades. Sheet: {sheet_id}"}
    except Exception as e:
        logging.error(f"❌ Google-auth FEL: {e}", exc_info=True)
        return {"status": "error", "message": str(e)}

# Lokalt (inte nödvändig på Railway men skadar inte)
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
