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



mainloop()