#!/usr/bin/python3
import sys, os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QLineF, QPointF
from window import Window
import random, math

class Squiggly:
	def __init__(self):
		self.app = QApplication(sys.argv)

		self.win = Window()
		self.starting_line = QLineF(0,0,400.0,0)

		self.steps = 4
		self.smooth = 50
		self.dampen = 100

		self.steps_update(self.steps)
		self.smooth_update(self.smooth)
		self.dampen_update(self.dampen)

		self.win.steps_spin.valueChanged.connect(self.steps_update)
		self.win.steps_slider.valueChanged.connect(self.steps_update)
		self.win.smooth_spin.valueChanged.connect(self.smooth_update)
		self.win.smooth_slider.valueChanged.connect(self.smooth_update)
		self.win.dampen_spin.valueChanged.connect(self.dampen_update)
		self.win.dampen_slider.valueChanged.connect(self.dampen_update)
		self.win.update_button.clicked.connect(self.draw_lines)

		self.win.show()

		sys.exit(self.app.exec_())

	def steps_update(self, value):
		self.steps = value
		self.win.steps_spin.setValue(value)
		self.win.steps_slider.setValue(value)
		self.draw_lines()

	def smooth_update(self, value):
		self.smooth = value/100.0
		self.win.smooth_spin.setValue(value)
		self.win.smooth_slider.setValue(value)
		self.draw_lines()

	def dampen_update(self, value):
		self.dampen = value/100.0
		self.win.dampen_spin.setValue(value)
		self.win.dampen_slider.setValue(value)
		self.draw_lines()

	def draw_lines(self):
		lines = self.generate_lines(
			self.starting_line,
			self.steps,
			self.smooth)
		self.win.setLines(lines)

	def generate_lines(self, line, steps = 4, smooth = 0.7):
		if steps <= 0:
			return [line]
		mid = (line.p1() + line.p2()) * 0.5
		diff = (line.p2() - line.p1())
		norm = QPointF(-diff.y(), diff.x())
		mid += norm * (random.random() - 0.5) * smooth
		return self.generate_lines(
			QLineF(line.p1(), mid), steps - 1, smooth * self.dampen
			) + self.generate_lines(
			QLineF(mid, line.p2()), steps - 1, smooth * self.dampen)
	
def main():
	Squiggly()

if __name__ == "__main__":
	main()
