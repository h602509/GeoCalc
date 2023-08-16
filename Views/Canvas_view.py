class Canvas_view :
    
    def __init__(self, master, tk) :
        #Setting up drawing space
        tk.update()
        frm_canvas = tk.Frame(master=self.master, width = self.master.winfo_width() - self.master.frm_menu.winfo_width(), bg="yellow")
        frm_canvas.pack(side="right", fill="both", expand=True)
