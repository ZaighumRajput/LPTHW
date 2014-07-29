people = 30
cars = 30
buses = 15

if cars > people:
    print "We should take the cars."

elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."


#checks if buses is greater than car,
#if so it prints
#if not it goes and chceck the elif statement
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."


#checks if people an integer is greater than buses.
#if so it exists the print statement
#if not it goes on the statement under the else statement
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."


