#Coltz series in python
def colltz(number):
    if number % 2 == 0: # It is even number
        return number // 2
    elif number % 2 == 1: # It is odd number
        return number * 3 + 1
    else:
        print('Something went wrong')
print('Enter the number: ')
number = int(input())
print(f"The colltz series for the {number} is,")
print(number)
while number !=1:
    number = colltz(number)
    print(number)
