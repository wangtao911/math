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

def make_prime_number(min,max):
    prime_num_list = []
    for x in range (min, max):
        prime_num=0
        for c in range (2,x/2):
            #print x , c
            if x%c == 0:
                prime_num = 1
        if prime_num == 0:
            prime_num_list.append(x)
    print len(prime_num_list)
    print prime_num_list
    return prime_num_list

def division(a,b,s):
    if s == 0: #等待计算结果，正向计算
        if a in [10,12,14,15,16,18,20,21,24,25,27,28,30,32,35,36,40,42,45,48,49,50,54,56,60,63,64,70,72,80,81,90,100]:
            s = a/b
        else:
            print "%s is NOT right" % a
    elif s != 0:  #反向计算 ，计算除数或者被除数
        if (a in [1,2,3,4,5,6,7,8,9,10]) and b==0:
            b = s / a
        elif (b in [1,2,3,4,5,6,7,8,9,10]) and a == 0: 
            a = s / b
    #print "This is division a,b,s=%s,%s,%s" %(a,b,s)
    #print ( '%s ÷ %s = %s '% (a,b,s))
    return a,b,s

def multiplication(a,b,s):
    if s == 0: #等待计算结果，正向计算
        s = a * b
    elif s in [10,12,14,15,16,18,20,21,24,25,27,28,30,32,35,36,40,42,45,48,49,50,54,56,60,63,64,70,72,80,81,90,100]: #反向计算 ，计算乘数或者被乘数
        if (a in [1,2,3,4,5,6,7,8,9]) and b==0:
            b = s / a
        elif (b in [1,2,3,4,5,6,7,8,9]) and a == 0: 
            a = s / b
        elif (a==0) and (b==0):
            for num in range(2,9):
                if s % num == 0:
                    a = num
                    b = s / a
    #print "This is multiplication a,b,s=%s,%s,%s" %(a,b,s)
    #print ( '%s x %s = %s '% (a,b,s))
    return a,b,s

def rand_mul():
    a = random.choice([4,5,6,7,8,9])
    b = random.choice([3,4,5,6,7,8,9])
    s = a * b
    #print "This is multiplication a,b,s=%s,%s,%s" %(a,b,s)
    #print ( '%s x %s = %s '% (a,b,s))
    return a,b,s

def rand_div():
    a = rand_mul()[2]
    s = 0
    b_list = [2,3,4,5,6,7,8,9]
    random.shuffle(b_list)
    b = b_list.pop()
    while (a % b != 0) or (a/b > 9):
        b = b_list.pop()
    s = a / b
    #print "This is division a,b,s=%s,%s,%s" %(a,b,s)
    #print ( '%s ÷ %s = %s '% (a,b,s))
    return a,b,s

def mul_div():
    d1,d2,d3=1,1,1
    while d3==d1 or d3==d2 or d3>9:
        d1,d2,s = rand_mul()
        ncare,d3,ncare_ss = multiplication(0,0,s)
    ss = d1*d2/d3
    result = ( '%s x %s ÷ %s , = ,'% (d1,d2,d3))
    return result,ss

def div_mul():
    d1,d2,s = rand_div()
    d3 = random.randint(4,9)
    ss = d1/d2*d3
    result = ( '%s ÷ %s x %s , = ,'% (d1,d2,d3))
    return result,ss