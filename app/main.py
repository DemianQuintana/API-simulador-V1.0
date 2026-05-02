from fastapi import FastAPI, HTTPException

from app.schemas import SimulacionRequest, SimulacionResponse
from app.services import ejecutar_simulacion

app = FastAPI(
    title="API Simulador Fotovoltaico",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/simulaciones", response_model=SimulacionResponse)
def simular(payload: SimulacionRequest):
    try:
        return ejecutar_simulacion(payload)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
