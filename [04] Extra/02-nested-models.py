from pprint import pprint
from pydantic import BaseModel



class Employee(BaseModel):

    name: str
    age: int
    gender: str


employee_info = {
    'name': 'Pratik',
    'age': 27,
    'gender': 'male',
}
employee = Employee(**employee_info)
pprint(employee)