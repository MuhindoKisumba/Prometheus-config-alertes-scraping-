############################################################
# METRICS PROMETHEUS (FASTAPI)
############################################################

from fastapi import FastAPI
from prometheus_client import Counter, Gauge, generate_latest
from fastapi.responses import Response

app = FastAPI()

cas_total = Counter('cas_total', 'Nombre total de cas')
temperature = Gauge('temperature', 'Temperature actuelle')

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

@app.get("/simulate")
def simulate():
    cas_total.inc(10)
    temperature.set(30)
    return {"status":"ok"}