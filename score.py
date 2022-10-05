from turtle import Turtle

class Score(Turtle):

  def __init__(self):    
    super().__init__()
    self.score = 0
    self.up()
    self.color("white")
    self.speed("fastest")
    self.goto(0,270)
    self.hideturtle()
    self.write(arg = f"SCORE: {self.score}",align = "center",font = ("arial",15,"bold"))

  def goal(self):
    self.score +=1
    self.clear()
    self.write(f"SCORE: {self.score}")