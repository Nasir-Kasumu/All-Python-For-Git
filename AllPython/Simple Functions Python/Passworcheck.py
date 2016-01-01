
def passwordcheck(password):
    eightcharacters = False
    Uppercase = False
    Lowercase = False
    Digits = False

    
    if len(password) >= 8:
        eightcharacters = true


            
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits ="0123456789"

    for i in range(len(password)):
        if password[i] in lowercase and Lowercase != True:
            Lowercase = True

        elif password[i] in uppercase and Uppercase != True:
            hasUpper = True

        elif password [i] in digits and Digits != True:
            Digits = True

        if eightcharacters == True and Digits == True and Uppercase == True and Lowercase == True:
            return True

        else:
            return False
def main():
            inputPassword = str(input("Enter your password please :D"))
            inputPasswordtwo = str(input("Enter your password please :D"))

            if passwordcheck(inputPassword) == True:
                print("good password")
            else:
                print("bad password")


main()
     
