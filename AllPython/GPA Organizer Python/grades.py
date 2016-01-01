

inputfile = input("open grades.txt")
outputfile = input("write to some different file")

infile = open(inputfile, "r")
outfile = open(outputfile,"w")

line = infile.readline
for line in infile:
    line.split(":")


inputfile.close()
outpufile.close()
