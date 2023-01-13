from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

#SCREEN
screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("My snake game!")
screen.listen()
screen.tracer(0)

#INIT SNAKE
snake = Snake()
food = Food()
food.refresh()
score = Score()


#CONTROLS
screen.onkeypress(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

#GAME
game_on = True

while game_on:
  
  screen.update()  
  snake.move()
  time.sleep(0.1)

  #compare distance beteen food and snake
  if snake.head.distance(food) < 15:
    print ("nom nom nom")
    snake.add_seg()
    food.refresh()
    score.goal()
    
  #GAME OVER'score
  for x in snake.segs[1:]:
    if snake.head.distance(x) < 15:
      score.reset()
      snake.reset()
  
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
      score.reset()
      snake.reset()
    
    


screen.exitonclick()