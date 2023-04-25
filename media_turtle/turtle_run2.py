# turtle run 게임 심화
import turtle as t
import random

# 점수와 게임 스위치 변수
score = 0
playing = False

# 적 거북이 생성
te = t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0, 200)

# 주인공 거북이
t.setup(550, 550)
t.bgcolor('lightgreen')
t.shape('turtle')
t.color('white')
t.speed(0)
t.up()



# 먹이
tf = t.Turtle()
tf.shape('circle')
tf.color('yellow')
tf.speed(0)
tf.up()
tf.goto(0, -200)


# 방향 전환 함수
def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

def message(m1, m2):
    t.clear()
    t.goto(0, 120)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -120)
    t.write(m2, False, "center", ("", 15))
    t.home()  # 주인공 거북이의 (0, 0)
    te.goto(0, 200)

def play():
    global score
    global playing
    t.forward(15)


    if random.randint(1, 4) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)

    speed = score + 12  # 기본속도 12
    if speed > 20:
        speed = 20
    te.forward(speed)

    # 적 거북이와 닿지 않으면 게임 유지
    # 적 거북이와 닿으면 게임 종료
    if t.distance(te) < 14:
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    # 주인공 거북이가 먹이에 닿으면 점수가 올라감
    if t.distance(tf) < 14:
        score += 1
        t.write(score)  # 점수 출력
        start_x = random.randint(-250, 250)
        start_y = random.randint(-250, 250)
        tf.goto(start_x, start_y)

    if playing:
        t.ontimer(play, 80)  # 0.1초 간격으로 계속 play 호출


t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()
message("Turtle Run", "[Space]")
play()


t.mainloop()