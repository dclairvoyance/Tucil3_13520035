# File: app.py
# Description: main program
# Credits: Damianus Clairvoyance DP (13520035)

# import libraries and classes
import time
import os.path
from puzzle import *
from node import *
from livenodequeue import *
from inputfile import *
from gui import *

def welcomeMessage():
    # show welcome message
    print()
    print("==========================")
    print("        Welcome to        ")
    print("     15 Puzzle Solver     ")
    print("==========================")
    print("         Credits:         ")
    print(" Damianus Clairvoyance DP ")
    print("         13520035         ")
    print("==========================")
    print()

def loadSuccessful():
    # show load successful message
    print()
    print("==========================")
    print("Puzzle Loaded Successfully")
    print("==========================")
    print()

def main():
    # main program
    welcomeMessage()

    # initialize puzzle
    puzzle = Puzzle()

    # handle input puzzle source
    print("Input method:")
    print("[1] Computer Generated")
    print("[2] Text File")
    print("[3] Manual")
    inputMethod = int(input("Pick method (1/2/3): "))
    while (inputMethod > 3 or inputMethod < 0):
        print("Invalid!")
        inputMethod = int(input("Pick method (1/2/3): "))

    # computer generated, ensures valid and solvable puzzle
    if (inputMethod == 1):
        puzzle.findSolvable()
    # text file
    elif (inputMethod == 2):
        inputFile = InputFile()

        # input and validate file name
        fileName = input("Type file name: ")
        while (not os.path.isfile(fileName)):
            print("Invalid!")
            fileName = input("Type file name: ")

        # read text file line by line and put into puzzle
        arrayNumber = inputFile.readTextFile(fileName)
        puzzle.insertPuzzle(arrayNumber)

        # abort program if puzzle is invalid
        if (not puzzle.isValid()):
            print("Puzzle is invalid. Exiting.")
            exit()
    # manual
    else: # inputMethod == 3
        print("Insert your puzzle:")
        arrayNumber = []
        # read text file line by line and put into puzzle
        for i in range (4):
            arrayLine = input()
            numbersInLine = arrayLine.strip("\n").split(" ")
            for j in range (4):
                if (numbersInLine[j] == "X"):
                    arrayNumber.append(16)
                else:
                    arrayNumber.append(int(numbersInLine[j]))
        puzzle.insertPuzzle(arrayNumber)

        # abort program if puzzle is invalid
        if (not puzzle.isValid()):
            print("Puzzle is invalid. Exiting.")
            exit()
    
    # show puzzle successfully loaded
    loadSuccessful()
    puzzle.print()

    # print Kurang(i) and Sigma(Kurang(i)) + X
    print("Kurang(i) Function")
    puzzle.printOff()
    print("Sigma(Kurang(i)) + X Function = ", end = "")
    print(puzzle.solveableFactor())
    print()

    # handles puzzle based on puzzle solveability
    if (not puzzle.isSolveable()):
        print("Puzzle is not solveable. Exiting.")
        exit()
    else:
        print("Puzzle is solveable.")
        print()

        # initialize everything
        commands = ["up", "left", "down", "right"] # order matters, but not significantly
        arrayPath = []
        countNode = 0
        queueLiveNode = LiveNodeQueue()

        # initialize puzzle for printing purpose
        printPuzzle = Puzzle()
        printPuzzle.insertPuzzle(puzzle.matrix)

        # start of branch and bound algorithm
        # algorithm is explained further in report (see docs directory)
        startTimer = time.process_time_ns()
        expandNode = Node(puzzle, arrayPath, "")
        newNode = Node(puzzle, arrayPath, "")
        countNode += 1
        queueLiveNode.enqueue(newNode)
        expandNode.insertNode(queueLiveNode.dequeue())

        while (not expandNode.puzzle.isSolved()):
            for command in commands:
                if (expandNode.puzzle.isMoveValid(command) and not expandNode.isOpposite(command)):
                    newPuzzle = expandNode.puzzle.move(command)
                    arrayPath.append(command)
                    newNode = Node(newPuzzle, arrayPath, command)
                    countNode += 1
                    queueLiveNode.enqueue(newNode)
                    arrayPath.pop()
            expandNode.insertNode(queueLiveNode.dequeue())
            arrayPath = expandNode.getPath()

        # end of branch and bound algorithm
        stopTimer = time.process_time_ns()

        # print puzzle from initial to solved position
        print("initial:")
        printPuzzle.print()
        for i in range (len(arrayPath)):
            print(str(arrayPath[i]) + ":")
            printPuzzle = printPuzzle.move(arrayPath[i])
            printPuzzle.print()
        
        # print additional informations
        print(countNode - 1, "nodes generated")
        print((stopTimer-startTimer)/1000000, "ms taken")

    return arrayNumber, arrayPath

if __name__ == "__main__":
    # run CLI program
    arrayNumber, arrayPath = main()

    # run GUI program
    Game(arrayNumber, arrayPath)