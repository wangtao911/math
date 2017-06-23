#! /usr/bin/python
# coding: utf-8
"""
    创建一个素数（质数）的列表
    --------------------------------
    create by wangtao   2017.06.22
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
    print "Prime Number list :"+str(len(prime_num_list))
    #print prime_num_list
    return prime_num_list
