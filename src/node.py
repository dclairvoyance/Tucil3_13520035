# File: node.py
# Description: Node class, containing id, puzzle, path from root, cost, and last move
# Credits: Damianus Clairvoyance DP (13520035)

import itertools

class Node:
    # initialize iterator for id
    id_iterator = itertools.count()

    # user-defined constructor
    def __init__(self, puzzle, arrayPath, lastMove):
        self.id = next(self.id_iterator)
        self.puzzle = puzzle
        self.path = []
        for index in range (len(arrayPath)):
            self.path.append(arrayPath[index])
        self.cost = self.countUpperCost() + self.countLowerCost()
        self.lastMove = lastMove

    # copy constructor
    def insertNode(self, inputNode):
        self.id = inputNode.id
        self.puzzle.insertPuzzle(inputNode.puzzle.matrix)
        self.path = inputNode.path
        self.cost = inputNode.cost
        self.lastMove = inputNode.lastMove
    
    # get path of node
    def getPath(self):
        return self.path

    # count number of moves from root to node
    # (f(P) in lecture notes)
    def countUpperCost(self):
        return len(self.path)
    
    # count number of numbers placed not in their respective cell 
    # (g(P) in lecture notes)
    def countLowerCost(self):
        return (15-self.puzzle.countCorrectPosition())
    
    # returns true if next move is opposite of last move,
    # preventing infinite loop
    def isOpposite(self, command):
        return (
            (command == "up" and self.lastMove == "down") or
            (command == "right" and self.lastMove == "left") or
            (command == "down" and self.lastMove == "up") or
            (command == "left" and self.lastMove == "right")
        )

    # destructor
    # not implemented, used garbage collection