## if conditions
cars = ['lexus', 'bugatti', 'bmw', 'ferrari']
for car in cars:
     if car == 'bmw':
         print(car.upper())
     else:
         print(car.title())

##if expression:
##    code to execute when expression is True
##elif expression2:
##    code to execute when expression2 is True
##else:
##    code to execute for all others

is_bmw_listed = ('bmw' in cars)
print(is_bmw_listed)
print('bmw' in cars)

if 'bmw5' not in cars:
    cars.append('bmw5')
print(cars)

if 'toyota' not in cars:
    cars.append('toyota')
print(cars)


age = int('25')
states_17 = ['NY', 'CA', ]
for i in range(3):
    age = int(input("Enter your age:"))
    state = input("Enter your state:")
    if age >=16 and state == 'NJ':
            print('You are eligible to apply for DL.')
            print('Available cars in NJ')
            for car in cars[:2]:
                print(f"\t{car}")

    elif age >=17 and state == 'NY':
        print(f"You are eligible for DL")
        print('Available cars in NY')
        for car in cars[2:]:
            print(f"\t{car}")
    else:
        print(f"You are not eligible for DL")

    ###    diff = 17 - age
###    print(f"You will be elifible in {diff} years.")
  ###  print(f"You are not eligible for DL")

