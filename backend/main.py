from typing import Optional
# from fastapi import Depends, FastAPI
from fastapi import FastAPI, Depends, HTTPException, status, File
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from see_fastdb import name, password, dict_user
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from starlette.requests import Request
from starlette.routing import Route
from createImageFromText2 import createImageFromText
from googleTranslate import googleTranslate

import db_model as m
import db_setting as s

import path_models as pm
import path_settings as ps


king = "fast.db"

async def path_read():
    result = ps.session.query(pm.Users).all()
    # print(result[1].password)
    return result

async def read_users():
    result = s.session.query(m.Users).all()
    # print(result[1].password)
    return result


# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "fakehashedsecret",
#         "disabled": False,
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "Alice Wonderson",
#         "email": "alice@example.com",
#         "hashed_password": "fakehashedsecret2",
#         "disabled": True,
#     },
# }

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# def fake_hash_password(password: str):
#     return "fakehashed" + password
def fake_hash_password(password: str):
    return password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class PathBase(BaseModel):
    id : int
    path : str
    name : str
      
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    name : str
    
class UserBase(BaseModel):
    name : str
    password : str
    url_num : int
    url : str

# def get_user(db, name: str):
def get_user(name:str):
    db = name(king)
    if name in db:
        user_dict = dict_user(king, name)
        return UserInDB(**user_dict)
    
def fake_decode_token(token):
    result = read_users()
    user = get_user(result, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invaild authentication credentials",
            headers = {"WWW-Authenticate" : "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail = "Inactive user")
    return current_user

# async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # result = read_users()
    # user_dict = fake_users_db.get(form_data.username)
    # print(user_dict)
    user_dict = dict_user(king, form_data.username)
    if user_dict == None:
        raise HTTPException(status_code=400, detail = "Incorrect username or password")
    if not user_dict:
            raise HTTPException(status_code=400, detail = "username or password none")
    # user = UserInDB(**user_dict)
    user = user_dict[0][1]
    hashed_password = fake_hash_password(form_data.password)
    # hashed_password = password(king)
    if not hashed_password == user:
        raise HTTPException(status_code=400, detail = "Incorrect username or password")
    return {"access_token": user_dict[0][0], "token_type" : "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
    
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users", tags = ["users"])
async def read_users():
    result = s.session.query(m.Users).all()
    # print(result.password)
    return result

@app.post("/users", tags = ["users"])
async def create_user(data: UserBase):
    user = m.Users()
    session = s.session()
    s.session.add(user)
    
    try:
        user.name = data.name
        user.password = data.password
        user.url_num = data.url_num
        user.url = data.url
        session.commit()
    except():
        session.rollback()
        raise
    finally:
        session.close()
        
@app.delete("/users/{name}", tags = ["users"])
async def delete_user(name: str):
    session = s.session()
    try:
        query = s.session.query(m.Users)
        query = query.filter(m.User.user_name == name)
        query.delete()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    
@app.put("/users/{name}", tags = ["users"])
async def update_user(name: str, data:UserBase):
    session = s.session()
    try:
        s.session.query(m.Users).\
        filter(m.Users.user_id == id).\
        update({"name" : data.name, "password" : data.password, "url_num" : data.url_num, "url" : data.url})
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        
@app.get("/path", tags = ["path"])
async def read_path():
    result = ps.session.query(pm.Users).all()
    print(result.path)
    return result
    
    
@app.post("/path", tags = ["path"])
async def create_user(data: PathBase):
    user = pm.Users()
    session = ps.session()
    ps.session.add(user)
    
    try:
        user.id = data.id
        user.path = data.path
        user.name = data.name
        # user.url = data.url
        session.commit()
    except():
        session.rollback()
        raise
    finally:
        session.close()
        
@app.put("/path/{id}", tags = ["path"])
async def update_user(name: str, data:PathBase):
    session = ps.session()
    try:
        ps.session.query(pm.Users).\
        filter(pm.Users.user_id == id).\
        update({"id" : data.id, "path" : data.path, "name" : data.name})
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


@app.delete("/path/{id}", tags = ["path"])
async def delete_user(id: int):
    session = ps.session()
    try:
        query = ps.session.query(pm.Users)
        query = query.filter(pm.User.id == id)
        query.delete()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        
# @app.get("/items/")
# async def read_items(commons: dict = Depends()):
#     return commons

# @app.get("/users/")
# async def read_users(commons: dict = Depends()):
#     return commons

@app.post("/prompt")
async def getPromptTemp(request: Request, promptTextTemp: str):
    PromptTextJp = googleTranslate(promptTextTemp)
    img, imageName = createImageFromText(PromptTextJp)
    # return FileResponse(img, media_type="image/png"), imageName
    return imageName