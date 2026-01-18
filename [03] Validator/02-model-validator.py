from typing import List, Dict
from pydantic import BaseModel, EmailStr, model_validator

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    allergies: List[str]
    married: bool
    email: EmailStr
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def check_elderly_have_emergency_contact(cls, model):

        if model.age > 60:
            if 'Emergency' not in model.contact_details:
                raise ValueError("Elderly must have emergency contact number")
        
        return model


patient_info = {
    'name': 'Varun',
    'age': '32',
    'weight': 77,
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