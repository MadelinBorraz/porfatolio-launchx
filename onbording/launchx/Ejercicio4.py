fact = 'The Moon has no atmosphere.'
fact + 'No sound can be heard on the Moon.'
print(fact)
two_facts = fact + 'No sound can be heard on the Moon.'

print(two_facts)

moon_radius = 'The "near side" is the part of the Moon that faces the Earth'
print(moon_radius)

multiline = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline)

heading = 'temperatures and facts about the moon'
print(heading.title())

temperatures = '''Daylight: 260 F
... Nighttime: -280 F'''
print(temperatures .split())
print(temperatures .split('\n'))

#buscar cadenas
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
print(temperatures.find('Mars'))

#c
print('Lower: ',temperatures.lower())
print('Upper: ',temperatures.upper())
#combinar contenido
temperatures = 'Mars Average Temperature: -60 C'
parts = temperatures.split(':')
print('Combinar: ',parts)

mass_percentage = '1/6'
print('On the Moon, you would weigh about %s of your weight on Earth' % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight,
    but only one side is seen from %s because
    the %s rotates around its own axis when it orbits %s.""" % ('Moon', 'Earth', 'Moon', 'Earth'))
mass_percentage = '1/6'
print('On the Moon, you would weigh about {} of your weight on Earth'.format(mass_percentage))

print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))
print(f'On the Moon, you would weigh about {mass_percentage} of your weight on Earth')
print(round(100/6, 1))
print(f'On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth')
