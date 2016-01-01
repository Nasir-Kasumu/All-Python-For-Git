I = input("what is your income?")
Income = int(I)
if Income >= 500000:
           Tax = Income * .06
elif 499999 >= Income >= 250000:
            Tax = Income * .05
elif 249999 >= Income >=100000:
    Tax = Income * .04
elif 99999 >= Income >= 75000:
    Tax = Income * .03
elif 74999 >= Income >= 50000:
    Tax = Income * .02
else:
  Tax = Income * .01

print("Your income tax is")
print(Tax)
