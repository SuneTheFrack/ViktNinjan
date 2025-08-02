import logging
import sys
from fastapi import FastAPI
from routers import matlogg  # Endast matlogg aktiv just nu


import os

@app.get("/debug-env")
def debug_env():
    return {
        "SERVICE_ACCOUNT_JSON_exists": "SERVICE_ACCOUNT_JSON" in os.environ,
        "SHEET_ID_exists": "SHEET_ID" in os.environ
    }




# Loggning till stdout (för att synas i Railway logs)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

app = FastAPI()

# Registrera routers
app.include_router(matlogg.router)

@app.get("/")
def root():
    return {"message": "ViktNinjan API är igång"}

# Endast vid lokal körning (inte nödvändig på Railway)
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))  # Använd Railway PORT
    uvicorn.run("main:app", host="0.0.0.0", port=port)
