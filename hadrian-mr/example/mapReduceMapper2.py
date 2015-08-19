from antinous import *

input = {"type":"record","name":"Star","fields":[{"name":"name","type":"string","doc":"Name of the host star"},{"name":"ra","type":["double","null"],"doc":"Right ascension of the star in our sky (degrees, J2000)"},{"name":"dec","type":["double","null"],"doc":"Declination of the star in our sky (degrees, J2000)"},{"name":"mag","type":["double","null"],"doc":"Magnitude (dimness) of the star in our sky (unitless)"},{"name":"dist","type":["double","null"],"doc":"Distance of the star from Earth (parsecs)"},{"name":"mass","type":["double","null"],"doc":"Mass of the star (multiples of our Sun's mass)"},{"name":"radius","type":["double","null"],"doc":"Radius of the star (multiples of our Sun's radius)"},{"name":"age","type":["double","null"],"doc":"Age of the star (billions of years)"},{"name":"temp","type":["double","null"],"doc":"Effective temperature of the star (degrees Kelvin)"},{"name":"type","type":["string","null"],"doc":"Spectral type of the star"},{"name":"planets","type":{"type":"array","items":{"type":"record","name":"Planet","fields":[{"name":"name","type":"string","doc":"Name of the planet"},{"name":"detection","type":{"type":"enum","name":"DetectionType","symbols":["astrometry","imaging","microlensing","pulsar","radial_velocity","transit","ttv","OTHER"]},"doc":"Technique used to make discovery"},{"name":"discovered","type":"string","doc":"Year of discovery"},{"name":"updated","type":"string","doc":"Date of last update"},{"name":"mass","type":["double","null"],"doc":"Mass of the planet (multiples of Jupiter's mass)"},{"name":"radius","type":["double","null"],"doc":"Radius of the planet (multiples of Jupiter's radius)"},{"name":"period","type":["double","null"],"doc":"Duration of planet's year (Earth days)"},{"name":"max_distance","type":["double","null"],"doc":"Maximum distance of planet from star (semi-major axis in AU)"},{"name":"eccentricity","type":["double","null"],"doc":"Ellipticalness of orbit (0 == circle, 1 == escapes star)"},{"name":"temperature","type":["double","null"],"doc":"Measured or calculated temperature of the planet (degrees Kelvin)"},{"name":"temp_measured","type":["boolean","null"],"doc":"True iff the temperature was actually measured"},{"name":"molecules","type":{"type":"array","items":"string"},"doc":"Molecules identified in the planet's atmosphere"}]}}}]}

output = record(key={"type": "record", "name": "CompositeKey", "fields": [{"name": "groupby", "type": "string"}, {"name": "sortby", "type": "double", "order": "descending"}]},
                value=record(name=string, mass=double, radius=double, max_distance=double))

class Value(object):
    def __init__(self, name, mass, radius, max_distance):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.max_distance = max_distance

def action(star):
    for planet in star.planets:
        if planet.mass is not None and planet.radius is not None and planet.max_distance is not None:
            emit({"key": {"groupby": star.name, "sortby": planet.max_distance},
                  "value": Value(planet.name, planet.mass, planet.radius, planet.max_distance)})