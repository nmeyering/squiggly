from PyQt4.QtGui import QGraphicsItem
from PyQt4.QtGui import QPen
from PyQt4.QtGui import QColor
from PyQt4.QtCore import QLineF, QRectF, QPointF
import random

class Path(QGraphicsItem):
	def __init__(self, start, end, pen = QPen(QColor(0,0,0,255))):
		self.pen = pen

		QGraphicsItem.__init__(self)

		self.starting_line = QLineF(start, end)
		self.bounds = QRectF(
			start - (end - start),
			end + (end - start))

		self.steps = 4
		self.smooth = 50
		self.dampen = 100
		self.update_lines()

	def update_lines(self):
		self.prepareGeometryChange()
		self.lines = self.generate_lines(
			self.starting_line,
			self.steps,
			self.smooth / 100.0,
			self.dampen / 100.0)

	def generate_lines(self, line, steps = 4, smooth = 0.7, dampen = 1.0):
		if steps <= 0:
			return [line]
		mid = (line.p1() + line.p2()) * 0.5
		diff = (line.p2() - line.p1())
		norm = QPointF(-diff.y(), diff.x())
		mid += norm * (random.random() - 0.5) * smooth
		return self.generate_lines(
			QLineF(line.p1(), mid), steps - 1, smooth * dampen
			) + self.generate_lines(
			QLineF(mid, line.p2()), steps - 1, smooth * dampen)

	def paint(self, painter, option, widget = None):
		painter.setPen(self.pen)
		for line in self.lines:
			painter.drawLine(line)

	def boundingRect(self):
		return self.bounds
