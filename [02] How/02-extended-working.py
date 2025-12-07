from pydantic import BaseModel
from typing import List, Dict

# ideal schema
class Patient(BaseModel):
    
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str] # list of str
    contact: Dict[str, str] # dict, where keys & values are str
