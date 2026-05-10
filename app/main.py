import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import SimulacionRequest, SimulacionResponse
from app.services import ejecutar_simulacion


def obtener_origenes_cors():
    origenes = os.getenv("CORS_ORIGINS")
    if not origenes:
        return ["*"]

    return [
        origen.strip()
        for origen in origenes.split(",")
        if origen.strip()
    ]


app = FastAPI(
    title="API Simulador Fotovoltaico",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=obtener_origenes_cors(),
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "API Simulador Fotovoltaico",
        "health": "/health",
        "docs": "/docs",
        "simulaciones": "/simulaciones",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/simulaciones", response_model=SimulacionResponse)
def simular(payload: SimulacionRequest):
    try:
        return ejecutar_simulacion(payload)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
