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
#reload(sys)
#sys.setdefaultencoding('utf-8')

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

def fix_sub():
    s = rand_mul()[2]
    a = random.randint(32,92)
    while a < s:
        s = rand_mul()[2]
        a = random.randint(32,92)
    b = a - s
    return a,b,s

def sub_div():
    d1,d2,s = fix_sub()
    ncare,d3,ncare_ss = multiplication(0,0,s)
    ss = (d1-d2)/d3
    result = ( '(%s - %s) ÷ %s , = ,'% (d1,d2,d3))
    return result,ss

def sub_div_2():
    d2,d3,s = rand_div()
    d1 = random.randint(32,98)
    ss = d1-d2/d3
    result = ( '%s - %s ÷ %s , = ,'% (d1,d2,d3))
    return result,ss

def plus_div():
    d2,d3,s = rand_div()
    d1 = random.randint(32,81)
    ss = d1+d2/d3
    result = ( '%s + %s ÷ %s , = ,'% (d1,d2,d3))
    return result,ss

def plus_sub():
    d1 = random.randint(41,67)
    d2 = random.randint(11,33)
    d3 = random.randint(13,52)
    ss = d1+d2-d3
    result = ( '%s + %s - %s , = ,'% (d1,d2,d3))
    return result,ss

def plus_sub_2():
    ss = 101
    while ss > 100:
        d1 = random.randint(21,47)
        d2 = random.randint(65,97)
        d3 = random.randint(23,52)
        ss = d1+(d2-d3)
    result = ( '%s + (%s - %s) , = ,'% (d1,d2,d3))
    return result,ss

def plus_mul():
    ss = 101
    while ss > 100:
        d2,d3,s = rand_mul()
        d1 = random.randint(11,90)
        ss = d1+d2*d3
    result = ( '%s + %s x %s , = ,'% (d1,d2,d3))
    return result,ss

def sub_mul():
    ss = 101
    while ss > 100:
        d2,d3,s = rand_mul()
        d1 = random.randint(52,99)
        if d1 >(d2*d3):
            ss = d1-d2*d3
        else:
            pass
    result = ( '%s - %s x %s , = ,'% (d1,d2,d3))
    return result,ss

def sub_plus():
    ss = 101
    while ss > 100:
        d1 = random.randint(40,99)
        d2 = random.randint(29,40)
        d3 = random.randint(13,69)
        ss = d1-d2+d3
    result = ( '%s - %s + %s , = ,'% (d1,d2,d3))
    return result,ss

def sub_plus_2():
    ss = -1
    while ss < 0:
        d1 = random.randint(60,99)
        d2 = random.randint(29,81)
        d3 = random.randint(13,69)
        ss = d1-(d2+d3)
    result = ( '%s - (%s + %s) , = ,'% (d1,d2,d3))
    return result,ss



def make_tiku(tiku_path):
    file_path = tiku_path
    for filename in range (1,11):
        answer_list=[]
        question_list=[]
        type_list = [mul_div,div_mul,sub_div,sub_div_2,plus_div,plus_sub,plus_sub_2,plus_mul,sub_mul,sub_plus,sub_plus_2]
        for n in range(0,100):
            question,answer = random.choice(type_list)()
            question_list.append(question)
            answer_list.append(answer)
        #生成题库
        question_file = "Q-" + str(filename)+".csv"
        fo = open(file_path+question_file, "wb")
        fo.write( ",,姓名,,日期,,得分,,用时,,%s\n" % (question_file))
        for n in range(0,20):
            text = ","
            for m in range(0,2):
                text = text + str(n+m*20+1)+","+str(question_list[n+m*20])+","
            fo.write( text +"\n")
        fo.close()
        #生成答案
        answer_file = "A-" + str(filename)+".csv"
        fo = open(file_path+answer_file, "wb")
        fo.write( ",,,,,answer,%s\n" %(filename))
        for n in range(0,20):
            text = ","
            for m in range(0,2):
                text = text + str(n+m*20+1)+","+str(answer_list[n+m*20])+","+","
            fo.write( text +"\n")



if __name__ == '__main__':
    #print "main"
    #function(a,b)
    #for n in range(1,11):
        # mul_div()
        # div_mul()
        # sub_div()
        # sub_div_2()
        # plus_div()
        # plus_sub()
        # plus_sub_2()
        # plus_mul()
        # sub_mul()
        # sub_plus()
        # sub_plus_2()
        # output_10()
    #   print n+90
    #   n =n +1 
    print tiku_path
    make_tiku(tiku_path)

