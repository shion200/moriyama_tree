from typing import Optional
# from fastapi import Depends, FastAPI
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

import db_model as m
import db_setting as s


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

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str
    
class UserBase(BaseModel):
    name : str
    mail : str
    sex : str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    
def fake_decode_token(token):
    user = get_user(fake_users_db, token)
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

async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail = "Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail = "Incorrect username or password")
    return {"sccess_token": user.username, "token_type" : "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
    
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("users", tags = ["users"])
async def read_users():
    result = s.session.query(m.Users).all()
    return result

@app.post("/users", tags = ["users"])
async def create_user(data: UserBase):
    user = m.Users()
    session = s.session()
    s.session.add(user)
    
    try:
        user.name = data.name
        user.mail = data.mail
        user.sex = data.sex
        session.commit()
    except():
        session.rollback()
        raise
    finally:
        session.close()
        
@app.delete("/users/{id}", tags = ["users"])
async def delete_user(id: int):
    session = s.session()
    try:
        query = s.session.query(m.Users)
        query = query.filter(m.User.user_id == id)
        query.delete()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    
@app.put("/users/{id}", tags = ["users"])
async def update_user(id: int, data:UserBase):
    session = s.session()
    try:
        s.session.query(m.Users).\
        filter(m.Users.user_id == id).\
        update({"name" : data.name, "mail" : data.mail, "sex" : data.sex})
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

