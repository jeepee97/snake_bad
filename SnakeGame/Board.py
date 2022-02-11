from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from SnakeGame.Snake import Snake
from SnakeGame.Food.Food import Food
import random
import sys

class Board(QFrame):
    msg2statusbar = pyqtSignal(str)
    #changer le speed et le nom de variable
    SPEED = 400
    HORIZONTAL_BLOCKS_COUNT = 60
    VERTICAL_BLOCKS_COUNT = 40

    def __init__(self, parent):
        super(Board, self).__init__(parent)
        #enlever la redondance et simplement appeler reset()
        self.setStyleSheet("background-color: #15f4ee")
        self.timer = QBasicTimer()
        self.snake = Snake()
        self.food = []
        self.dropFood()
        self.setFocusPolicy(Qt.StrongFocus)

    def reset(self):
        #changer le background color
        self.setStyleSheet("background-color: #15f4ee")
        self.timer = QBasicTimer()
        self.snake = Snake()
        self.food = []
        self.dropFood()
        self.setFocusPolicy(Qt.StrongFocus)

    def squareWidth(self):
        return self.contentsRect().width() / Board.HORIZONTAL_BLOCKS_COUNT

    def squareHeight(self):
        return self.contentsRect().height() / Board.VERTICAL_BLOCKS_COUNT

    def start(self):
        self.game_started = True
        self.msg2statusbar.emit(str(len(self.snake.body) - 2))
        self.timer.start(Board.SPEED, self)

    def drawSquare(self, painter, x, y, colorHexa):
        color = QColor(colorHexa)
        padding = 1
        painter.fillRect(x + padding, 
                         y + padding, 
                         self.squareWidth() - 2*padding,
                         self.squareHeight() - 2*padding, 
                         color)

    def moveSnake(self):
        self.snake.move(self.msg2statusbar)

    def hitWall(self):
        if self.snake.head[0] < 0 or self.snake.head[0] == Board.HORIZONTAL_BLOCKS_COUNT or \
           self.snake.head[1] < 0 or self.snake.head[1] == Board.VERTICAL_BLOCKS_COUNT:
            self.msg2statusbar.emit(str("oops.."))
            self.game_started = False
            self.snake.body = [[x, y] for x in range(0, 60) for y in range(0, 40)]
            self.food = []
            self.timer.stop()
            self.update()
    
    def isSuicide(self):
        for i in range(1, len(self.snake.body)):
            if self.snake.body[i] == self.snake.body[0]:
                # redondance, faire une fonction avec ca et la fonction hitWall()
                self.msg2statusbar.emit(str("that aint food..."))
                self.game_started = False
                self.snake.body = [[x, y] for x in range(0, 61) for y in range(0, 41)]
                self.food = []
                self.timer.stop()
                self.update()            

    def isFoodCollision(self):
        for f in self.food:
            pos = f.pos
            if pos == self.snake.body[0]:
                self.food.remove(f)
                self.dropFood()
                self.snake.grow = True

    def dropFood(self):
        x = 0
        y = 0
        while (True):
            x = random.randint(0, Board.HORIZONTAL_BLOCKS_COUNT - 1)
            y = random.randint(0, Board.VERTICAL_BLOCKS_COUNT - 1)
            posInvalid = False
            for bodyPart in self.snake.body:
                if (bodyPart == [x, y]):
                    posInvalid = True
            for f in self.food:
                if (f.pos == [x,y]):
                    posInvalid = False
            if not posInvalid:
                break
        food = [Food([x,y])]

        #food = FoodFactory.createFood(self.snake.body, self.food, Board.HORIZONTAL_BLOCKS_COUNT, Board.VERTICAL_BLOCKS_COUNT)
        self.food = self.food + food

    ##### QFrame Functions #####
    # these function definition cannot be changed

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.contentsRect()
        board_top = rect.bottom() - Board.VERTICAL_BLOCKS_COUNT * self.squareHeight()

        for pos in self.snake.body:
            self.drawSquare(painter, rect.left() + pos[0] * self.squareWidth(),
                             board_top + pos[1] * self.squareHeight(), self.snake.color)#0xfca311)
        for f in self.food:
            pos = f.pos
            self.drawSquare(painter, rect.left() + pos[0] * self.squareWidth(),
                             board_top + pos[1] * self.squareHeight(), f.color)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.moveSnake()
            self.isFoodCollision()
            self.isSuicide()
            self.update()
            self.hitWall()

    def keyPressEvent(self, event):
        key = event.key()
        self.snake.updateDirection(key)

        if key == Qt.Key_Return:
            if self.game_started == False:
                self.reset()
                self.start()