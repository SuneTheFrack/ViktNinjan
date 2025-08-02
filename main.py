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
