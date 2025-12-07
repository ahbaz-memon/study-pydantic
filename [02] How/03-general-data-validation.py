from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

# ideal schema
class Patient(BaseModel):
    
    name: str
    age: int
    email: EmailStr # built-in email validation
    linkedin: AnyUrl # url validation
    weight: float
    married: bool = False # setting default val
    allergies: Optional[List[str]] = None # optional need default val
    contact: Dict[str, str] # dict, where keys & values are str

# raw data
patient_info = {
    'name': 'Zeeshan',
    'age': 29,
    'email': 'abc@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/ahbaz-memon/',
    'weight': 62,
    # 'married': False,
    # 'allergies': ['Dust', 'Mold', 'Pollen'],
    'contact': {
        'Mobile': '9126673990',
        'Phone': '020456',
    },
}

# calling
patient = Patient(**patient_info)
print(patient)