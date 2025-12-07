from pydantic import BaseModel
from typing import List, Dict, Optional

# ideal schema
class Patient(BaseModel):
    
    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None # optional need default val
    contact: Dict[str, str] # dict, where keys & values are str

# raw data
patient_info = {
    'name': 'Zeeshan',
    'age': 22,
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