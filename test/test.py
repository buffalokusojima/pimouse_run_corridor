#!/usr/bin/env python
if __name__ == '__main__':
    with open("/dev/rtlightsensor0","w") as f:
        f.write("%d %d %d %d\n" % (400,100,100,0))

#    with open("/dev/rtmotor_raw_l0", "r") as lf, open("/dev/rtmotor_raw_r0","r"):
#        left = int(lf.readline().rstrip())
#        right = int(rf.readline().rstrip())
