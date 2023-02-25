from fastapi import FastAPI,status,Body,Path,HTTPException,APIRouter,Depends
from Connection.Connection_DB import SessionLocal,engine

from Servants.Model import *
from Servants.schema import *
from fastapi.responses import JSONResponse 
from fastapi.encoders import jsonable_encoder

class Servants:
    router = APIRouter()
    
    @router.get(path="/servants/view",status_code=status.HTTP_200_OK,
            summary="Show all servants data",tags=["Servants"])
    def read_servant():
        db = SessionLocal()
        consult = db.query(Servant).all()
        return JSONResponse(status_code=200,content=jsonable_encoder(consult))

    
    @router.get(path='/search/servants/{id}',status_code=status.HTTP_200_OK,
            summary="Servant data search",tags=["Servants"])
    def search_servant(id : int):
        db = SessionLocal()
        consult =db.query(Servant).filter(Servant.id_Servant==id).first()
        if not consult:
            return JSONResponse(status_code=404,content={'message':'No encontrado'})
        return JSONResponse(status_code=200,content=jsonable_encoder(consult))
    
    @router.post(path="/create/servants",status_code=status.HTTP_201_CREATED,
            summary="Create servant data",response_model=dict,tags=["Servants"])
    def post_servant(schema_servant:schema_Servants,id_class: int):
        db = SessionLocal()
        new_class_servant = Servant( owner_id=id_class,**schema_servant.dict())
        db.add(new_class_servant)
        db.commit()
        return JSONResponse(status_code=201,content={'message':'Se ha registrado'})
    
    @router.put(path='/edit/servants/{id}',status_code=status.HTTP_200_OK,
            summary="Edit servant data",tags=["Servants"])
    def put_servant(schema_servant:schema_Servants,id : int):
        db = SessionLocal()
        consult =db.query(Servant).filter(Servant.id_Servant==id).first()
        if not consult:
            return JSONResponse(status_code=404,content={'message':'No encontrado'})
        
        consult.name_Servant = schema_servant.name_Servant
        consult.skill_One = schema_servant.skill_One
        consult.skill_Two = schema_servant.skill_Two
        consult.skill_Three = schema_servant.skill_Three
        consult.noble_Phantasm = schema_servant.noble_Phantasm
        consult.type_Noble_phantasm = schema_servant.type_Noble_phantasm
        
        db.commit()
        return JSONResponse(status_code=200,content={'message':'Se ha modificado este dato'})
    
    @router.delete(path="/delete/servants",status_code=status.HTTP_200_OK,
            summary="Delete servant data",tags=["Servants"])
    def delete_class(id:int):
        db = SessionLocal()
        consult =db.query(Servant).filter(Servant.id_Servant==id).first()
        if not consult:
             return JSONResponse(status_code=404,content={'message':'No encontrado'})
        
        db.delete(consult)
        db.commit()
        return JSONResponse(status_code=201,content={'message':'Ya se borro la información'})
    