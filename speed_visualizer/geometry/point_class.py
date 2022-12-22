import math

earth_radius_km = 6373.0


class Point:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def distance(self, p):
        lat1 = math.radians(self.lat)
        lon1 = math.radians(self.lon)
        lat2 = math.radians(p.lat)
        lon2 = math.radians(p.lon)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = earth_radius_km * c
        return distance * 1000
        pass

    def __str__(self):
        return str(self.lat) + ", " + str(self.lon)


class StopPoint(Point):
    def __init__(self, lat, lon, stop_id):
        super(StopPoint, self).__init__(lat, lon)
        self.stop_id = stop_id
