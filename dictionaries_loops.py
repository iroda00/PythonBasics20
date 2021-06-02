student1 = {'name': 'Ali', 'gpa': 3.8}
student2 = {'name': 'Alexa', 'gpa': 3.9}

for info in student1:
    print(info)

for info in student1.keys():
    print('key is :', info)
print(" #looping with keys")
for key in student1:
    print('key is :', key)
print()
for key in sorted(student1.keys()):
    print('key is:', key)
print()
print("# looping the values")
for key in student1:
    print('value is :', student1[key])

for value in student1.values():
    print('value is:', value)
print()


print("# loping the keys and values")
for dkey, dvalue in student1.items():
    print('key is', dkey)
    print('value is , ', dvalue)

print("Nesting dictionaries")
class_2020 = [student1, student2]
print(class_2020)
for student in class_2020:
    print("Name of the student: ", student['name'])

