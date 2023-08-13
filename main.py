from FrameComponents.ContactPoints import ContactPoints
import tkinter as tk

from Views.ContactPoints.ContactPoints_menu_view import ContactPoints_menu_view
from Views.Main_window import Main_window



#init contactpoint

Main_window(tk)

"""

#Setting up drawing space
win_main.update()
frm_canvas = tk.Frame(master=win_main, width = win_main.winfo_width() - frm_text.winfo_width() - frm_input.winfo_width(), bg="black")
frm_canvas.pack(side="right", fill="both", expand=True)

"""

#Init mainloop
tk.mainloop()
