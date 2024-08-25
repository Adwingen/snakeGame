from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    return screen


def play_game(screen, snake, food, score):
    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.update_score()

        # Detect collision with wall
        if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or
                snake.head.ycor() > 290 or snake.head.ycor() < -290):
            game_is_on = False
            score.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()

    response = screen.textinput("Game Over", "Want to play again? (yes/no)").strip().lower()
    if response in ("sim", "s", "yes", "y"):
        screen.clear()
        main()
    else:
        screen.bye()


def main():
    screen = setup_screen()

    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    play_game(screen, snake, food, score)


if __name__ == "__main__":
    main()






