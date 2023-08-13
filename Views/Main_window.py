from Views.ContactPoints.ContactPoints_menu_view import ContactPoints_menu_view


class Main_window :
    
    def __init__(self, tk) :
        self.tk = tk
        
        #Init window
        win_main = tk.Tk()
        win_main.geometry("750x500")
        win_main.title("geoCalc")   
        
        #Setting up menu frame
        frm_menu = tk.Frame(master=win_main, bg="red")
        frm_menu.pack(side="left", fill="y")
        
        #Setting up drawing space
        win_main.update()
        frm_canvas = tk.Frame(master=win_main, width = win_main.winfo_width() - frm_menu.winfo_width() - frm_menu.winfo_width(), bg="black")
        frm_canvas.pack(side="right", fill="both", expand=True)
        
        #setting up menu
        ContactPoints_menu_view(frm_menu, tk)
        
        tk.mainloop()