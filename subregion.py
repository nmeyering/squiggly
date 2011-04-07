from PyQt4.QtGui import QGraphicsItem
from PyQt4.QtGui import QGraphicsPolygonItem
from PyQt4.QtGui import QPen
from PyQt4.QtGui import QColor
from PyQt4.QtCore import QLineF, QRectF, QPointF
from functools import reduce
import math

class SubRegion(QGraphicsPolygonItem):
	def __init__(self, poly, connectors = []):
		QGraphicsPolygonItem.__init__(self, poly)
		self.connectors = connectors

	def setConnectors(self, connectors):
		self.connectors = []
		points = list(self.polygon())
		for c in connectors:
			a = points[c[0] % len(points)]
			b = points[(c[0] + 1) % len(points)]
			self.connectors.append( a + (b - a)* c[1] )

	def paint(self, painter, option, widget = None):
		QGraphicsPolygonItem.paint(self, painter, option, widget)
		pen = QPen(QColor("red"))
		pen.setWidth(10)
		painter.setPen(pen)
		for c in self.connectors:
			painter.drawPoint(c)

		pen.setColor(QColor(0,255,255))
		painter.setPen(pen)
		painter.drawPoint(self.cog())

	def cog(self):
		points = list(self.polygon())
		return reduce(QPointF.__add__, points) * (1/len(points))
