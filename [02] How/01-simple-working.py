from pydantic import BaseModel

# ideal schema
class Patient(BaseModel):
    name: str
    age: int

# function written by senior programmer
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)

    print("data inserted!")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)

    print("data updated!")

# raw data
# patient_info = {'name': 'Sid', 'age': 'thirty'}
patient_info = {'name': 'Sid', 'age': '30'}

# calling
patient = Patient(**patient_info)
insert_patient_data(patient)
update_patient_data(patient)