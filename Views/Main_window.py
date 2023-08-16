from tkinter import Canvas
from FrameComponents.Bottombracket import Bottombracket
from FrameComponents.ContactPoints import ContactPoints
from Views.ContactPoints.ContactPoints_menu_view import ContactPoints_menu_view
from Views.ContactPoints.ContactPoints_canvas_view import ContactPoints_Canvas_view

class Main_window :

    def __init__(self, tk) :
        self.tk = tk
        scale = 0.8
        offset = get_canvas_offset()
        
        draw_contactpoints = False
        draw_outline = True
        draw_centerline = False
        
        color_cp = "00bbbb"
        color_bg = "black"
        color_outline = "#aaaaaa"
        color_centerline = "green"
        color_metal = "#707070"
        
        #Init window
        win_main = tk.Tk()
        win_main.geometry("1500x750")
        win_main.title("geoCalc")   
        
        #Setting up menu frame
        frm_menu = tk.Frame(master=win_main)
        frm_menu.pack(side="left", fill="y")
        
        #setting up canvas
        win_main.update()
        canvas = Canvas(master=win_main, width = win_main.winfo_width() - frm_menu.winfo_width(), bg=color_bg)
        canvas.pack(side="right", fill="both", expand=True)

        #Init ContactPoints
        cp = ContactPoints()
        
        #Init frame parts
        bb = Bottombracket(scale)
        
        #setting up menu
        ContactPoints_menu_view(frm_menu, tk, cp)
        
        #draw on canvas
        
        if draw_contactpoints:
            draw_contactpoints(color_cp)
        
        if draw_outline:
            draw_bb_outline(canvas, bb, color_outline, color_metal, color_bg, offset)
        
        if draw_centerline:
            pass
        
        tk.mainloop()

def get_canvas_offset():
    return (500, 500)

def draw_contactpoints(canvas: Canvas, cp: ContactPoints, color_cp):
    pass

def draw_bb_centerline(canvas: Canvas, bb: Bottombracket, color_centerline):
    pass

def draw_bb_outline(canvas : Canvas, bb: Bottombracket, color_outline, color_metal, color_bg, offset):
    outer_points = bb.points_bb_outline(offset)[0]
    inner_points = bb.points_bb_outline(offset)[1]
    
    canvas.create_oval(outer_points, outline= color_outline, fill= color_metal)
    canvas.create_oval(inner_points, outline= color_outline, fill= color_bg)
        
        