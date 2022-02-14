from datetime import timedelta, datetime
# Defino mi función
def rocket_parts():
    return 'payload, propellant, structure'
output = rocket_parts()
print(output)
print(any([True, False, False]))
print(any([False, False, False]))
#print(any())

def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'

print(distance_from_earth('Moon'))
print(distance_from_earth('Saturn'))

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(238855, 75))

print(round(days_to_complete(238855, 75)))

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f'{destination} Arrival: %A %H:%M')


print(arrival_time('Moon'))
print(arrival_time('Orbit', hours=0.13))

def variable_length(*args):
    print(args)

variable_length()
variable_length('one', 'two')
variable_length(None)

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f'Total time to launch is {total_minutes} minutes'
    else:
        return f'Total time to launch is {total_minutes/60} hours'

print(sequence_time(4, 14, 18))
print(sequence_time(4, 14, 48))

def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day='Wednesday', pilots=3)

def crew_members(**kwargs):
    print(f'{len(kwargs)} astronauts assigned for this mission:')
    for title, name in kwargs.items():
        print(f'{title}: {name}')

crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', command_pilot='Michael Collins')