#Find my pet name in Python
myPet = ['stark','black','white','adam','luke']
name = input('Enter the pet name: ')
if name not in myPet:
    print(f"I don't have a pet named {name}")
else:
    print(f"Yes, {name} is my pet")

