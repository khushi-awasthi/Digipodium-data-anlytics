from turtle import *
speed('fastest')
bgcolor('black')
for i in range(6):
    rt(60)
    fd(120)
colors=['green','pink',]
i=0
while True:
    pencolor(colors[i%2])
    rt(75)
    fd(300)
    for item in range(5):
        rt(144)
        fd(300)
        i += 1
mainloop()