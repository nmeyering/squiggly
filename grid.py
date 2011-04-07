from PyQt4.QtGui import QGraphicsItem
from PyQt4.QtGui import QPen
from PyQt4.QtGui import QColor
from PyQt4.QtCore import QLineF
from PyQt4.QtCore import QRectF

class Grid(QGraphicsItem):
	def __init__(self, size = 32, bounds = QRectF(0,0,100,100), pen = QPen(QColor(0,0,255,64))):
		self.bounds = bounds
		QGraphicsItem.__init__(self)
		self.lines = []
		self.size = size
		self.pen = pen
	
	def paint(self, painter, option, widget = None):
		bounds = self.bounds
		for x in range(0, int(bounds.width()), self.size):
			self.lines.append(
				QLineF(
					x,
					bounds.y(),
					x,
					bounds.y() + bounds.height()))

		for y in range(0, int(bounds.height()), self.size):
			self.lines.append(
				QLineF(
					bounds.x(),
					y,
					bounds.x() + bounds.width(),
					y))

		painter.setPen(self.pen)

		for line in self.lines:
			painter.drawLine(line)

	def boundingRect(self):
		return self.bounds
