"""
This small snippet demonstrates the use of property
getter and setter to transparently create a property
with type checking.

Credit: Sean kelly from his Recover_from_Addiction.mov presentation
"""


# Here is a coordinate class
class Coordinate(object):
    def __init__(self, lat=0.0, lon=0.0):
        self.__lat, self.__lon = lat, lon

    def get_lat(self):
        return self.__lat

    def set_lat(self, lat):
        if not -90.0 <= lat <= 90.0:
            raise ValueError("Latitude is out of range (-90..90): %.4f" % lat)
        self.__lat = lat

    lat = property(get_lat, set_lat)


# main program

# This block of code is OK because the latitude is in range
# The output should be:
#   55.0

c = Coordinate()
c.lat = 55.0  # this statement works because of the property() above
print("latitude = %s" % c.lat)


# This block of code should raise an exception and crash
# because the latitude is out of range. We will not even reach
# the print statement.

c.lat = 90.001
print("latitude = %s" % c.lat)
