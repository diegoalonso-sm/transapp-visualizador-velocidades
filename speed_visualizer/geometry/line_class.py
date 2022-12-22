import math

from speed_visualizer.geometry.point_class import Point


class Line:
    def __init__(self, pa: Point, pb: Point):
        self.a = pa
        self.b = pb
        self.length = self.a.distance(self.b)

    def distances(self, p: Point):
        """
        This method return 2 values.
        The first one corresponds to the distance between de point P and its projection to the segment AB
        The second corresponds to the distance from the start of th segment (point A) to the aforementioned projection
        """
        segment_length = self.length
        distance_a = p.distance(self.a)
        distance_b = p.distance(self.b)

        sides = [segment_length, distance_b, distance_a]
        sides.sort()

        obtuse_check = (math.pow(sides[0], 2) + math.pow(sides[1], 2)) < math.pow(sides[2], 2)

        # This checks that the projection of the stop to the segment IS in the segment or not
        if not obtuse_check or (sides[2] == segment_length):
            # using heron's formula we get the distance from the stop to the segment
            s = (segment_length + distance_a + distance_b) / 2
            a = math.sqrt(s * (s - distance_a) * (s - distance_b) * (s - segment_length))
            stop_distance = (a * 2) / segment_length

            # using pitagoras we get the distance form the start of the segment to the point
            # projection. The abs() in the equation is there to prevent a math domain error
            # that may happen due to decimal precision
            return stop_distance, math.sqrt(abs(math.pow(distance_a, 2) - math.pow(stop_distance, 2)))
        else:
            # the projection is outside the segment, the distance is the min distance to one of the segment ends,
            # the second value is either 0 if the projection is point A,
            # or the segment length if the projection is the point B
            min_d = min(distance_a, distance_b)
            if min_d == distance_a:
                return distance_a, 0
            else:
                return distance_b, segment_length


class Segment(Line):
    def __init__(self, pa: Point, pb: Point, prev_distance, sequence):
        super(Segment, self).__init__(pa, pb)
        self.prev_distance = prev_distance
        self.sequence = sequence

    def en_route_distances(self, p: Point):
        distance, projection = self.distances(p)
        projection += self.prev_distance
        return distance, projection

    def __str__(self):
        return f"{self.a} -> {self.b}, seq: {self.sequence}, prev_dist: {self.prev_distance}, length: {self.length}"

