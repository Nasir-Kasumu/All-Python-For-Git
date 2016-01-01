#P4.15 
input = int(input("What is your number?"))

firstfold = 0
secondfold = 0
newfold = 1

while newfold <= input:
    print(newfold)
    secondfold = firstfold
    firstfold = newfold
    newfold = secondfold + firstfold
