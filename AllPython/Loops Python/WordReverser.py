#P4.9
Word = str(input("Enter a word "))

for i in range(len(Word) - 1, -1, -1):
    print(Word[i], end = "")
