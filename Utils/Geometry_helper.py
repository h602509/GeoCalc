import math

from Utils.Point import Point


class Geometry_helper:
    
    @staticmethod
    def circle_intersection(c1, r1, c2, r2):
        dx, dy = c2[0]-c1[0], c2[1]-c1[1]
        d = math.sqrt(dx*dx + dy*dy)
        if d > r1 + r2:
            return "The circles do not intersect"
        elif d < abs(r1-r2):
            return "One circle is contained within the other"
        elif d == 0 and r1 == r2:
            return "The circles are identical and there are an infinite number of intersection points"

        a = (r1*r1 - r2*r2 + d*d) / (2*d)
        h = math.sqrt(r1*r1 - a*a)
        x3 = c1[0] + a*(c2[0]-c1[0])/d
        y3 = c1[1] + a*(c2[1]-c1[1])/d
        rx = -(c2[1]-c1[1])*(h/d)
        ry = (c2[0]-c1[0])*(h/d)

        xi1 = x3 + rx
        xi2 = x3 - rx
        yi1 = y3 + ry
        yi2 = y3 - ry


        if xi1 > xi2:
            return (xi1, yi1)

        else:
            return (xi2, yi2)
            