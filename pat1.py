from turtle import *
speed('fastest')
colors = ['red','purple',]
bgcolor('black')

for i in range(8):
    pencolor('red')
    pensize('2')
    fd(100)
    for i in range(4):
        pencolor('blue')
        pensize('2')
        fd(50)
        fillcolor(colors[i%2])
        begin_fill()
        for i in range(4):
            pencolor('green')
            pensize(2)
            fd(25)
            lt(360/4)
        end_fill()
        lt(360/4)
    lt(360/8)
mainloop()


