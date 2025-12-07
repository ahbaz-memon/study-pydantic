# function written by senior programmer
def insert_patient_data(name: str, age: int): # type hinting

    # assuming database code
    if type(name) == str and type(age) == int: # type forcing
        if age > 0:
            print(name)
            print(age)

            print("data inserted!")
        else:
            ValueError("Age cannot be negative!")
    else:
        raise TypeError("Wrong data types!")