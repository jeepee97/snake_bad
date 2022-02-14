from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Snake:
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    UP = 4

    def __init__(self):
        self.body = [[5, 10], [5, 11]]
        self.head = [self.body[0][0], self.body[0][1]]
        self.grow = False
        self.direction = 2
        self.color = 0xfca311

    def updateDirection(self, key):
        # bug dans les directions (et enlever les chiffres)
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