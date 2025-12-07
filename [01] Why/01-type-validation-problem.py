# function written by senior programmer
def insert_patient_data(name: str, age: int): # type hinting

    # assuming database code
    if type(name) == str and type(age) == int: # type forcing
        print(name)
        print(age)

        print("data inserted!")
    else:
        raise TypeError("Wrong data types")

# called by junior programmer
insert_patient_data('Rahul', 'thirty')
insert_patient_data('Rahul', '30')
insert_patient_data('Rahul', 30)