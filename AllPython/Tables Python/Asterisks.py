def inputs(list):
    print("Enter positive numbers(q to quit): ")

    inputquit = ""

    while inputquit != "q":
        try:
            inputquit = int(input())
            list.append(inputquit)
        except ValueError:
            break

        return list

def displayCharts(list):
    biggestelement = max(list)

    for i in range(len(list)):
            if list[i] < 0:
                list[i] *= -1

            time = int((list[i] / biggestelement) * 40)
            print("*" * time)

def main():
    inputlist = []
    inputlist = inputs(inputlist)
    print("List", inputlist)

    displayCharts(inputlist)

main()
            
