from fastapi import FastAPI

from routers.credit_router import router as credit_router

app = FastAPI()

app.include_router(credit_router)
