student = {
    'name':'Arpit',
    'age':25,
    'is_married':False,
    'has_job':True,
}

print(student)

# From Python 3.7 dictionary is start to have order.
# dictionary key must be immutable.
# dictionary key must be unique, will not throw error will just lose the old value.


# dictionary methods
# print(student['age'])
# print(student.get('age1',78))

user = dict()
# dict.keys() -> will return list of keys
print(student.keys())
# dict.values() -> will return list of values
# print(student.values())

# dict.items() -> will return the list of tuples
# print(student.items())
# copy() -> will copy one dict into another.
# popitem() -> will remove last entry from dictionary.
# update -> to update a key value in dictionary.