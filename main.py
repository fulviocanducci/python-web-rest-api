from fastapi import FastAPI

from routers.login_router import router as login_router
from routers.me_router import router as me_router
from routers.user_router import router as user_router
from routers.credit_router import router as credit_router

app = FastAPI()

app.include_router(user_router)
app.include_router(credit_router)
app.include_router(login_router)
app.include_router(me_router)
