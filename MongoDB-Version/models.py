from pydantic import BaseModel, Field, field_validator
from bson import ObjectId
from enum import Enum
from typing import Optional

class Priority(str, Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'    

class CreateTask(BaseModel):
    title: str
    description: str = ""
    completed: bool = False
    priority: Priority = Priority.low
    
class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[Priority] = None
    
 
class Task(BaseModel):
    id: str = Field(alias='_id')
    title: str
    description: str
    completed: bool
    priority: Priority
    
    model_config = {
        'populate_by_name':True
    }
    
    @field_validator("id", mode="before")
    @classmethod
    def validate_id(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v
    