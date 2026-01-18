from typing import List, Dict
from pydantic import BaseModel, EmailStr

class Patient(BaseModel):

    name: str
    age: int
    weight: float # kg
    height: float # mtr
    allergies: List[str]
    married: bool
    email: EmailStr
    contact_details: Dict[str, str]


patient_info = {
    'name': 'Varun',
    'age': '32',
    'weight': 77,
    'height': 1.8,
    'allergies': ['Dust', 'Pollen'],
    'married': True,
    'email': 'varun88@hdfc.com',
    'contact_details':  {
        'Mobile': '8229673990',
        'Phone': '020976',
        # 'Emergency': '9898989898',
    },
}

# calling
patient = Patient(**patient_info)
print(patient)