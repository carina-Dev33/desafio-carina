import logging
import random

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from opentelemetry import metrics
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("dice-api")

app = FastAPI(title="dice-api", version="dev")
FastAPIInstrumentor.instrument_app(app)

meter = metrics.get_meter(__name__)
roll_counter = meter.create_counter(
    name="dice_rolls_total",
    description="Total de lançamentos do dado",
    unit="1",
)
error_counter = meter.create_counter(
    name="dice_errors_total",
    description="Total de erros da aplicação",
    unit="1",
)

@app.get("/")
async def roll_dice():
    value = random.randint(1, 6)
    roll_counter.add(1, {"route": "/", "result": str(value)})
    logger.info("Rolou o dado: %s", value)
    return {"dice": value}

@app.get("/health")
async def health():
    logger.info("Health check chamado")
    return {"status": "ok", "app": "dice-api", "version": "dev"}

@app.get("/fail")
async def fail():
    error_counter.add(1, {"route": "/fail"})
    logger.error("Erro proposital gerado")
    raise Exception("Erro proposital para teste de observabilidade")

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.exception("Erro não tratado em %s", request.url.path)
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
    )