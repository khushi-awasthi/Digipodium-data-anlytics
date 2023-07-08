
from turtle import*
speed('fastest')
colors = ['red','blue','green','yellow']
n=70
h=0
for i in range (360):
    
    
    for i in range (200):
        pencolor(colors[i%4])
        left(50)
        circle(200)

mainloop()