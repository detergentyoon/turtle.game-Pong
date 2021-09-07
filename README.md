`turtle module` 은 많은 기능을 가진 `pygame`에 비해 기능성은 떨어지지만 간단한 게임 제작의 경우 이 방법이 더 쉽게 시작할 수 있습니다.
창을 여는데 매우 편리하고 고전적인 구식 프로그램 게임에 잘 작동합니다.
(이 프로그램은 초보자를 위해 작성되었으므로 실제로는 객체 지향 프로그래밍을 사용하지 않습니다.)

# **2_ game_objects**
### Paddle process
```python
paddle_a = turtle.Turtle()
```
`turtle` = `turtle` module 적용
`Turtle` = `Turtle class`

<br>

```python
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
```
너비와 높이가 5:1 비율

<br>

```python
paddle_a.penup()
```
`penup` : 설정값을 실제로 화면에 그려주는 역할

<br>


```python
paddle_a.goto(-350, 0)
```
![sd](info\screen.jpg)

<br>

# **5_ paddle_collision**
```python
    # Ball collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() - 55):
        ball.setx(-340) # 공이 패들면에서 미끄러지는 현상 방지
        ball.dx *= -1
```
`(ball.xcor() < -340 and ball.xcor() > -350)` : 패들 뒤에서 공이 튕기는 현상 방지
`ball.setx(-340)` : 공이 패들과 접촉 시 패들의 면에서 미끄러지는 현상 방지, 이것은 공이 이동하던 좌표가 -340 보다 더 작아질 때 발동하는 if문 때문에 생기는 버그로, setx를 할당해줌으로서 공이 패들과 충돌 시 곧바로 튕겨나갈 수 있도록 해줌