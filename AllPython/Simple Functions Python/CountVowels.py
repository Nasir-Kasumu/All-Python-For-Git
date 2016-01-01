def countVowels(string):
	countVowels = 0
	vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

	for i in range(len(string)):
		if string[i] in vowels:
			countVowels += 1

	return countVowels

def main():
	string = str(input("Enter a word"))

	print("number of vowels are", countVowels(string))


main()
