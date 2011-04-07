import sys, os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QGraphicsScene
from PyQt4.QtCore import QLineF, QPointF, QRectF
from window import Window
from grid import Grid
from path import Path
import random, math

class Squiggly:
	def __init__(self, dim = QRectF(0,0,800,600)):
		self.app = QApplication(sys.argv)

		self.dim = dim

		self.win = Window()
		self.scene = QGraphicsScene(dim)
		self.win.view.setScene(self.scene)

		self.path = Path(dim)
		self.grid = Grid(size = 16, bounds = dim)

		self.scene.addItem(self.grid)
		self.scene.addItem(self.path)

		self.win.smooth_slider.setValue(self.path.smooth)
		self.win.dampen_slider.setValue(self.path.dampen)
		self.win.steps_slider.setValue(self.path.steps)
		self.win.smooth_spin.setValue(self.path.smooth)
		self.win.dampen_spin.setValue(self.path.dampen)
		self.win.steps_spin.setValue(self.path.steps)

		self.win.steps_spin.valueChanged.connect(self.steps_slider_update)
		self.win.steps_slider.valueChanged.connect(self.steps_spin_update)
		self.win.smooth_spin.valueChanged.connect(self.smooth_slider_update)
		self.win.smooth_slider.valueChanged.connect(self.smooth_spin_update)
		self.win.dampen_spin.valueChanged.connect(self.dampen_slider_update)
		self.win.dampen_slider.valueChanged.connect(self.dampen_spin_update)

		self.win.update_button.clicked.connect(self.path.update_lines)

		self.win.show()

		sys.exit(self.app.exec_())

	def steps_slider_update(self, value):
		self.path.steps = value
		self.win.steps_slider.setValue(value)
		self.path_update()

	def steps_spin_update(self, value):
		self.path.steps = value
		self.win.steps_spin.setValue(value)
		self.path_update()

	def smooth_slider_update(self, value):
		self.path.smooth = value
		self.win.smooth_slider.setValue(value)
		self.path_update()

	def smooth_spin_update(self, value):
		self.path.smooth = value
		self.win.smooth_spin.setValue(value)
		self.path_update()

	def dampen_slider_update(self, value):
		self.path.dampen = value
		self.win.dampen_slider.setValue(value)
		self.path_update()

	def dampen_spin_update(self, value):
		self.path.dampen = value
		self.win.dampen_spin.setValue(value)
		self.path_update()

	def path_update(self):
		self.path.update_lines()
