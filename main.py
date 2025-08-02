import logging

logging.basicConfig(level=logging.INFO)

from fastapi import FastAPI
from routers import matlogg, viktlogg, rorelselogg, preferences

app = FastAPI()

app.include_router(matlogg.router)
# app.include_router(viktlogg.router)
# app.include_router(rorelselogg.router)
# app.include_router(preferenser.router)

@app.get("/")
def root():
    return {"message": "ViktNinjan API är igång"}

if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.environ.get("PORT", 8000))  # Default till 8000 om PORT inte finns
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
