from pydantic import BaseModel
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
    id: int
    title: str
    description: str
    completed: bool
    priority: Priority
