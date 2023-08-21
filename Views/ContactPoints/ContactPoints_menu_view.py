from tkinter import Canvas
from FrameComponents.ContactPoints import ContactPoints

class ContactPoints_menu_view:
    
    def __init__(self, master : Canvas, tk, cp) :
        self.master = master
        self.tk = tk
        self.cp = cp

        #functions for getting input text
        def save_seat_height(event):
            self.cp.bb_seat_distance = ent_seat_heigth.get()
            
        def save_bb_grip(event):
            self.bb_grip_distance = ent_bb_grip.get()
            
        def save_seat_grip(event):
            self.seat_grip_distance = ent_seat_grip.get()

        def save_seat_angle(event):
            self.seat_angle = ent_seat_angle.get()
            
        #Setting up menu frames
        frm_text = tk.Frame(master=self.master)
        frm_text.pack(side="left", fill="y")
        frm_input = tk.Frame(master=self.master)
        frm_input.pack(side="left", fill="y")

        #Seat heigth input
        lbl_bb_seat = tk.Label(master=frm_text, text="     Seat Height:")
        lbl_bb_seat.pack(padx=5, pady=7)

        ent_seat_heigth = tk.Entry(master=frm_input, width=4)
        ent_seat_heigth.insert(0, str(cp.bb_seat_distance))
        ent_seat_heigth.bind('<Return>', save_seat_height)
        ent_seat_heigth.pack(ipadx= 5, padx=5, pady=4)

        #bb to grip distance input
        lbl_bb_grip = tk.Label(master=frm_text, text="Standing reach:")
        lbl_bb_grip.pack(padx=5, pady=7)

        ent_bb_grip = tk.Entry(master=frm_input, width=4)
        ent_bb_grip.insert(0, str(cp.bb_grip_distance))
        ent_bb_grip.bind('<Return>', save_bb_grip)
        ent_bb_grip.pack(ipadx= 5, padx=5, pady=4)

        #seat to grip input
        lbl_seat_grip = tk.Label(master=frm_text, text="   Seated reach:")
        lbl_seat_grip.pack(padx=5, pady=7)

        ent_seat_grip = tk.Entry(master=frm_input, width=4)
        ent_seat_grip.insert(0, str(cp.seat_grip_distance))
        ent_seat_grip.bind('<Return>', save_seat_grip)
        ent_seat_grip.pack(ipadx= 5, padx=5, pady=4)

        #Seat angle input
        lbl_seat_angle = tk.Label(master=frm_text, text="       Seat angle:")
        lbl_seat_angle.pack(padx=5, pady=7)

        ent_seat_angle = tk.Entry(master=frm_input, width=4)
        ent_seat_angle.insert(0, str(cp.bb_seat_angle))
        ent_seat_angle.bind('<Return>', save_seat_angle)
        ent_seat_angle.pack(ipadx= 5, padx=5, pady=4)

        #Standing Reach angle (attack angle)
        lbl_seat_angle = tk.Label(master=frm_text, text="     attack angle:")
        lbl_seat_angle.pack(padx=5, pady=7)

        angle_bb_grip = cp.angle_bb_grip()

        lbl_seat_angle_output = tk.Label(master=frm_input, text=str(angle_bb_grip))
        lbl_seat_angle_output.pack(padx=5, pady=7)

        #Seated reach angle (seated attack angle)
        lbl_seat_angle = tk.Label(master=frm_text, text="Seated attack angle:")
        lbl_seat_angle.pack(padx=5, pady=7)

        angle_seat_grip = cp.angle_seat_grip()

        lbl_seat_angle_output = tk.Label(master=frm_input, text=str(angle_seat_grip))
        lbl_seat_angle_output.pack(padx=5, pady=7)

                