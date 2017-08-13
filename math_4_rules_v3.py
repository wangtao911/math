#! /usr/bin/python
# coding: utf-8
"""
    See README.md
    --------------------------------
    create by wangtao   yyyy.mm.dd
"""
#reload(sys)
#sys.setdefaultencoding('utf-8')

import sys
import os
import commands
import random 
from setting import *
from user_setting import *

from base_4_rules import *
from make_sub_plus_with_min_max import *
from make_tiku import *


if __name__ == '__main__':
    print "min is " + str(min)
    print "max is " + str(max)
    print "tiku_path is " + tiku_path
    print "This math V3"
    make_tiku(tiku_path)

