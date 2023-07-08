from turtle import *


#function definition
def square(size,color='red'):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        fd(size)
        rt(90)
    end_fill()
def  hexagon(size,color='red'):
    fillcolor(color)
    begin_fill()
    for i in range(6):
        fd(size)
        rt(60)
    end_fill()
square(100,'blue') #calling
square(50,'green')
hexagon(100,'purple')
hexagon(50,'red')
square(25,'yellow')

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