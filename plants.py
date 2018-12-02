#!/usr/bin/env python3

"""planets.py: Description of the moving plants around the sun.

__author__ = "WangKunhao"
__pkuid__  = "1800011715"
__email__  = "1800011715@pku.edu.cn"
"""
import math
import turtle

Mercury=turtle.Turtle()
Venus=turtle.Turtle()
Earth=turtle.Turtle()
Mars=turtle.Turtle()
Jupiter=turtle.Turtle()
Saturn=turtle.Turtle()
Sun=turtle.Turtle()
r=[40,60,80,100,130,160]
colors=['gray','orange','blue','red','brown','green','white']
planets=[Mercury,Venus,Earth,Mars,Jupiter,Saturn,Sun]
def planet():
    wn=turtle.Screen()
    wn.bgcolor('black')
    for i in range(7):
        planets[i].shape('circle')
        planets[i].color(colors[i])
        planets[i].speed(0)
        
def position():
    for i in range(6):
        planets[i].penup()
        x=r[i]*math.cos(math.radians(60*i))
        y=r[i]*math.sin(math.radians(60*i))
        planets[i].goto(x,y)
        planets[i].pendown()

def step(t,r,jd,i):
    x=r*math.cos(math.radians(jd))
    y=r*math.sin(math.radians(jd))
    t.goto(x,y)

def main():
    planet()
    position()
    jd=[0,60,120,180,240,300]
    for time in range(1000):
        for i in range(6):                  
            djd=5
            jd[i]=jd[i]+djd
            step(planets[i],r[i],jd[i],i)
    turtle.done()

if __name__ == '__main__':
    main()
