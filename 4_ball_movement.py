import turtle

wn = turtle.Screen() # 창 호출
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0) # 윈도우 트레이서 : 기본적으로 하는 작업으로 실제로 창을 멈추게 하는 것

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

# Function
def paddle_a_up():
    y = paddle_a.ycor() # ycor 메소드는 turtle module 에서 가져옴. y 좌표를 반환 
    y += 20
    paddle_a.sety(y) # sety 를 새로운 y 로 적용

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() # 창에 키보드의 입력(keyboard input)을 수신함

wn.onkeypress(paddle_a_up, "w") # 소문자 w 이므로 caps lock 이 걸려있는 경우 작동하지 않게됨, w 키를 입력하면 paddle_a_up 함수를 호출
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) # 현재 공의 좌표 + 움직임
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290) # y의 현 좌표가 290일 때, 다시 290으로 설정하여 특정 유형의 문제발생을 방지
        ball.dy *= -1 # 방향 반전

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1