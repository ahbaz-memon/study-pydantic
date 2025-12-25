from typing import List, Dict
from pydantic import BaseModel, EmailStr

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    allergies: List[str]
    married: bool
    email: EmailStr
    contact_details: Dict[str, str]


