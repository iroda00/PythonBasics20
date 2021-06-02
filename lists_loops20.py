states = ['New York', 'New Jersey', 'Connecticut', 'California', 'Maryland']

# for variable in list_of_elements:
#   repetitive code here

for state in states:
    print(f"Welcome to the {state}!!")
    print("Enjoy your trip!!!")

print(states)

#for state in states:
#   pass   # means to do nothing

# RANGE

for num in range(5):
    print(f"My current number from range(5): {num}")

for num in range(3,6):
    print(f"My curent number from range(3,6): {num}")


friends = list()
students = []
numbers = list(range(5))
print(numbers)

# print squares of numbers from 5 to 12

squares = []
for num in range(5, 13):
    num_sqr = num**2
    squares.append(num_sqr)
    print(num_sqr)
    print(squares)
print(squares)

squares = list()
for num in range(5,13):
    squares.append(num**2)
print(squares)

numbers = [5,78, 127, 230, 6, 5]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers = []

numbers = list(range(1, 1000001))
print(f"Minimum number is: {min(numbers)}")
print(f"Maximum number is: {max(numbers)}")
print(f"Sum of number is: {sum(numbers)}")







