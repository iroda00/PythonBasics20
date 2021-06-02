students = ['john', 'mark', 'aziz', 'feruza', 105]
print(students)
print(students[0])
print(students[3])
print(f"Hello, {students[1].title()}! Thank you for coming.")
print(f"Hello, {students[4]}. Thank you for coming")
print(f"Hello, " + str(students[4]) + ". Thank you for coming")

cars = ['toyota', 'honda', 'bmw', 'subaru']
print(f"I like my {cars[2]}")
print(f"Tomorrow I want do drive my {cars[3]}")
print(f"Hello Mark! Would you like to drive {cars[1]} or {cars[2]} or {cars[3]}.")
print(f"Hello, {students[2].title()}. Thank you for coming.")
### MODIFY list

cars = ['toyota', 'honda', 'bmw', 'subaru']
print(f"Before: {cars}")
cars[2] = 'tesla'
print(f"After: {cars}")

### ADDING elements
# APPEND

cars.append('lexus')   # this will add to the end of the list
print(cars)

# INSERT
# inserting to specific index or location, not replacing
cars.insert(2, 'nissan')

cars[3] = 'mercedes'    # this will replace

#REMOVE from the list
#delete by index
print(cars)
del cars[4]
print(cars)

#deleting by value
cars.remove('nissan')
print(cars)

cars.pop()  #by default removes last value, 
words = ['hello', 'students']
for word in words:
    word.upper()
    print(word.upper())