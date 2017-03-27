#!/usr/bin/python
import sys,os
import pickle
import subprocess


#######################################################################################
####             Define consts 
#######################################################################################

L_value   = 12
CMD       = './2x2_c'
TurnStr   = ('R','U','F',"R'","U'","F'","R2","U2","F2")
color     = { 'r'  :0, 'o'     :1, 'g'    :2, 'b'   :3, 'w'    :4, 'y'     :5,
            'red':0, 'orange':1, 'green':2, 'blue':3, 'white':4, 'yellow':5,
            'black': 4, 'purple': 1, 'p':1 
}

#######################################################################################
#######          Input Start State 
#######################################################################################
os.system("clear")
print """\n>>>>>>> Hello, I'll try to solve a 2x2 rubik puzzle. 
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

COLORS:  Red(r)  Orange(o)  Green(g)  Blue(b)  White(w)  Yellow(y)  Purple(p)  Black
         Use blank to seperate them. '''

Please put you 2x2 rubik cube on desktop, and tell me its state.
"""

try:
    if len(sys.argv)>1 and os.path.isfile(sys.argv[1]):
        a = pickle.load(open(sys.argv[1],'r'))
    else:
        a=range(24)
        line=raw_input("    >>> The color of 0,1,2,3 in the graph:")
        a[0],a[1],a[2],a[3]=line.split()
        line=raw_input("    >>> The color of 8,9,10,11 in the graph:")
        a[8],a[9],a[10],a[11]=line.split()
        line=raw_input("    >>> The color of 4,5,6,7 in the graph:")
        a[4],a[5],a[6],a[7]=line.split()
        line=raw_input("    >>> The color of 20,21,22,23 in the graph:")
        a[20],a[21],a[22],a[23]=line.split()
        line=raw_input("    >>> The color of 12,13,14,15 in the graph:")
        a[12],a[13],a[14],a[15]=line.split()
        line=raw_input("    >>> The color of 16,17,18,19 in the graph:")
        a[16],a[17],a[18],a[19]=line.split()
        pickle.dump(a, open('last_input',"w"))
    try:
        cube=range(24)
        for _ in range(24):
            cube[_]=color[a[_].lower()]
    except:
        print "  ##### ERROR, I don't know the color %s"%a[_]
        sys.exit()
except:
    print "  ##### Input ERROR #####"
    sys.exit()

#######################################################################################
#######            Solve  
#######################################################################################

cmd_str=[CMD,]+[str(x) for x in cube]
print "\n  >>>>>  Solving , please wait ..."
print "\n  >>>>>  %s"%(" ".join(cmd_str))
output=subprocess.Popen(cmd_str,stdout=subprocess.PIPE)
pstdout,pstderr=output.communicate()
print pstdout

for line in pstdout:
    if "MORE" in line:
        step=line.split()[1]
        print "  >>>>>  %s steps is not possible"%step
        sys.stdout.flush()
    elif "OK" in line:
        step=line.split()[1]
        print "  >>>>>  Found a solution of %s steps :"%step
        sys.stdout.flush()
    elif "SEQ" in line:
        print "  >>>>>  Solvation : ",
        seq=line.split()[1:]
        for i in seq:
            print TurnStr[int(i)],
print "\n  >>>>>  Done."

