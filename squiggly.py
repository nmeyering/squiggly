# coding=utf-8
from PyQt4 import QtGui
from PyQt4.QtGui import QWidget, QGraphicsScene, QPen, QColor

class Squiggly( QWidget ):
	def __init__( self, lines ):
		QWidget.__init__( self )
		scene = QGraphicsScene()
		for line in lines:
			scene.addLine(line)

		self.layout = QtGui.QGridLayout()
		self.view = QtGui.QGraphicsView()
		self.setLayout(
			self.layout)
		self.layout.addWidget(
			self.view)

		#scene.addRect(0,0,50,50,QPen(QColor("red")))
		self.view.setScene(scene)
