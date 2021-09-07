import turtle

wn = turtle.Screen() # 창 호출
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0) # 윈도우 트레이서 : 기본적으로 하는 작업으로 실제로 창을 멈추게 하는 것

# Main game loop
while True:
    wn.update()