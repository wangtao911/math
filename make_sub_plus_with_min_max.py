#! /usr/bin/python
# coding: utf-8
"""
    根据给定的 最大值 与 最小值
    生成 加减题库
    对于数字取整程度，由round_range控制
    sub()                a-b
    plus()               a+b
    sub_plus()           a-b+c
    plus_sub()           a+b-c
    plus_sub_bracket()   a+(b-c)
    sub_plus_bracket()   a-(b+c)
    --------------------------------
    create by wangtao   2017.06.23
"""
import sys
import os
import commands
import random 
from setting import *
from user_setting import *
from make_prime_number import *

pnl = make_prime_number(min,max)
round_range=[-1,-2,-2,-2]

def sub():
    
    a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    s = a - b
    while (a < b) or (s < ((max-min)/13)) or (s > max) or (s < min): 
        a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        s = a - b
    d1,d2,d3 = int(a),int(b),int(s)
    result = ( '%s - %s , = ,'% (d1,d2))
    return result,d3

def plus():
    
    a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    s = a + b
    while (s > max) or (s < min) : 
        a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        s = a + b
    d1,d2,d3 = int(a),int(b),int(s)
    result = ( '%s + %s , = ,'% (d1,d2))
    return result,d3

def sub_plus():
    
    a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    c = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    s = a - b + c
    while (a < b) or (s < ((max-min)/13)) or (s > max) or (s < min): 
        a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        c = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        s = a - b + c
    d1,d2,d3,d4 = int(a),int(b),int(c),int(s)
    result = ( '%s - %s + %s , = ,'% (d1,d2,d3))
    return result,d4

def plus_sub():
    
    a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    c = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    s = a + b - c
    while ((a+b)<c) or ((a+b) > max) or (s < ((max-min)/13)) or (s > max) or (s < min) : 
        a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        c = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        s = a + b - c
    d1,d2,d3,d4 = int(a),int(b),int(c),int(s)
    result = ( '%s + %s - %s , = ,'% (d1,d2,d3))
    return result,d4

def plus_sub_bracket():
    
    a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    c = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    s = a - b + c
    while (a < b) or (s < ((max-min)/13)) or (s > max) or (s < min): 
        a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        c = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        s = a - b + c
    d1,d2,d3,d4 = int(a),int(b),int(c),int(s)
    result = ( '%s + (%s - %s) , = ,'% (d3,d1,d2))
    return result,d4

def sub_plus_bracket():
    
    a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    c = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    s = a - (b + c)
    while ((b+c)>a) or ((b+c) > max) or (s < ((max-min)/13)) or (s > max) or (s < min) : 
        a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        c = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        s = a - (b + c)
    d1,d2,d3,d4 = int(a),int(b),int(c),int(s)
    result = ( '%s - (%s + %s) , = ,'% (d1,d2,d3))
    return result,d4

print sub_plus_bracket()[0]
