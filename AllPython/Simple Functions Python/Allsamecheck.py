
def allTheSame(x,y,z):
    if x == y and y == z:
        print("true")
    else:
        print("false")
def main():
    
    x = int(input("what is the x number"))
    y = int(input("what is the y number"))
    z = int(input("what is the z number"))
    print(allTheSame(x, y, z))


main()
