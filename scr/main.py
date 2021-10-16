from fastapi import FastAPI
import services as _services,schemas as _schemas
import sqlalchemy.orm as _orm

app = FastAPI

_services.create_database()
#Now we can create our endpoint

@app.post("users/",response_model=_schemas.User)
def create_user(user:_schemas.UserCreate,db:_orm.Session=FastAPI.depends(_services.get_db)):
   db_user= _services.get_user_by_email(db=db,email=user.email)
   if db_user:
       raise FastAPI.HTTPException(status_code=400,detail="woop the email is in use")

   return _services.create_user(db=db,user=user)