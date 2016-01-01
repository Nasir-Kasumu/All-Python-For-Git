def main():
        uniqueword = set()
        inputfile = input("what is the name of your file")
        outputfile = input("what is the output file?")

        inputfilename = open(inputfile,"r")
        outputfilename = open(outputfile, "w")

        line = inputfilename.readline()
        for line in inputfilename:
                words = line.split()
                for word in words:
                        newword = new(word)
                        if newword != "":
                                uniqueword.add(newword)
                
                wordcount = len(uniqueword)
                print("the new words are", wordcount)



        inputfilename.close()
        outputfilename.close()
main()
