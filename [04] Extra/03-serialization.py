from pprint import pprint
from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    country: str
    pin_code: int

class Employee(BaseModel):

    name: str
    age: int
    gender: str
    address: Address


employee_info = {
    'name': 'Pratik',
    'age': 27,
    'gender': 'male',
    'address': Address(**{
        'city': 'Pune',
        'state': 'Maharashtra',
        'country': 'India',
        'pin_code': 411040,
    })
}
employee = Employee(**employee_info)


# exporting model in python dict
dumped = employee.model_dump()
print(type(dumped))
pprint(dumped)

# controlling field, while exporting
dumped = employee.model_dump(exclude={'address': ['country']})
pprint(dumped)