people = [
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Draco", "house":"Slytherin"},
    {"name":"Cho", "house":"Ravenclaw"},
]

# Error
# people.sort()
# print(people)

# Method 1
print("Classic: ")

def f(person):
    return person["name"]

people.sort(key=f)
print(people)

# Method 2 lambda function (Used to write simple 1 line function)
print("Lambda: ")
people.sort(key=lambda person: person["name"])
print(people)
