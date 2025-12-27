from typing import List, Dict
from pydantic import BaseModel, EmailStr, field_validator

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    allergies: List[str]
    married: bool
    email: EmailStr
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_domain_validator(cls, value): # cls for class instance, to get other function

        valid_domains = ['hdfc.com', 'icici.com', 'axis.com'] # if employee of...
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError("Not a valid domain")

        return value


patient_info = {
    'name': 'Varun',
    'age': 32,
    'weight': 77,
    'allergies': ['Dust', 'Pollen'],
    'married': True,
    'email': 'varun88@hdfc.com',
    'contact_details':  {
        'Mobile': '8229673990',
        'Phone': '020976',
    },
}

# calling
patient = Patient(**patient_info)
print(patient)