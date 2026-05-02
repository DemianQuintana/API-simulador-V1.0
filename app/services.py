from app.schemas import SimulacionRequest
from motor import calcular_generacion


def ejecutar_simulacion(payload: SimulacionRequest):
    return calcular_generacion(payload.model_dump())
