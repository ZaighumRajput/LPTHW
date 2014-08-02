stuff = {'name':'Zed', 'age':39, 'height':6*12 +2}
print stuff['name']

print stuff['age']

print stuff['height']

stuff['city'] = "San Francisco"
print stuff['city']


stuff[1] = "Wow"

print stuff[1]

print stuff

del stuff[1]


# create a mapping of state to abbreviation

states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York': 'NY',
    'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-'*10
print "NY State has:", cities['NY']
print "OR State has:", cities['OR']

#print some states
print '*'*10
print "Michigan has:" ,cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]

#print every state abbreviation
print '*'*10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

print '*'*10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev]
    )

print '*'*10
#safely get a abbreviation by state that might not be there
state = states.get('Texas')
print state
if not state:
    print "Sorry, no Texas"

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX is: %s" % city
