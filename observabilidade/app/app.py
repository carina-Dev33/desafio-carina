import logging
import random
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("dice-api")

app = FastAPI(title="dice-api", version="dev")

@app.get("/")
async def roll_dice():
    value = random.randint(1, 6)
    logger.info(f"Rolou o dado: {value}")
    return {"dice": value}

@app.get("/health")
async def health():
    logger.info("Health check chamado")
    return {"status": "ok", "app": "dice-api", "version": "dev"}

@app.get("/fail")
async def fail():
    logger.error("Erro proposital gerado")
    raise Exception("Erro proposital para teste")

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.exception(f"Erro não tratado em {request.url.path}")
    return JSONResponse(status_code=500, content={"detail": str(exc)})