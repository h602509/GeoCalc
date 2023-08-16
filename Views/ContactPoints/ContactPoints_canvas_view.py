import tkinter as tk
from tkinter import Canvas
from FrameComponents.ContactPoints import ContactPoints

class ContactPoints_Canvas_view:
    
    def __init__(self, master, tk, cp, scale, bg_color):
        self.master = master
        self.tk = tk
        self.cp = cp
        self.scale = scale
        
        self.bg_color = bg_color
        self.color = "green"
        self.canvas = Canvas(master=self.master, bg="black")
        
        self.offset_x = 500 * self.scale
        self.offset_y = self.cp.bb_seat_distance * self.scale
        self.seat_x = self.offset_x + self.cp.pos_seat().x * self.scale
        self.seat_y = self.offset_y - self.cp.pos_seat().y * self.scale
        self.grip_x = self.offset_x + self.cp.pos_grip().x * self.scale
        self.grip_y = self.offset_y - self.cp.pos_grip().y * self.scale
        

        
        
        self.draw()
        
        self.canvas.pack(side="right", fill="both", expand="true",)
        
    def draw(self): 
        self.draw_guide_lines()
        #self.draw_bb()
        
    def draw_guide_lines(self):
        self.canvas.create_line(self.offset_x, self.offset_y
                                , self.seat_x, self.seat_y
                                , self.grip_x, self.grip_y
                                , self.offset_x, self.offset_y
                                , fill=self.color, dash=(6,10))
        
    def draw_bb(self):
        radius = 20
        self.canvas.create_oval(self.offset_x - radius
                                , self.offset_y - radius
                                , self.offset_x + radius
                                , self.offset_y + radius
                                , fill=self.bg_color)