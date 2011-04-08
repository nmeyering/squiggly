from PyQt4.QtGui import QGraphicsItem
from PyQt4.QtGui import QGraphicsPolygonItem
from PyQt4.QtGui import QPen
from PyQt4.QtGui import QColor
from PyQt4.QtGui import QPolygonF
from PyQt4.QtCore import QLineF, QRectF, QPointF
from functools import reduce
import math
import random
import planar

class SubRegion(QGraphicsPolygonItem):
	def __init__(self, poly = None, dim = None):
		if not poly:
			if not dim:
				raise ValueError("need to set bounding rect!")
			else:
				poly = []
				for i in range(10):
					poly.append(planar.Point(
						random.randint(dim.left(),dim.right()),
						random.randint(dim.top(),dim.bottom())))
				poly = planar.Polygon.convex_hull(poly)
				poly = QPolygonF([QPointF(p.x,p.y) for p in poly])
			
		QGraphicsPolygonItem.__init__(self, poly)
		self.setConnectors([(0,random.random()),(len(poly)//2,random.random())])

	def setConnectors(self, conn):
		self.connectors = []
		points = list(self.polygon())
		for c in conn:
			a = points[c[0] % len(points)]
			b = points[(c[0] + 1) % len(points)]
			self.connectors.append( a + (b - a)* c[1] )

	def paint(self, painter, option, widget = None):
		QGraphicsPolygonItem.paint(self, painter, option, widget)
		pen = QPen(QColor("yellow"))
		pen.setWidth(10)
		painter.setPen(pen)
		painter.drawPoint(self.entrance())

		pen.setColor(QColor("magenta"))
		painter.setPen(pen)
		painter.drawPoint(self.exit())
		for c in self.connectors[2:]:
			painter.drawPoint(c)

		pen.setColor(QColor(0,255,255))
		pen.setWidth(2)
		painter.setPen(pen)
		painter.drawEllipse(self.cog(), 5, 5)

	def cog(self):
		points = list(self.polygon())
		return reduce(QPointF.__add__, points) * (1/len(points))
	
	def entrance(self):
		return self.connectors[0]

	def exit(self):
		return self.connectors[1]
