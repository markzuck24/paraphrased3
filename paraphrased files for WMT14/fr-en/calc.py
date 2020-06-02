import os
import time

# a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
a = [1,2,3,4,5,6,7,8]
# a=[1,2]
for i in a:
    f = open("b.txt", "a")
    f1 = open("b1.txt", "a")
    f2 = open("b2.txt", "a")
    f3 = open("b3.txt", "a")
    
    ss = str(i)+"\n"
    f.write(ss)
    f1.write(ss)
    f2.write(ss)
    f3.write(ss)
    
    time.sleep(5)
    fname = str(i)+'.txt'
    os.system("perl blu.pl r.txt < %s" % (fname))
    os.system("perl blu1.pl r.txt p1.txt < %s" % (fname))
    os.system("perl blu2.pl r.txt p1.txt p2.txt < %s" % (fname))
    os.system("perl blu3.pl r.txt p1.txt p2.txt p3.txt < %s" % (fname))
    time.sleep(1)