#!/usr/bin/python3
import sys, os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QLineF, QPointF
from squiggly import Squiggly
import random

def main():
	if len(sys.argv) > 1:
		steps = int(sys.argv[1])
	else:
		steps = 4

	lines = squiggle(QLineF(0.0,0.0,400.0,400.0),steps)
	print(lines)
	app = QApplication(sys.argv)
	squiggly = Squiggly(lines)
	squiggly.show()

	sys.exit(app.exec_())

def squiggle(line, steps):
	if steps <= 0:
		return [line]
	mid = (line.p1() + line.p2()) * 0.5
	diff = (line.p2() - line.p1())
	norm = QPointF(-diff.y(), diff.x())
	mid += norm * (random.random() - 0.5) * 0.7
	#norm = norm / math.sqrt(norm.x() ** 2 + norm.y() ** 2)
	return squiggle(
		QLineF(line.p1(), mid), steps - 1
		) + squiggle(
		QLineF(mid, line.p2()), steps - 1)

if __name__ == "__main__":
	main()
