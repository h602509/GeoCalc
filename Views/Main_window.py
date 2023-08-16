from tkinter import Canvas
from FrameComponents.ContactPoints import ContactPoints
from Views.ContactPoints.ContactPoints_menu_view import ContactPoints_menu_view
from Views.ContactPoints.ContactPoints_canvas_view import ContactPoints_Canvas_view

class Main_window :
    
    def __init__(self, tk) :
        self.tk = tk
        scale = 0.8
        self.bg_color = "black"
        
        #Init window
        win_main = tk.Tk()
        win_main.geometry("1500x750")
        win_main.title("geoCalc")   
        
        #Setting up menu frame
        frm_menu = tk.Frame(master=win_main)
        frm_menu.pack(side="left", fill="y")
        
        #setting up canvas
        win_main.update()
        frm_canvas = tk.Frame(master=win_main, width = win_main.winfo_width() - frm_menu.winfo_width(), bg=self.bg_color)
        frm_canvas.pack(side="right", fill="both", expand=True)

        #Init ContactPoints
        cp = ContactPoints()
        
        #setting up menu
        ContactPoints_menu_view(frm_menu, tk, cp)
        
        #setting up canvas
        ContactPoints_Canvas_view(frm_canvas, tk, cp, scale, self.bg_color)
        
        tk.mainloop()
    
        
        