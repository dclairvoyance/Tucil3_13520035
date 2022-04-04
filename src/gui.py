# File: gui.py
# Description: Game class, containing all functions and scriptings for GUI
# Credits: Damianus Clairvoyance DP (13520035)

import tkinter as tk
import configurations
from puzzle import *

class Game(tk.Frame):
    # default constructor (and main program for GUI)
    def __init__(self, arrayPuzzle, arrayPath):
        # initial scriptings
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("15 Puzzle Solver")
        self.master.resizable(False, False)

        # initial functions
        self.puzzle = Puzzle()
        self.puzzle.insertPuzzle(arrayPuzzle)
        arrayPath.insert(0, "none")
        arrayPath.append("none")
        self.path = arrayPath
        self.index = 1
        self.ongoing = "stop"

        # scripting: initialize puzzle board
        self.mainGrid = tk.Frame(
            self,
            bg = configurations.GRID_COLOR,
            bd = 3,
            width = 600,
            height = 600
        )
        # scripting: add spaces above and below puzzle board
        self.mainGrid.grid(pady = (100, 90))

        # put GUI window at the middle of the screen
        windowWidth = 445
        windowHeight = 640
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        x = int((screenWidth/2) - (windowWidth/2))
        y = int((screenHeight/2) - (windowHeight/2))
        self.master.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

        self.createGUI()
        self.startGame()

        # add functionalities with keyboard arrow
        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        self.mainloop()

    # initialize all GUI components
    def createGUI(self):
        # scripting: initialize cells in puzzle board
        self.cells = []
        for i in range (4):
            for j in range (4):
                cell_frame = tk.Frame(
                    self.mainGrid,
                    bg = configurations.EMPTY_CELL_COLOR,
                    width = 100,
                    height = 100
                )
                cell_frame.grid(row = i, column = j, padx = 5, pady = 5)

                cell_number = tk.Label(
                    self.mainGrid, 
                    bg = configurations.EMPTY_CELL_COLOR
                )
                cell_number.grid(row = i, column = j)

                cell_data = {"frame": cell_frame, "number": cell_number}
                self.cells.append(cell_data)
        
        # scripting: initialize title frame (above puzzle board)
        titleFrame = tk.Frame(self)
        titleFrame.place(relx = 0.5, y = 45, anchor = "center")

        self.gameTitle = tk.Label(
            titleFrame,
            text = "15 Puzzle Solver",
            font = configurations.TITLE_FONT
        )
        self.gameTitle.grid(row = 0)

        self.creditTitle = tk.Label(
            titleFrame, 
            text = "Damianus Clairvoyance DP (13520035)", 
            font = configurations.CREDIT_FONT,
        )
        self.creditTitle.grid(row = 1)

        # scripting: initialize move frame (below puzzle board)
        moveFrame = tk.Frame(self)
        moveFrame.place(relx = 0.5, y = 590, anchor = "center")

        self.lastMoveTitle = tk.Label(
            moveFrame,
            text = "Last Move",
            font = configurations.MOVE_TITLE_FONT
        )
        self.lastMoveTitle.grid(row = 0, column = 0, padx = 20)

        self.nextMoveTitle = tk.Label(
            moveFrame,
            text = "Next Move",
            font = configurations.MOVE_TITLE_FONT
        )
        self.nextMoveTitle.grid(row = 0, column = 1, padx = 20)

        self.lastMove = tk.Label(
            moveFrame,
            text = self.path[self.index-1],
            font = configurations.MOVE_FONT
        )
        self.lastMove.grid(row = 1, column = 0, padx = 20)

        self.nextMove= tk.Label(
            moveFrame,
            text = self.path[self.index],
            font = configurations.MOVE_FONT
        )
        self.nextMove.grid(row = 1, column = 1, padx = 20)

        self.autoTitle = tk.Label(
            moveFrame,
            text = "Auto Move",
            font = configurations.MOVE_TITLE_FONT
        )
        self.autoTitle.grid(row = 0, column = 2, padx = 20)

        self.autoDirection = tk.Label(
            moveFrame,
            text = "stop",
            font = configurations.MOVE_FONT
        )
        self.autoDirection.grid(row = 1, column = 2, padx = 20)

    # scripting: intialize cells of puzzle board
    def startGame(self):
        for index in range (16):
            if (self.puzzle.matrix[index] != 16):
                self.cells[index]["frame"].configure(bg = configurations.CELL_COLOR)
                self.cells[index]["number"].configure(
                    bg = configurations.CELL_COLOR,
                    fg = configurations.CELL_NUMBER_COLOR,
                    font = configurations.CELL_NUMBER_FONT,
                    text = str(self.puzzle.matrix[index])
                )
    
    # switch two adjacent cells of puzzle board
    def switchCell(self, cell, emptyCell):
        self.puzzle.matrix[emptyCell] = self.puzzle.matrix[cell]
        self.puzzle.matrix[cell] = 16
        self.emptyCell = cell
        self.cells[emptyCell]["frame"].configure(bg = configurations.CELL_COLOR)
        self.cells[emptyCell]["number"].configure(
            bg = configurations.CELL_COLOR,
            fg = configurations.CELL_NUMBER_COLOR,
            font = configurations.CELL_NUMBER_FONT,
            text = str(self.puzzle.matrix[emptyCell])
        )
        self.cells[cell]["frame"].configure(bg = configurations.EMPTY_CELL_COLOR)
        self.cells[cell]["number"].configure(
            bg = configurations.EMPTY_CELL_COLOR,
            text = ""
        )

    # update GUI to next move
    def updateGUIRight(self, command):
        x = 0
        for index in range (16):
            if (self.puzzle.matrix[index] == 16):
                x = index
        if (command == "up"):
            self.switchCell(x-4, x)
        elif (command == "right"):
            self.switchCell(x+1, x)
        elif (command == "down"):
            self.switchCell(x+4, x)
        elif (command == "left"):
            self.switchCell(x-1, x)
        self.lastMove.configure(
            text = self.path[self.index]
        )
        self.nextMove.configure(
            text = self.path[self.index+1]
        )
        self.update_idletasks()
    
    # update GUI to last move
    def updateGUILeft(self, command):
        x = 0
        for index in range (16):
            if (self.puzzle.matrix[index] == 16):
                x = index
        if (command == "up"):
            self.switchCell(x+4, x)
        elif (command == "right"):
            self.switchCell(x-1, x)
        elif (command == "down"):
            self.switchCell(x-4, x)
        elif (command == "left"):
            self.switchCell(x+1, x)
        self.lastMove.configure(
            text = self.path[self.index-1]
        )
        self.nextMove.configure(
            text = self.path[self.index]
        )
        self.update_idletasks()
    
    # update GUI when puzzle hit initial or solved position
    def updateGUI(self):
        self.autoDirection.configure(
            text = self.ongoing
        )
    
    # update GUI when left arrow is pushed
    def left(self, event):
        if (self.index-1 >= 1 and self.index-1 < (len(self.path) - 1)):
            self.index -= 1
            self.updateGUILeft(self.path[self.index])
            self.updateGUI()
    
    # update GUI when right arrow is pushed
    def right(self, event):
        if (self.index >= 1 and self.index < (len(self.path) - 1)):
            self.updateGUIRight(self.path[self.index])
            self.updateGUI()
            self.index += 1
    
    # switch auto move in the direction of last move
    def switchOngoingLeft(self):
        if (self.ongoing == "right"):
            self.ongoing = "stop"
        elif (self.ongoing == "stop"):
            self.ongoing = "left"
    
    # switch auto move in the direction of next move
    def switchOngoingRight(self):
        if (self.ongoing == "left"):
            self.ongoing = "stop"
        elif (self.ongoing == "stop"):
            self.ongoing = "right"

    # functions for auto move left
    def repeatLeft(self):
        if (self.index == 1):
            self.ongoing = "stop"
            self.updateGUI()
        elif (self.index-1 >= 1 and self.index-1 < (len(self.path) - 1) and self.ongoing == "left"):
            self.index -= 1
            self.updateGUILeft(self.path[self.index])
            self.after(1000, self.repeatLeft)
    
    # functions for auto move right
    def repeatRight(self):
        if (self.index == (len(self.path) - 1)):
            self.ongoing = "stop"
            self.updateGUI()
        elif (self.index >= 1 and self.index < (len(self.path) - 1) and self.ongoing == "right"):
            self.updateGUIRight(self.path[self.index])
            self.index += 1
            self.after(1000, self.repeatRight)

    # start auto move right when up arrow is pushed
    def up(self, event):
        if (self.ongoing != "right"):
            self.switchOngoingRight()
            self.repeatRight()
            self.updateGUI()
    
    # start auto move left when down arrow is pushed
    def down(self, event):
        if (self.ongoing != "left"):
            self.switchOngoingLeft()
            self.repeatLeft()
            self.updateGUI()