from turtle import Turtle

START_LENGTH = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.segs = []
    self.create_snake()
    self.head = self.segs[0]
    
  def create_snake(self):
    x_pos = 0
    for box in range(0,START_LENGTH+1):
      box = Turtle(shape = "square")
      box.color("white")
      box.up()
      box.speed("slowest")
      box.goto(x = x_pos,y= 0)
      self.segs.append(box)
      x_pos -=20

  def add_seg(self):
    box = Turtle(shape = "square")
    box.color("white")
    box.up()
    box.speed("slowest")
    self.segs.append(box)

  def move(self): 
    for x in range(len(self.segs)-1,0,-1):
      self.segs[x].goto(self.segs[x-1].pos())
    self.head.forward(MOVE_DISTANCE)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
    
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
  
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)