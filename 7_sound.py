import turtle
import winsound

wn = turtle.Screen() # 창 호출
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0) # 윈도우 트레이서 : 기본적으로 하는 작업으로 실제로 창을 멈추게 하는 것

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid = 1, stretch_len = 1)
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

# Pen
pen = turtle.Turtle()
pen.speed(0) # 이동 속도 x , 애니메이션 속도 o
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0   Player B : 0", align="center", font=("Courier", 24, "normal"))


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
        winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A : {score_a}   Player B : {score_b}", align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("sounds/goal.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear() # 이전 스코어 화면에서 제거(텍스트 곂침 방지)
        pen.write(f"Player A : {score_a}   Player B : {score_b}", align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("sounds/goal.wav", winsound.SND_ASYNC)
        
    # Paddle & Ball collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() - 55):
        ball.setx(-340) # 패들면을 미끄러지는 현상 방지, setx를 할당해줌으로서 패들과 충돌 시 바로 튕겨나갈 수 있도록 함
        ball.dx *= -1
        winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() - 55):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)