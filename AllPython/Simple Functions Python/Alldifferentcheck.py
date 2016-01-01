def allDifferent(x,y,z):
    if x == y or y == z or z == x:
        print("false")
    else:
        print ("true")
def main():
        
    x = int(input("what is the x number"))
    y = int(input("what is the y number"))
    z = int(input("what is the z number"))
    print(allDifferent(x, y, z))


main()
        
