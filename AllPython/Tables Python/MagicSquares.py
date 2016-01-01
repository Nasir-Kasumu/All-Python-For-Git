from sys import exit


def main():
    square_list = []


    print("Enter 16 values: ")
    for i in range(16):
        inputN = int(input())
        square_list.append(inputN)


    for i in range(1, 17):
        found = False
        for j in range(len(square_list)):
            if found == False:
                if square_list[j] == i:
                    found = True

        if found == False:
            print(i, "not in the matrix")


    magicSquare = [[0 for x in range(4)] for x in range(4) ]


    for i in range(4):
        for j in range(4):
            magicSquare[i][j] = square_list[i * 4 + j]

    sumMatrix = 0


    for i in range(4):
        total = 0
        for j in range(4):
            total += magicSquare[i][j]

        if i == 0:
            sumMatrix = total

        elif sumMatrix != total:
            exit("Not a magic square")


    for i in range(4):
        total = 0
        for j in range(4):
            total += magicSquare[j][i]

        if sumMatrix != 0:
            exit("Not a magic square")


    total = 0
    for i in range(4):
        total += magicSquare[i][i]

    if sumMatrix != total:
        exit("Not a magic square")


    total = 0
    for i in range(4):
        total += magicSquare[i][4 - 1 - i]

    if sumMatrix != total:
        exit("Not a magic square")

 
    print("It's a magic square")


main()
