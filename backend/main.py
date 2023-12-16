from typing import Optional
# from fastapi import Depends, FastAPI
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from see_fastdb import name, password, dict_user

import db_model as m
import db_setting as s

king = "fast.db"
async def read_users():
    result = s.session.query(m.Users).all()
    # print(result[1].password)
    return result


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

# def fake_hash_password(password: str):
#     return "fakehashed" + password
def fake_hash_password(password: str):
    return password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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
    print(form_data.username)
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
    return {"sccess_token": user_dict[0][0], "token_type" : "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
    
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users", tags = ["users"])
async def read_users():
    result = s.session.query(m.Users).all()
    print(result.password)
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
    
# @app.get("/items/")
# async def read_items(commons: dict = Depends()):
#     return commons

# @app.get("/users/")
# async def read_users(commons: dict = Depends()):
#     return commons

