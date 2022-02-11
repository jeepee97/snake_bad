import sys
from SnakeGame.SnakeGame import SnakeGame
#from MainWindow import MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def main():
    app = QApplication([])
    launch_game = SnakeGame()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()