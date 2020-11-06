import turtle
import math

bob= turtle.Turtle()
print(bob)
#turtle.mainloop()

'''
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
turtle.mainloop()
'''

#4-1
'''def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
square(bob)
turtle.mainloop()
'''
#4-2
'''def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
square(bob,360)
turtle.mainloop()
'''
#4-3
def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
'''n=input()
polygon(bob,360,n)
turtle.mainloop()
'''
#4-4
def circle(t,r):
    polygon(t,r*math.pi/180,360)
#n=input()
#circle(bob,1,int(n))  # 输入的是360的倍数 完美的圆
#bob.circle(100)
#circle(bob,100)
#turtle.mainloop()

#4-5
def arc(t,r,a):
    #polygon(t,r*math.pi/180,a)
    for i in range(a):
        t.fd(r*math.pi/180)
        t.lt(1)
arc(bob,100,165)
turtle.mainloop()
