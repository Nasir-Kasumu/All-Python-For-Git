def SecondLargest(list):
    list = [1,2,3,4,5,6,7,8,9,10]
    largest = max(list)

    while largest in list:
        list.remove(largest)
    return max(list)



def main():
    list = [1,2,3,4,5,6,7,8,9,10]
print("second largets in the list is")
print(SecondLargest(list))

main()
