import sys
from PySide2.QtWidgets import *
from draw_shapes import  DrawShapes

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.ui = DrawShapes()
        self.setCentralWidget(self.ui)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()