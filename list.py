from turtle import *

speed('fastest')
bgcolor('black')
colors =['red','blue','orange','pink','purple']
i=0
while True:
    pencolor(colors[i%5])
    fd(10+i)
    lt(50)
    i += 1
mainloop()