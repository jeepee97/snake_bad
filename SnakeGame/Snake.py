from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Snake:
    # enlever tous les (1,2,3,4) qui serve de direction

    def __init__(self):
        self.body = [[5, 10], [5, 11]]
        self.head = [self.body[0][0], self.body[0][1]]
        self.grow = False
        self.direction = 2
        self.color = 0xff08fc #0xfca311
        print("snake")

    def updateDirection(self, key):
        if key == Qt.Key_Left:
            if self.direction != 1:
                self.direction = 2
        elif key == Qt.Key_Right:
            if self.direction != 2:
                self.direction = 1
        elif key == Qt.Key_Down:
            if self.direction != 4:
                self.direction = 3
        elif key == Qt.Key_Up:
            if self.direction != 3:
                self.direction = 4
    
    def move(self, msg2statusbar):
        if self.direction == 1:
            self.head = [self.head[0] - 1, self.head[1]]
        if self.direction == 2:
            self.head = [self.head[0] + 1, self.head[1]]
        if self.direction == 3:
            self.head = [self.head[0], self.head[1] + 1]
        if self.direction == 4:
            self.head = [self.head[0], self.head[1] - 1]

        self.body.insert(0, self.head)
        # ne pas ecrire condition == False
        if (self.grow == False):
            self.body.pop()
        else:
            msg2statusbar.emit(str(len(self.body)-2))
            self.grow = False