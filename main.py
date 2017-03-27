#!/usr/bin/python
import sys,os
import numpy as np
import random 

L_value=10

########### Initialize the rubik cube ###########
cube=np.zeros((24,),int)
for i in range(24):
    cube[i]=i/4
print cube

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

########### Main ###############

####### Define Color ######
color={ 'r'  :0, 'o'     :1, 'g'    :2, 'b'   :3, 'w'    :4, 'y'     :5,
        'red':0, 'orange':1, 'green':2, 'blue':3, 'white':4, 'yellow':5,
        'black': 4, 'purple': 1, 'p':1 
}
colorstr='''COLORS:  Red(r)  Orange(o)  Green(g)  Blue(b)  White(w)  Yellow(y)  Purple(p)  Black
Note: Color black has no abbreviation. You have to type 'black'. while other colors can be short as on letter. 
>>>> For example. first four color could be : b r green black 
Use blank to seperate them. '''

definestr='''
  ##################  Define Cube  ##################
  #                                                 #
  #                 16  17                          #
  #                                                 #
  #                 18  19                          #
  #                                                 #
  #             6   7                               #
  #           4   5                                 #
  #     21                9                         #
  #  20      0   1     8       Front   0  1  2  3   #
  #     23               11    Right   8  9 10 11   #
  #  22      2   3    10       Up      4  5  6  7   #
  #                            Left   20 21 22 23   #
  #            12  13          Back   16 17 18 19   #
  #          14  15            Down   12 13 14 15   #
  #                                                 #
  ###################################################
'''


####### Input Start State #######
os.system("clear")
print "\n>>>>>>> Hello, I'll try to solve a 2x2 rubik puzzle. "
print definestr
print colorstr
print "Please put you 2x2 rubik cube on desktop, and tell me its state."

try:
    a=range(24)
    line=raw_input(">>> The color of Front 4 pieces (0,1,2,3 in the graph):")
    a[0],a[1],a[2],a[3]=line.split()
    line=raw_input(">>> The color of Right 4 pieces (8,9,10,11 in the graph):")
    a[8],a[9],a[10],a[11]=line.split()
    line=raw_input(">>> The color of Up 4 pieces (4,5,6,7 in the graph):")
    a[4],a[5],a[6],a[7]=line.split()
    line=raw_input(">>> The color of Left 4 pieces (20,21,22,23 in the graph):")
    a[20],a[21],a[22],a[23]=line.split()
    line=raw_input(">>> The color of Down 4 pieces (12,13,14,15 in the graph):")
    a[12],a[13],a[14],a[15]=line.split()
    line=raw_input(">>> The color of Back 4 pieces (16,17,18,19 in the graph):")
    a[16],a[17],a[18],a[19]=line.split()

    try:
        cube=range(24)
        for _ in range(24):
            cube[_]=color[a[_].lower()]
    except:
        print "##### ERROR, I don't know the color %s"%a[_]
        sys.exit()
except:
    print "##### Input ERROR #####"
    sys.exit()
    

####### solve  #######
print "\n>>>>>>>>>> Solving , please wait ..."
run(cube)

if len(path)!=0:
    print "\n>>>>>>>>>Solved, the move sequence:"
    for i in path:
        print TurnStr[i]," ",
    print ""

    print ">>>>>>> I've totally tried %d times\n"%count
    print """>>>>>>> ( Tips, but 'R','U','F', I mean the right, upper and front layer of the cube. a " ' " means anticlockwise. ) """
else:
    print "\n>>>>>>>>>> Sorry, I didn't solve the puzzle this time. You could try a larger L-value ( In top of source code ,defult 8 ) "
    print "\n>>>>>>>>>> But by trying that, this program will cost mounts of time "
