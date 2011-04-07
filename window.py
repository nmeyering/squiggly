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

		self.main_layout = QGridLayout()

		self.steps_spin = QSpinBox()
		self.steps_spin.setRange(1,12)
		self.steps_label = QLabel("steps:")
		self.steps_slider = QSlider(1) #horizontal
		self.steps_slider.setRange(1,12)

		self.smooth_spin = QSpinBox()
		self.smooth_spin.setRange(1,100)
		self.smooth_label = QLabel("smoothness:")
		self.smooth_slider = QSlider(1) #horizontal
		self.smooth_slider.setRange(0,100)
		self.smooth_slider.setSingleStep(1)

		self.dampen_spin = QSpinBox()
		self.dampen_spin.setRange(1,100)
		self.dampen_label = QLabel("dampening:")
		self.dampen_slider = QSlider(1) #horizontal
		self.dampen_slider.setRange(0,100)
		self.dampen_slider.setSingleStep(1)

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
			self.dampen_spin,
			2,
			0)
		self.main_layout.addWidget(
			self.dampen_label,
			2,
			1)
		self.main_layout.addWidget(
			self.dampen_slider,
			2,
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

