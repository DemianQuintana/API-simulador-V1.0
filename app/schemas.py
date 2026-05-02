from typing import Literal

from pydantic import BaseModel, Field


class SimulacionRequest(BaseModel):
    lat: float = Field(
        description="Latitud de la ubicacion a simular.",
        examples=[-31.6475],
    )
    lon: float = Field(
        description="Longitud de la ubicacion a simular.",
        examples=[-60.6985],
    )
    betha: float = Field(
        ge=0,
        le=90,
        description="Inclinacion de los paneles en grados.",
        examples=[30],
    )
    azimuth: float = Field(
        ge=0,
        le=360,
        description="Azimuth de los paneles en grados.",
        examples=[0],
    )
    pot_dc: float = Field(
        gt=0,
        description="Potencia DC instalada de paneles en kW.",
        examples=[5],
    )
    pot_ac: float = Field(
        gt=0,
        description="Potencia AC nominal del inversor en kW.",
        examples=[4],
    )
    tipo_panel: Literal["Estandar", "Premium"] = Field(
        default="Estandar",
        description="Tipo de panel fotovoltaico usado en la simulacion.",
    )
    tipo_montaje: Literal["En techo", "En campo"] = Field(
        default="En techo",
        description="Tipo de montaje del sistema fotovoltaico.",
    )
    perdidas: float = Field(
        default=14.08,
        ge=0,
        le=100,
        description="Perdidas totales del sistema en porcentaje.",
        examples=[14.08],
    )
    eficiencia_inversor: float = Field(
        default=96.0,
        gt=0,
        le=100,
        description="Eficiencia nominal del inversor en porcentaje.",
        examples=[96],
    )


class EnergiaMensual(BaseModel):
    mes: int = Field(
        description="Numero de mes, entre 1 y 12.",
        examples=[1],
    )
    energia: float = Field(
        description="Energia generada durante el mes en kWh.",
        examples=[650.25],
    )


class SimulacionResponse(BaseModel):
    latitud_dataset: float = Field(
        description="Latitud del punto climatico mas cercano usado por el motor.",
        examples=[-31.65],
    )
    longitud_dataset: float = Field(
        description="Longitud del punto climatico mas cercano usado por el motor.",
        examples=[-60.7],
    )
    energia_anual: float = Field(
        description="Energia anual total generada en kWh.",
        examples=[7200.5],
    )
    energia_mensual: list[EnergiaMensual] = Field(
        description="Energia generada por mes en kWh.",
    )
    factor_capacidad: float = Field(
        description="Factor de capacidad anual en porcentaje.",
        examples=[20.55],
    )

