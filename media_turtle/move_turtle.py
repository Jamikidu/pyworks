# turtle 모듈
import turtle as t

t.shape("turtle")
"""
t.forward(100) # 직진 100px
t.left(90)  # 머리방향이 왼쪽으로 90도
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)


"""

# 삼각형을 그리며 이동

"""
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
"""

for i in range(4):
    t.forward(100)
    t.right(90)

t.color('blue')
for i in range(3):
    t.forward(100)
    t.left(120)

t.color("red")
t.pensize(2)
t.circle(50)
t.mainloop()
