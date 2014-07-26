# assigns a string to x
x = "There are %d types of people." % 10
# assigns a string
binary = "binary"
# assigns a string
do_not = "don't"
# assigns a string with formated variables
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#%r is
print "I said: %r." %x
print "I also said: '%s'." %y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e