# File: puzzle.py
# Description: Puzzle class, containing puzzle matrix and index of empty cell
# Credits: Damianus Clairvoyance DP (13520035)

import random

class Puzzle:
    # default constructor
    def __init__(self):
        numbers = list(range(1, 17))
        random.shuffle(numbers)
        self.matrix = numbers
        self.emptyCell = self.findEmptyCell()

    # find a solveable puzzle
    def findSolvable(self):
        numbers = list(range(1, 17))
        while (not self.isSolveable()):
            random.shuffle(numbers)
            self.matrix = numbers
            self.emptyCell = self.findEmptyCell()

    # user-defined constructor
    def insertPuzzle(self, inputMatrix):
        for i in range (4):
            for j in range (4):
                self.matrix[i*4+j] = inputMatrix[i*4+j]
        self.emptyCell = self.findEmptyCell()

    # find index of empty cell
    def findEmptyCell(self):
        index = 0
        while (self.matrix[index] != 16):
            index += 1
        return index
    
    # convert index of empty cell to (row, col)
    def convertEmptyCell(self):
        return (self.emptyCell // 4, self.emptyCell % 4)

    # check if puzzle is valid (unique combinations of number 1-16)
    def isValid(self):
        found = set()
        for number in self.matrix:
            if (number in found or number > 16 or number < 1):
                return False
            else:
                found.add(number)
        return True

    # count solveable factor
    # (S(Kurang(i)) + X in lecture notes)
    def solveableFactor(self):
        counter = 0
        for index in range (1, 17):
            counter += self.countOff(index)
        return counter + self.shadedX()

    # check if puzzle is solvable (S(countOff(i)) + shadedX is even)
    def isSolveable(self):
        return (self.solveableFactor() % 2 == 0)
    
    # count number of numbers placed in their respective cell
    def countCorrectPosition(self):
        counter = 0
        for index in range (16):
            if (self.matrix[index] == index + 1 and self.matrix[index] != 16):
                counter += 1
        return counter

    # check if puzzle is solved
    def isSolved(self):
        return (self.countCorrectPosition() == 15)
    
    # find index of a number
    def findIndex(self, i):
        index = 0
        while (index < 16 and self.matrix[index] != i):
            index += 1
        return index + 1
    
    # count number of off placed cells 
    # (Kurang(i) function in lecture notes)
    def countOff(self, i):
        indexI = self.findIndex(i)
        counter = 0
        for index in range (indexI, 16):
            if (self.matrix[index] < i):
                counter += 1
        return counter
    
    # print countOff (Kurang(i) in lecture notes) for all index
    def printOff(self):
        for index in range (16):
            print("Kurang({0:2d}) = ".format(index + 1), end = "")
            print(self.countOff(index+1))
        print()

    # find shaded X parameter 
    # (X function in lecture notes)
    def shadedX(self):
        i, j = self.convertEmptyCell()
        return ((i + j) % 2 == 1)
    
    # check if move is valid (tile movable)
    def isMoveValid(self, command):
        i, j = self.convertEmptyCell()
        return (
            (command == "up" and i != 0) or
            (command == "right" and j != 3) or
            (command == "down" and i != 3) or
            (command == "left" and j != 0)
        )
    
    # switch number of a cell and empty cell
    def switchCell(self, cell, emptyCell):
        self.matrix[emptyCell] = self.matrix[cell]
        self.matrix[cell] = 16
        self.emptyCell = cell

    # move cell based on command
    def move(self, command):
        newPuzzle = Puzzle()
        newPuzzle.insertPuzzle(self.matrix)
        x = self.emptyCell
        if (command == "up"):
            newPuzzle.switchCell(x-4, x)
        elif (command == "right"):
            newPuzzle.switchCell(x+1, x)
        elif (command == "down"):
            newPuzzle.switchCell(x+4, x)
        elif (command == "left"):
            newPuzzle.switchCell(x-1, x)
        return newPuzzle
    
    # print puzzle
    def print(self):
        for i in range (4):
            print("---------------------")
            for j in range (4):
                if (self.matrix[i*4+j] == 16):
                    print("|    ", end = "")
                else:
                    print("|", end = "")
                    print(" {0:2d} ".format(self.matrix[i*4+j]), end = "")
            print("|")
        print("---------------------")
        print()
    
    # destructor
    # not implemented, used garbage collection