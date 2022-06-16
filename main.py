# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting_temp="Hello, <name>!"):
    if name and "<name>" in greeting_temp:
        new_greeting = greeting_temp.replace("<name>", name)
        return new_greeting
    elif name and greeting_temp:
        return greeting_temp + name
    else:
        return greeting_temp


def force(mass, body="earth"):
    gravity_list = {
        "sun": 274.0,
        "jupiter": 24.9,
        "neptune": 11.1,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6
    }
    force = mass * gravity_list[body]
    return force


def pull(mass1, mass2, distance):
    pull = (6.674 * 10 ** -11) * ((mass1 * mass2) / distance ** 2)
    return pull
