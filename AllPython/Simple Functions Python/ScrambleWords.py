from random import randint


def scramble(word):
    result = word[0]

    if len(word) > 1:
        for i in range(len(word) - 2, 0, -1):
            result += word[i]

        result += word[len(word) - 1]

    return result


def main():
    print("I don't give a damn for a man that can only spell a word one way.")
    print("Scrambled....")
    print(scramble("I"), scramble("don't"), scramble("give"), scramble("a"), scramble("damn"), scramble("for"),
          scramble("a"), scramble("man"), scramble("that"), scramble("can"), scramble("only"), scramble("spell"),
          scramble("a"), scramble("word"), scramble("one"), scramble("way"))



main()
