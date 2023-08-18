from math import cos, sin, atan, degrees, radians
from Utils.Point import Point
from Utils.Geometry_helper import Geometry_helper

class ContactPoints :
    
    # Deafult values are measured from the klein pulse with the old syncros bars
    def __init__ (self, bb_grip_distance = 810, bb_seat_distance = 730
                  , seat_grip_distance = 720, bb_seat_angle = 73):
        self.bb_grip_distance = bb_grip_distance
        self.seat_grip_distance = seat_grip_distance
        self.bb_seat_distance = bb_seat_distance
        self.bb_seat_angle = bb_seat_angle
    
    staticmethod
    def pos_grip(self):
        pos_bb = (0,0)
        return Geometry_helper.circle_intersection(pos_bb, 
                                                   self.bb_grip_distance, 
                                                   self.pos_seat(), 
                                                   self.seat_grip_distance)
    
    def pos_seat(self):
        x = self.bb_seat_distance * cos(radians(180 - self.bb_seat_angle))
        y = self.bb_seat_distance * sin(radians(180 - self.bb_seat_angle))
        return (x,y)

    def distance_seat_grip(self):
        delta_x = self.pos_grip()[0] - self.pos_seat()[0]
        delta_y = self.pos_grip()[1] - self.pos_seat()[1]
        
        distance = (delta_x**2 + delta_y**2)**0.5
        return distance
    
    def angle_seat_grip(self):
        delta_x = self.pos_grip()[0] - self.pos_seat()[0]
        delta_y = self.pos_grip()[1] - self.pos_seat()[1]
        
        angle = degrees(atan(delta_y / delta_x))
        return angle

    def angle_bb_grip(self):
        pos_grip = self.pos_grip()
        
        angle = degrees(atan(pos_grip[0] / pos_grip[1]))
        return angle
    
    def points_cp_offset(self, offset):
        seat_offset = (self.pos_seat()[0] + offset[0], - self.pos_seat()[1] + offset[1])
        grip_offset = (self.pos_grip()[0] + offset[0], - self.pos_grip()[1] + offset[1])
        return (offset, seat_offset, grip_offset, offset)