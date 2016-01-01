#P4.12 
Word = str(input("Enter a word"))

WordLen = len(Word)
smallLen = 1
begin = 0

for i in range(smallLen):
    start = 0
    while begin + smallLen <= wordLen:
        print(word[begin:begin+smallLen])
        begin = begin + 1
    smallLen = smallLen + 1
