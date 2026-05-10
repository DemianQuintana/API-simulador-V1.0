# API Simulador Fotovoltaico

API local desarrollada con FastAPI para ejecutar el motor de calculo fotovoltaico y devolver resultados de generacion.

## Estructura

```text
app/
  main.py       # Endpoints HTTP de FastAPI
  schemas.py    # Modelos de entrada y salida
  services.py   # Puente entre la API y el motor
motor.py        # Motor de calculo
requirements.txt
```

## Requisitos

- Python 3.10 o superior
- Dataset climatico local:

```text
5_dataset_solar_santa_fe_LOCAL.parquet
```

## Instalacion

Desde la carpeta del proyecto:

```cmd
pip install -r requirements.txt
```

## Ejecutar en desarrollo

```cmd
python -m uvicorn app.main:app --reload
```

La documentacion interactiva queda disponible en:

```text
http://localhost:8000/docs
```

## Ejecutar en produccion

En un entorno de nube no se usa `--reload`.

```cmd
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Algunas plataformas definen el puerto con una variable de entorno llamada `PORT`.

## Endpoint principal

```http
POST /simulaciones
```

Ejemplo de entrada:

```json
{
  "lat": -31.6475,
  "lon": -60.6985,
  "betha": 30,
  "azimuth": 0,
  "pot_dc": 5,
  "pot_ac": 4,
  "tipo_panel": "Estandar",
  "tipo_montaje": "En techo",
  "perdidas": 14.08,
  "eficiencia_inversor": 96
}
```

Ejemplo de salida:

```json
{
  "latitud_dataset": -31.5835,
  "longitud_dataset": -60.6797,
  "energia_anual": 7003.34,
  "energia_mensual": [
    {
      "mes": 1,
      "energia": 660.73
    }
  ],
  "generacion_promedio_horaria_estacional": [
    {
      "estacion": "verano",
      "valores": [
        {
          "hora": 0,
          "energia_promedio": 0.0
        },
        {
          "hora": 12,
          "energia_promedio": 3.12
        }
      ]
    }
  ],
  "factor_capacidad": 19.99
}
```

## Notas

Por ahora la API esta pensada para ejecutarse localmente y simular una sola ubicacion por llamada. Mas adelante se puede agregar autenticacion con API keys y preparar el despliegue en la nube.
