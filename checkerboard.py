# pylint: disable=print-statement

for row in range(0,8):
    if row % 2 == 0:
        print "* * * * "
    elif row % 2 != 0:
        print " * * * *"