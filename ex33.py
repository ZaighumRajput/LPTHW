
def numberLoop(loopCount, increment):
    '''prints the construction of a list up to the given number '''
    i = 0
    numbers = []

    while i < loopCount:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i


def numberForLoop(loopCount, increment):
    '''implements the same thing as above but using a for loop instead of a while loop'''
    numbers = []
    for i in range(0,loopCount, increment):
        print "At the top i is %d" % i

        numbers.append(i)

        print "Numbers now:", numbers
