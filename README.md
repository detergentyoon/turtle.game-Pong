`turtle module`은 많은 기능을 가진 `pygame`에 비해 기능성은 떨어지지만 간단한 게임 제작의 경우 이 방법이 더 쉽게 시작할 수 있습니다.

turtle은 그래픽 창을 여는데 매우 편리하고 고전적인 구식 프로그램에 잘 작동합니다.

(이 프로그램은 초보자를 위해 작성되었으므로 실제로는 객체 지향 프로그래밍을 사용하지 않습니다.)

# **2_ game_objects**
```python
paddle_a = turtle.Turtle()
```
`turtle` = `turtle` module 명렁어를 적용합니다.  
`Turtle` = `Turtle class` 를 의미합니다.

<br>

```python
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
```
너비와 높이가 5:1 비율을 이루도록 합니다.

<br>

```python
paddle_a.penup()
```
`penup` : 설정한 값을 turtle이 실제로 화면에 그려주는 역할을 합니다.

<br>


```python
paddle_a.goto(-350, 0)
```
![sd](info\screen.jpg)  
중앙이 좌표의 (0, 0)으로 적용되어 있습니다.

<br>

# **5_ paddle_collision**
```python
    # Ball collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() - 55):
        ball.setx(-340) # 공이 패들면에서 미끄러지는 현상 방지
        ball.dx *= -1
```
`(ball.xcor() < -340 and ball.xcor() > -350)` : 패들 뒷면과 화면 경계 사이에서 비정상적으로 공이 튕기며 득점 반영이 되지 않는 현상을 방지합니다.

`ball.setx(-340)` : 공이 패들과 접촉 시 패들의 면에서 미끄러지는 현상을 방지합니다. 이것은 공이 이동하던 좌표가 -340 보다 더 작아질 때만 호출되도록 설정한 `if`문 때문에 생기는 버그로, `setx`를 할당해줌으로서 공이 패들과 충돌 시 곧바로 튕겨나갈 수 있도록 해줍니다.

<br>

# **8_ winner**
```python
# Winner display
if score_a == 3:
    pen.clear()
    ball.reset()
    paddle_a.reset()
    paddle_b.reset()
    pen.goto(0, 50)
    pen.write("Player    A    Win ! !", align="center", font("ARCADECLASSIC", 50, "normal"))
    winsound.PlaySound("sounds/winner.wav", winsound.SND_NOWAIT)
    restart.goto(0, -50)
    restart.write("regame press r", align="center", font=("pressstart k", 25, "normal")
```
3점(예시)을 먼저 달성하는 경우 승리 & 재시작 유무 화면을 띄웁니다.

이 때 이전에 그려진 turtle 요소들을 화면에서 지우고, A 와 B의 점수판으로 사용되던 텍스트란 `pen`은 `goto` 를 통해 새로운 좌표로 옮기고, `write` 를 통해 텍스트 내용을 **수정**하기로 했습니다.

그렇기 때문에 이전의 `pen`의 설정 내용들을 `clear()`를 통해 그렸던 요소들만 삭제 후 위치는 그대로 두었습니다.
>`turtle.clear()` 이 turtle이 그렸던 모든 것을 삭제합니다. (turtle의 **위치는 유지**됩니다.)

>`turtle.reset()` 이 turtle의 상태(예: 방향, 위치 등)를 수행한 `turtle clear()` 다음 재설정 합니다. (turtle의 **위치도 초기화**됩니다.)

<br>

반대로 `ball`과 `paddle`은 `pen`처럼 수정하여 재사용하지 않고 화면에서 완전히 사라지길 바랬기 때문에 `reset()`을 통해 turtle의 모든 수행을 초기화시켜 화면에서 완전히 지워버렸습니다.

그래서 하나의 플레이어가 승리 점수에 도달하면 위 logic을 통해 승리 & 재시작 유무 화면으로 전환된 것 처럼 나타낼 수 있었습니다.