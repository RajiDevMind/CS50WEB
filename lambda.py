people   =  [
    {"name": "yola",  "house": "bungalow"},
    {"name": "yuslov",  "house": "forklifts"},
    {"name": "adam",  "house": "storeybuilding"}
]
# sort  people by the return statement of func 'name'
# def f(person):
#     return person['name']

# here, lambda is a function, a shorter version of f
people.sort(key=lambda person: person['name'])

print(people)