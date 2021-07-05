# Collect the pet names suggetions
catNames = [] #Empty list created
while True:
    print(f"Enter the {str(len(catNames)+1)} pet names.or(press enter for nothing): ")
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
   print(' ' + str(name))