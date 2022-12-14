from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("arial",15,"bold")

class Score(Turtle):

  def __init__(self):    
    super().__init__()
    self.score = 0
    self.up()
    self.color("white")
    self.speed("fastest")
    self.goto(0,270)
    self.hideturtle()
    self.write(arg = f"SCORE: {self.score}", align = ALIGNMENT,font = FONT)

  def goal(self):
    self.score +=1
    self.clear()
    self.write(f"SCORE: {self.score}", align = ALIGNMENT,font = FONT)

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER...", align = ALIGNMENT,font = FONT)
    