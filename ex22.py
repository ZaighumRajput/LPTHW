'''
print - writes to console
 # is for comments
 + addition (depends on type)
 - subtracts (ints and floats?)
 / divide does not ensure float division unles the arguments are floats.
 * multiply
 % modulus, returns the remainder if ints

 also used in print statements to tell formattings and insert expression inside strings 

 < less-than returns boolean
 > greater-than
 <= less-than-equal
 greater-than-equal

 = assignment operator

 %s 
 %r raw
 %d decimal 
 %f float

 \n newline
 round() rounds number
 , separate variables in a list?


 \ escape character if the thing followed by \ is special and will mess things up, this prevents that 
 
 \t tabe

 raw_input() takes things from console

 pydoc python documentations

argv- comes from sys
takes the input from command line and puts them into a list
these can later be unpacked by => a1, a2 = argv

open : retruns a file object
syntac f = open('filename', 'mode')
mode can be r, w, a, r+

a fileobject has a few commands 

fileobject.read(size); reads the file

f.readline(); reads the first line
pythonic way of looping: 
    for line in f:
        print line,

f.close() save and closes?
f.truncate ?

import: loads modules into the current program

def: start a function with

+= : add and assign

func(args): how to call a function
*args if you don't know how many arguments the function might take
 
 '''