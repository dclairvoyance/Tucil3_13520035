# File: inputfile.py
# Description: InputFile class, containing handler for text file
# Credits: Damianus Clairvoyance DP (13520035)

class InputFile:
    # default constructor
    def __init__(self):
        pass

    # read puzzle from text file
    def readTextFile(self, fileName):
        textFile = open(fileName, "r")
        arrayLine = []
        arrayNumber = []
        for line in textFile:
            numbersInLine = line.strip("\n").split(" ")
            arrayLine.append(numbersInLine)
        textFile.close()
        for i in range (4):
            for j in range (4):
                if (arrayLine[i][j] == "X"):
                    arrayNumber.append(16)
                else:
                    arrayNumber.append(int(arrayLine[i][j]))
        return arrayNumber

    # destructor
    # not implemented, used garbage collection