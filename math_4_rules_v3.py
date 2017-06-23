#! /usr/bin/python
# coding: utf-8
"""
    See README.md
    --------------------------------
    create by wangtao   yyyy.mm.dd
"""
import sys
import os
import commands
import random 
from setting import *
from user_setting import *
from base_mul_div import *
from make_tiku import *
#reload(sys)
#sys.setdefaultencoding('utf-8')

global pnl 
pnl = make_prime_number(min,max)

def sub():
    #pnl = make_prime_number(min,max)
    round_range=[-1,-2,-2,-2]
    a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    while (a - b) < 800: 
        a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    s = a-b
    d1,d2,d3 = int(a),int(b),int(s)
    result = ( '%s - %s =  ,'% (d1,d2))
    return result,d3

def plus():
    #pnl = make_prime_number(min,max)
    round_range=[-1,-2,-2,-2]
    a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
    s = a + b
    while s > max : 
        a = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        b = round(pnl[random.randint(10,len(pnl)-1)],random.choice(round_range))
        s = a+b
    d1,d2,d3 = int(a),int(b),int(s)
    result = ( '%s + %s =  ,'% (d1,d2))
    return result,d3

if __name__ == '__main__':
    print "This math V3"
    make_tiku(tiku_path)