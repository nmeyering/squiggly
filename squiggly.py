import sys, os
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QGraphicsScene, QGraphicsPolygonItem, QPolygonF, QBrush, QColor, QPixmap
from PyQt4.QtCore import QLineF, QPointF, QRectF
from window import Window
from grid import Grid
from path import Path
from subregion import SubRegion
import random, math

class Squiggly:
	def __init__(self, dim = QRectF(0,0,800,600)):
		self.app = QApplication(sys.argv)

		self.dim = dim

		self.win = Window()
		self.scene = QGraphicsScene(dim)
		self.win.view.setScene(self.scene)

		self.grid = Grid(size = 16, bounds = dim)

		self.scene.addItem(self.grid)

		mypoly = SubRegion(dim = QRectF(-200,-200,200,200))
		mypoly.setBrush(QBrush(QPixmap("asphalt256.png")))
		mypoly.translate(200,200)
		self.scene.addItem(mypoly)

		mypoly2 = SubRegion(dim = QRectF(-200,-200,200,200))
		mypoly2.setBrush(QBrush(QPixmap("asphalt256.png")))
		mypoly2.translate(600,400)
		self.scene.addItem(mypoly2)

		mypoly3 = SubRegion(dim = QRectF(-100,-100,100,100))
		mypoly3.setBrush(QBrush(QColor("green")))
		mypoly3.translate(350,400)
		self.scene.addItem(mypoly3)

		self.link(mypoly, mypoly3)
		self.link(mypoly3, mypoly2)
		#self.path = Path(mypoly.connectors[1] + mypoly.mapToScene(mypoly.pos()),
		#	mypoly2.connectors[0] + mypoly2.mapToScene(mypoly2.pos()))
		self.path = Path(mypoly2.connectors[1] + mypoly2.mapToScene(mypoly2.pos()),
			QPointF(800,300))
		self.path_out = Path(QPointF(0,300),
			mypoly.connectors[0] + mypoly.mapToScene(mypoly.pos()))

		self.scene.addItem(self.path)
		self.scene.addItem(self.path_out)

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

	def link(self, a, b):
		self.scene.addItem(Path(a.exit() + a.mapToScene(a.pos()),
			b.entrance() + b.mapToScene(b.pos())))

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
