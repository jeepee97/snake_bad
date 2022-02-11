from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from SnakeGame.Board import Board
import sys
#from Snake_AI import Snake_AI

class SnakeGame(QMainWindow):
    def __init__(self):
        super(SnakeGame, self).__init__()
        self.statusbar = self.statusBar()

        self.sboard = Board(self)
        self.sboard.msg2statusbar[str].connect(self.statusbar.showMessage)

        self.setCentralWidget(self.sboard)
        
        self.setWindowTitle('PyQt5 Snake game')
        self.resize(1800, 1200)

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

        self.sboard.start()
        self.show()