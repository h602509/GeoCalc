import math

from Utils.Point import Point


class Geometry_helper:
    
    @staticmethod
    def circle_intersection(c1, r1, c2, r2):
        dx, dy = c2.x-c1.x, c2.y-c1.y
        d = math.sqrt(dx*dx + dy*dy)
        if d > r1 + r2:
            return "The circles do not intersect"
        elif d < abs(r1-r2):
            return "One circle is contained within the other"
        elif d == 0 and r1 == r2:
            return "The circles are identical and there are an infinite number of intersection points"

        a = (r1*r1 - r2*r2 + d*d) / (2*d)
        h = math.sqrt(r1*r1 - a*a)
        x3 = c1.x + a*(c2.x-c1.x)/d
        y3 = c1.y + a*(c2.y-c1.y)/d
        rx = -(c2.y-c1.y)*(h/d)
        ry = (c2.x-c1.x)*(h/d)

        xi1 = x3 + rx
        xi2 = x3 - rx
        yi1 = y3 + ry
        yi2 = y3 - ry


        if xi1 > xi2:
            return Point(xi1, yi1)

        else:
            return Point(xi2, yi2)
            