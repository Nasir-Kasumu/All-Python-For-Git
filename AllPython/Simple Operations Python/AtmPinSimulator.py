import sys
PIN = "1234"
count = 0
ATM = "1234"
while count != 3 or PIN != 1234:
    PIN = input("What is your pin number?")
    if PIN == ATM:
            print("correct pin number")
    elif PIN != ATM and  count == 3:
            print("exceeded number of tries account locked")
    count = count + 1:
    

