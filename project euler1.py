#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    n = n-1
    m3 = n//3
    m5 = n//5
    m15 = n//15
    s3= m3*((2*3)+(m3-1)*3)
    s3 = s3//2
    s5= m5*((2*5)+(m5-1)*5)
    s5 = s5//2
    s15= m15*((2*15)+(m15-1)*15)
    s15 = s15//2
    
   # print s5
    print (s3+s5-s15)
