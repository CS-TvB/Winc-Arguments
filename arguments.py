# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greetings = 'Hello, <name>!'):
    new_greet = greetings.replace('<name>', name)
    print (new_greet)
    return(new_greet)

def force(mass, body = "earth"):
    planets = {
    "sun": 274,
    "jupiter": 24.92,
    "neptune": 11.15,
    "saturn": 10.44,
    "earth": 9.798,
    "uranus": 8.87,
    "venus": 8.87,
    "mars": 3.71,
    "mercury": 3.7,
    "moon": 1.62,
    "pluto": 0.58
    }
    planet_graf = (planets[body])
    planet_graf_round = float(f'{planet_graf:.1f}')
    the_force = (float(mass)*planet_graf_round)
    print (the_force)
    return (the_force)

def pull(m1, m2, d):
    g = 6.674*(10**-11)
    f = (g*m1*m2)/(d**2)
    print (f)
    return(f)

#####################GREET#####################
name = 'Bob'
greetings = 'Hello, <name>!'
greet(name, greetings)

#####################FORCE#####################
mass = 0.1 #Apple
body = 'earth'
force(mass, body)

#####################Gravity#####################
m1 = 800
m2 = 1500
d = 3
pull(m1, m2, d)
