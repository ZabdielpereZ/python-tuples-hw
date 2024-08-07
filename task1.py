from helper import d
# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should loop through the list of itineraries and print a formatted string for each. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be:


"Itinerary 1: Alice - From New York to London"
"Itinerary 2: Bob - From Tokyo to San Francisco"
d()

def flight_itin(itineraries,):
    for i, (traveler_name, origin, destination) in range(len(itineraries)):
        itineraries[i] = [traveler_name, origin, destination]
        print(f"Itinerary {i+1}: {traveler_name} - From {origin} to {destination}")

itineraries = '''
Alice', 'New York', 'London'
Bob', 'Tokyo', 'San Francisco'
print(flight_itin)
'''
print(itineraries)

# ^^^ can i get an explenation of what i did Here??  ^^^
d()

# i int      # enumerate default zero start
def flight_itin(itineraries,):
    for i, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        print(f"Itinerary {i}: {traveler_name} - From {origin} to {destination}")

itineraries = [
    ("Alice", "New York", "London"),
    ("Bob", "Tokyo", "San Francisco")
]

flight_itin(itineraries)

# itinerary1 = 'Alice', 'New York', 'London'
# itinerary2 = 'Bob', 'Tokyo', 'San Francisco'

#def flight_itin(itinerary1, itinerary2):
#    print(f'Itinerary 1: {itinerary1[0]} - From {itinerary1[1]} to {itinerary1[2]}')
#    print(f'Itinerary 2: {itinerary2[0]} - From {itinerary2[1]} to {itinerary2[2]}')
#(flight_itin(itinerary1, itinerary2))        # incorrect first try!

# https://realpython.com/python-enumerate/           
# https://sebhastian.com/typeerror-cannot-unpack-non-iterable-int-object/

# ^^^^ helpful website's! ^^^^  