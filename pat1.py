from turtle import *
speed('fastest')
colors = ['black','purple']
bgcolor('pink')

for i in range(6):
    pencolor('red')
    pensize('2')
    fd(100)
    for i in range(6):
        pencolor('purple')
        pensize('2')
        fd(50)
        fillcolor(colors[i%2])
        begin_fill()
        for i in range(6):
            pencolor('green')
            pensize(2)
            fd(25)
            lt(360/6)
        end_fill()
        lt(360/6)
    lt(360/6)
mainloop()


