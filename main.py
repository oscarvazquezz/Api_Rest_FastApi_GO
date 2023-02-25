from fastapi import FastAPI,Request
from Connection.Connection_DB import Base,engine,SessionLocal
from Class_Servants.Model import *
from Class_Servants.View import *
from middlewares.error_handler import ErrorHandler
from Servants.View import *
from Servants.Model import *

app = FastAPI()
app.title = "Appi of Fate Grand Orden"

app.add_middleware(ErrorHandler)
Base.metadata.create_all(bind=engine)

#>uvicorn main:app --reload
Class_View = Class_Servants()
app.include_router(Class_View.router)
Servant_View =Servants()
app.include_router(Servant_View.router)