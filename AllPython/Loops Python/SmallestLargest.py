#P4.2.a 
from sys import exit

numbers = []
end = False
while not end:
        input = str(input("enter a number:(end to end):"))
        if input == "end":
        end = True

        else:
                if input.isdigit():
                    input = int(input)
                    numbers.append(input)

if not numbers:
    exit("List is empty")
print("Largest:", max(numbers))
print("Smallest:", min(numbers))
    

