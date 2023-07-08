#from turtle import *
#speed('fastest')
#color('red','yellow')
#begin_fill()
#while True:
 #   forward(200)
  #  left(170)
   # if abs(pos())<1:
    #    break
#end_fill()
#done()


import turtle
t=turtle.Turtle()

r=10
n=10

for i in range(1, n+1 ,1):
    t.circle(r*i)
