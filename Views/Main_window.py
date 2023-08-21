from tkinter import Canvas
from FrameComponents.Bottombracket import Bottombracket
from FrameComponents.ContactPoints import ContactPoints
from Views.ContactPoints.ContactPoints_menu_view import ContactPoints_menu_view

class Main_window :

    offset : int

    def __init__(self, tk) :
        self.tk = tk
        scale = 0.8
        offset = get_canvas_offset()
        
        draw_cp = True
        draw_outline = True
        draw_centerline = False
        
        color_cp = "#009999"
        color_bg = "black"
        color_outline = "#aaaaaa"
        color_centerline = "#00ff00"
        color_metal = "#707070"
        
        dash_cp = (6, 10)
        
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
        if draw_outline:
            draw_bb_outline(canvas, bb, color_outline, color_metal, color_bg, offset)
        
        if draw_centerline:
            pass
        
        if draw_cp:
            draw_contactpoints(canvas, cp, color_cp, dash_cp, offset)
            
        tk.mainloop()
    

def draw_contactpoints(canvas: Canvas, cp: ContactPoints, color_cp, dash, offset):
    canvas.create_line(cp.points_cp_offset(offset), fill=color_cp, dash= dash)

def get_canvas_offset():
    return (500, 700)
    
def draw_bb_centerline(canvas: Canvas, bb: Bottombracket, color_centerline):
    pass

def draw_bb_outline(canvas : Canvas, bb: Bottombracket, color_outline, color_metal, color_bg, offset):
    outer_points = bb.points_bb_outline(offset)[0]
    inner_points = bb.points_bb_outline(offset)[1]
    
    canvas.create_oval(outer_points, outline= color_outline, fill= color_metal)
    canvas.create_oval(inner_points, outline= color_outline, fill= color_bg)
        
        