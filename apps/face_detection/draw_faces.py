#!/usr/bin/python

import subprocess
import sys

usage="draw_faces.py <input.jpg> <output.png>"

# check args
if len(sys.argv)!=3:
    print "usage",usage
    sys.exit(-1)

# run face detection
s=subprocess.check_output(["./build/release/face_detection", sys.argv[1]])

# build an imagemagick command
cmd="convert %s -fill none -strokewidth 3 " % sys.argv[1]
for i in s.splitlines():
    print i
    x=i.split()
    if len(x) != 5:
        print "can't parse output"
        sys.exit(-1)
    if x[0] == "face":
        cmd += ' -stroke red -draw "rectangle '
    elif x[0] == "eye":
        cmd += ' -stroke green -draw "rectangle '
    else:
        print "can't parse output"
        sys.exit(-1)
    cmd += '%s %s %s %s"' % (x[1],x[2],x[3],x[4])
cmd+=' ' + sys.argv[2]

# run the command
print "command=",cmd
r=subprocess.call(cmd, shell=True)

# check return
if r!=0:
    print "error running command"
    sys.exit(-1)
