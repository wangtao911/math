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
from math_4_rules_v3 import *

question_type_list = [sub,plus,sub_plus,plus_sub,plus_sub_bracket,sub_plus_bracket]
question_type_list = question_type_list + [mul_div,div_mul,sub_div,sub_div_2,plus_div,plus_sub,plus_sub_2,plus_mul,sub_mul,sub_plus,sub_plus_2]
def make_tiku(tiku_path):
    file_path = tiku_path
    for filename in range (1,11):
        answer_list=[]
        question_list=[]
        type_list = question_type_list
        for n in range(0,100):
            question,answer = random.choice(type_list)()
            question_list.append(question)
            answer_list.append(answer)
        #生成题库
        question_file = "Q-" + str(filename)+".csv"
        fo = open(file_path+question_file, "wb")
        fo.write( ",,Name,,Date,,Score,,Timer,,%s\n" % (question_file))
        for n in range(0,20):
            text = ","
            for m in range(0,2):
                text = text + str(n+m*20+1)+","+str(question_list[n+m*20])+","
            fo.write( text +"\n")
        fo.close()
        #生成答案
        answer_file = "A-" + str(filename)+".csv"
        fo = open(file_path+answer_file, "wb")
        fo.write( ",,,,,,,,,,%s\n" %(answer_file))
        for n in range(0,20):
            text = ","
            for m in range(0,2):
                text = text + str(n+m*20+1)+","+str(answer_list[n+m*20])+","+","
            fo.write( text +"\n")