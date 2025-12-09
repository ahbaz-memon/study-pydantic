from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

# ideal schema
class Patient(BaseModel):
    
    name: str = Field(
        max_length=50,
        title='patient name',
        description='give the name of patient',
        examples=['Ratan', 'Jatin'],
    )
    age: int = Field(ge=18, lt=60) # 18 <= age < 60
    email: EmailStr # built-in email validation
    linkedin: AnyUrl # url validation
    weight: float = Field(gt=0) # only positive
    married: bool = False # setting default val
    allergies: Optional[List[str]] = Field(max_length=5, default=None) # optional need default val
    contact: Dict[str, str] # dict, where keys & values are str

# raw data
patient_info = {
    'name': 'Zeeshan',
    'age': 29,
    'email': 'abc@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/ahbaz-memon/',
    'weight': 62,
    'married': False,
    # 'allergies': ['Dust', 'Mold', 'Pollen'],
    'contact': {
        'Mobile': '9126673990',
        'Phone': '020456',
    },
}

# calling
patient = Patient(**patient_info)
print(patient)