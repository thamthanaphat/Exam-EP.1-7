import turtle
T= turtle.Pen()
T.shape("turtle")
for i in range(9):
    T.circle(190-i,90)
    T.left(90)
    T.circle(190-i,90)
    T.left(10)
