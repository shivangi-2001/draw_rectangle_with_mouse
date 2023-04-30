from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class DrawShapes(QLabel):

    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setScaledContents(True)
        self.start_point = None
        self.end_point = None
        self.completed_rect = None
        self.drawing = False
        self.setCursor(Qt.CrossCursor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.start_point = event.pos()
            self.end_point = event.pos()

    def mouseMoveEvent(self, event):
        if self.start_point:
            self.end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.completed_rect = QRect(self.start_point, self.end_point).normalized()
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.black)
        if self.drawing:
                rect = QRect(self.start_point, self.end_point).normalized()
                painter.drawRect(rect)
                painter.end()
        elif self.completed_rect:
                painter.drawRect(self.completed_rect)
                painter.end()
