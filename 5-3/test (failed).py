# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:38:47 2020

@author: a1377
"""

import math
import turtle

def DrawPetals(t,n,r):
        t.fd(r)
        t.lt(n+90)
        t.fd(r)
        t.lt(n+90)
        t.fd(r)
        t.lt(180-n)

def DrawPie(t,n,r):
    for i in range(n):
        DrawPetals(t, n, r)
        t.lt(360/n)
        
        
bob=turtle.Turtle()

DrawPie(bob, 6, 40)
turtle.mainloop()