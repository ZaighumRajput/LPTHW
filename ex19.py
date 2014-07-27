#we define a function that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# a print statement
print "We can just give the function numbers directly:"

#call the function we defined above
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"

#define two variables
amount_of_cheese = 10
amount_of_crackers = 50

#call the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
#call the function, but the arguments are expressions that can be evaluated
cheese_and_crackers(10+20, 5 + 6)


print "And we can combine the two, variables and math:"
#call the function, but the arguments are expressions that can be evaluated
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers + 1000)


def black(*args):
    arg1 = args
    print "a %d" % arg1

black(1)
black(2)
amount_f = 2
black(amount_f)
black(amount_of_crackers )
black(amount_f + amount_of_crackers)
black(amount_f + 1)
black(amount_f + amount_of_crackers + amount_f)
black(amount_f + 2 + 3)
