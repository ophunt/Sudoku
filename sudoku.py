#!/anaconda2/envs/sudoku/bin/python python

import random

boxChars = {
	"topLeft": "\u250C",
	"topRight": "\u2510",
	"botLeft": "\u2514",
	"botRight": "\u2518",
	"topTee": "\u252C",
	"botTee": "\u2534",
	"leftTee": "\u251C",
	"rightTee": "\u2524",
	"plus": "\u253c",
	"vert": "\u2502",
	"hori": 5*"\u2500"
}

boxLines = {
	"topLine": boxChars["topLeft"] \
		+ 2*(boxChars["hori"] + boxChars["topTee"]) \
		+ boxChars["hori"] + boxChars["topRight"] + "\n",
	"midLine": boxChars["leftTee"] \
		+ 2*(boxChars["hori"] + boxChars["plus"]) \
		+ boxChars["hori"] + boxChars["rightTee"] + "\n",
	"botLine": boxChars["botLeft"] \
		+ 2*(boxChars["hori"] + boxChars["botTee"]) \
		+ boxChars["hori"] + boxChars["botRight"] + "\n",
}

class Cell:

	currentValue = 0
	possibleValues = list(range(1, 10))

	def __init__(self, correctValue):
		self.correctValue = correctValue

	def isCorrect(self):
		return self.currentValue == self.correctValue

	def __str__(self):
		return str(self.correctValue) #if self.currentValue != 0 else " "

class Board:

	data = [[Cell(0) for i in range(9)] for j in range(9)]

	def __init__(self):
		# Seed board with first 1-9
		for i in range(1, 10):
			row, col = random.randint(0,8), random.randint(0,8)
			self.data[row][col].correctValue = i


	def __str__(self):
		s = ""
		for row in range(13):
			if row == 0:
				s += boxLines["topLine"]
			elif row == 12:
				s += boxLines["botLine"]
			elif row == 4 or row == 8:
				s += boxLines["midLine"]
			else:
				for col in range(19):
					if col % 6 == 0:
						s += boxChars["vert"]
					elif col % 2 == 1:
						s += str(self.data[row-1-row//4][col//2])
					else:
						s += " "
				s += "\n"
		return s

	def change(self, row, col, newVal):
		self.data[row][col].currentValue = newVal

class Game:

	board = Board()

if __name__ == "__main__":
	board = Board()

	print(board)
