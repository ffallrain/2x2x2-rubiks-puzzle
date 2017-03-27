#!/usr/bin/python
import sys,os
import numpy as np
import random 

########### Several Function to make a move ###########
def four_swap(a,tu,r=False):
    if r:
        a[tu[0]],a[tu[1]],a[tu[2]],a[tu[3]]=a[tu[1]],a[tu[2]],a[tu[3]],a[tu[0]]
    else:
        a[tu[0]],a[tu[1]],a[tu[2]],a[tu[3]]=a[tu[3]],a[tu[0]],a[tu[1]],a[tu[2]]

def R(a,r=False):
    four_swap(a,(8,9,11,10),r=r)
    four_swap(a,(1,7,19,15),r=r)
    four_swap(a,(5,17,13,3),r=r)

def U(a,r=False):
    four_swap(a,(5,4,6,7),r=r)
    four_swap(a,(1,20,16,9),r=r)
    four_swap(a,(0,21,17,8),r=r)

def F(a,r=False):
    four_swap(a,(0,1,3,2),r=r)
    four_swap(a,(5,10,14,20),r=r)
    four_swap(a,(4,8,15,22),r=r)

def R_r(a):
    R(a,r=True)

def U_r(a):
    U(a,r=True)

def F_r(a):
    F(a,r=True)

Turn=[R,U,F,R_r,U_r,F_r]
TurnStr=('R','U','F',"R'","U'","F'")
Rev=[R_r,U_r,F_r,R,U,F]
Free=len(Turn)

########## A function to check whether solved the puzzle #########
def check(a):
    for i in (0,1,2,3,4,5):
        if not a[4*i+0]==a[4*i+1]==a[4*i+2]==a[4*i+3]:
            return False
    return True 

############ Solve it ! #############
L=L_value
path=[]
count=0
def run(cube):
    global path
    global count
    if check(cube):
        return True
    if len(path)>L:
        return False
    count+=1
    _=range(Free)
    random.shuffle(_)
    for i in _:
        path.append(i)
        Turn[i](cube)
        if run(cube):
            return True
        Rev[i](cube)
        path.pop()
    return False
