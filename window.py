# coding=utf-8
from PyQt4 import QtGui
from PyQt4 import Qt
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QGraphicsScene
from PyQt4.QtGui import QGraphicsView
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QSpinBox
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QSlider
from PyQt4.QtGui import QPen
from PyQt4.QtGui import QColor

class Window( QWidget ):
	def __init__(self):
		QWidget.__init__(self)
		self.scene = QGraphicsScene()

		self.main_layout = QGridLayout()

		self.steps_spin = QSpinBox()
		self.steps_spin.setRange(1,12)
		self.steps_label = QLabel("steps:")
		self.steps_slider = QSlider(1) #horizontal
		self.steps_slider.setRange(1,12)

		self.smooth_spin = QSpinBox()
		self.smooth_spin.setRange(1,12)
		self.smooth_label = QLabel("smoothness:")
		self.smooth_slider = QSlider(1) #horizontal
		self.smooth_slider.setRange(0,100)
		self.smooth_slider.setSingleStep(1)

		self.update_button = QPushButton("update")

		self.view = QGraphicsView()

		self.main_layout.addWidget(
			self.steps_spin,
			0,
			0)
		self.main_layout.addWidget(
			self.steps_label,
			0,
			1)
		self.main_layout.addWidget(
			self.steps_slider,
			0,
			2)
		self.main_layout.addWidget(
			self.smooth_spin,
			1,
			0)
		self.main_layout.addWidget(
			self.smooth_label,
			1,
			1)
		self.main_layout.addWidget(
			self.smooth_slider,
			1,
			2)
		self.main_layout.addWidget(
			self.update_button,
			3,
			0,
			1,
			3)
		self.main_layout.addWidget(
			self.view,
			4,
			0,
			1, #rowSpan
			3) #columnSpan

		self.setLayout(
			self.main_layout)

		#scene.addRect(0,0,50,50,QPen(QColor("red")))
		self.view.setScene(self.scene)

	def setLines(self, lines):
		self.scene.clear()
		for line in lines:
			self.scene.addLine(line)
		self.repaint()