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

patient_info = {
    'name': 'Varun',
    'age': 32,
    'weight': 77,
    'allergies': ['Dust', 'Pollen'],
    'married': True,
    'email': 'varun88@gmail.com',
    'contact_details':  {
        'Mobile': '8229673990',
        'Phone': '020976',
    },
}


# calling
patient = Patient(**patient_info)
print(patient)