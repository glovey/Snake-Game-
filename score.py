from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("arial",15,"bold")

class Score(Turtle):

  def __init__(self):    
    super().__init__()
    self.score = 0
    with open("data.txt", "r") as data:
      self.high_score = data.read()    
    self.up()
    self.color("white")
    self.speed("fastest")
    self.goto(0,270)
    self.hideturtle()
    self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align = ALIGNMENT,font = FONT)


  def update_scoreboard(self):
    self.clear()
    self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align = ALIGNMENT,font = FONT)

  def goal(self):
    self.score +=1
    self.update_scoreboard()   

  def reset(self):
    if self.score > int(self.high_score):
      self.high_score = self.score
      with open("data.txt", "w") as f:
        f.write(f"{self.high_score}")
        
    self.score = 0
    self.update_scoreboard()

        