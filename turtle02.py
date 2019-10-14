# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:42:05 2019

@author: LZM
"""

import turtle
hg=turtle.Turtle()
def square(t,length):
       for i in range(4):
        t.fd(length)
        t.lt(90)
print('请输入边的长度：')
length=input()
length=float(length)
square(hg,length)

