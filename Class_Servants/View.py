from fastapi import FastAPI,status,Body,Path,HTTPException,APIRouter,Depends
from Connection.Connection_DB import SessionLocal,engine
from Class_Servants.Model import *
from Class_Servants.schema import *
from fastapi.responses import JSONResponse 
from fastapi.encoders import jsonable_encoder

class Class_Servants:
    router = APIRouter()
    
    @router.get(path="/class_servants/view",status_code=status.HTTP_200_OK,
            summary="Show all class of servants",tags=["Class Servants"])
    def read_class():
        db = SessionLocal()
        consult = db.query(Class_Servant).all()
        return JSONResponse(status_code=200,content=jsonable_encoder(consult))
    
    @router.get(path='/search/class/servants/{id}',status_code=status.HTTP_200_OK,
            summary="Search class of servants",tags=["Class Servants"])
    def search_class(id : int):
        db = SessionLocal()
        consult =db.query(Class_Servant).filter(Class_Servant.id==id).first()
        if not consult:
            return JSONResponse(status_code=404,content={'message':'No encontrado'})
        return JSONResponse(status_code=200,content=jsonable_encoder(consult))
    
    @router.post(path="/created/class/servants",status_code=status.HTTP_201_CREATED,
            summary="Created class of servants",response_model=dict,tags=["Class Servants"])
    def post_class(class_servant:schema_Class_Servant):
        db = SessionLocal()
        new_class_servant = Class_Servant(**class_servant.dict())
        db.add(new_class_servant)
        db.commit()
        return JSONResponse(status_code=201,content={'message':'Se ha registrado'})

    @router.put(path="/edit/class/servants/{id}",status_code=status.HTTP_200_OK,
            summary="Edit class of servants",tags=["Class Servants"])
    def put_class(id:int,class_servant:schema_Class_Servant):
        db = SessionLocal()
        consult =db.query(Class_Servant).filter(Class_Servant.id==id).first()
        if not consult:
             return JSONResponse(status_code=404,content={'message':'No encontrado'})
        consult.name_Class = class_servant.name_Class
        db.commit()
        return JSONResponse(status_code=201,content={'message':'Se ha modificado este dato'})
    
    @router.delete(path="/delete/class/servants",status_code=status.HTTP_200_OK,
            summary="Delete class of servants",tags=["Class Servants"])
    def delete_class(id:int):
        db = SessionLocal()
        consult =db.query(Class_Servant).filter(Class_Servant.id==id).first()
        if not consult:
             return JSONResponse(status_code=404,content={'message':'No encontrado'})
        
        db.delete(consult)
        db.commit()
        return JSONResponse(status_code=201,content={'message':'Ya se borro la información'})