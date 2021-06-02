## Fuzz-Buzz problem
# accept a number from th user  - input(), int().
# if that number is dividable by 3 print ('Fuzz')
# if that number is dividable by 5 print ('Buzz')
#if that number is dividable by 3 and 5 print ('ZuzzBuzz')
# if number % 3 is 0 - its mean its dividable by 3
# if number % 5 is 0 - its means its dividable by 5

for i in range(3):
    num = int(input("Enter your number:"))
    if  num % 3 == 0 and num % 5 == 0:
        print('FuzzBuzz')
    elif num % 3 == 0:
        print('Fuzz')
    elif num % 5 == 0:
        print('Buzz')



