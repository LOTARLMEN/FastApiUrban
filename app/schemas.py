from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    age: int

class UpdateUser(BaseModel):
    first_name: str
    last_name: str
    age: int

class CreateTask(BaseModel):
    title: str
    content: str
    priority: int

class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int