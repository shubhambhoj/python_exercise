# Create a mapping of state to abbreviation
states = {
    'Maharashatra':'MH',
    'Utter Pradesh':'UP',
    'Haryana':'HR',
    'Madhya Pradesh':'MP',
    'Karnataka':'KR'
}

# Create a basic set of states and some cities in them
cities = {
    'MH':'Mumbai',
    'UP':'Waranasi',
    'KR':'Bengalor'
}

# Add some more cities
cities['MP'] = 'Jaipur'
cities['HR'] = 'Chandigarh'

# Print out some cities
print('_'*10)
print("MH State has :",cities['MH'])
print("HR State has :",cities['HR'])

# Print some states
print("_"*10)
print("Karnataka's abbreviation is: ",states['Karnataka'])
print("Utter Pradesh's abbreviation is: ",states['Utter Pradesh'])

# Do it by using the state then cities dict.
print("_"*10)
print("Madhya Pradesh has: ",cities[states["Madhya Pradesh"]])
print("Haryana has: ",cities[states["Haryana"]])

# print every state abbreviation
print("_"*10)
for state,abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# Print every city in state
print("_"*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time 
print("_"*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreciated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("_"*10)
# safely get a abbreviation by state that might not be there

state = states.get('Tamilnadu')

if not state:
    print("Sorry,no Tamilnadu")

# get a city with a default value
city = cities.get('TN','Does Not Exist') 
print(f"The city for the state 'TN' is: {city}")   