from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
from planets import solar_system
import time

def menu():
    root = Tk()
    root.title("Replicate Antikythera")
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    mainStyle = ttk.Style()
    mainStyle.configure('DRK.TLabel',foreground="white", background="black")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.columnconfigure(1, weight=1)
    mainframe.columnconfigure(2, weight=1)

    inputFrame = ttk.Labelframe(mainframe, relief="groove", padding="3", text="Simulation Parameters")
    inputFrame.grid(column=0, row=0, sticky="n")

    solSystem_Background = PhotoImage(file='backgroundSolid.png')
    solSystem_canvas = Canvas(mainframe, height=solSystem_Background.height(), width=solSystem_Background.width())
    solSystem_canvas.create_image(0, 0, image=solSystem_Background, anchor='nw')
    solSystem_canvas.grid(column=1, row=0, sticky="n")

    infoFrame = ttk.Labelframe(mainframe, relief="groove", padding="3", text="Relevant Events")
    infoFrame.grid(column=2, row=0, sticky="n")
    text = Text(infoFrame, width=20, height=20, state='disabled')
    text.grid(column=0, row=0,sticky="n")

    start_month = StringVar(mainframe, "1")
    start_day = StringVar(mainframe,"1")
    start_year = StringVar(mainframe, "2001")
    end_month = StringVar(mainframe, "1")
    end_day = StringVar(mainframe,"1")
    end_year = StringVar(mainframe, "2005")

    ttk.Label(inputFrame, text="Start Year:").grid(column=0,row=1)
    ttk.Label(inputFrame, text="Start Month:").grid(column=0,row=2)
    ttk.Label(inputFrame, text="Start Day:").grid(column=0,row=3)
    ttk.Separator(inputFrame, orient=HORIZONTAL).grid(column=0, row=4, columnspan=2)
    ttk.Label(inputFrame, text="End Year:").grid(column=0,row=5)
    ttk.Label(inputFrame, text="End Month:").grid(column=0,row=6)
    ttk.Label(inputFrame, text="End Day:").grid(column=0,row=7)
    ttk.Entry(inputFrame, textvariable=start_month).grid(column=1, row=1)
    ttk.Entry(inputFrame, textvariable=start_day).grid(column=1, row=2)
    ttk.Entry(inputFrame, textvariable=start_year).grid(column=1, row=3)
    ttk.Entry(inputFrame, textvariable=end_month).grid(column=1, row=5)
    ttk.Entry(inputFrame, textvariable=end_day).grid(column=1, row=6)
    ttk.Entry(inputFrame, textvariable=end_year).grid(column=1, row=7)

    root.mainloop()

if __name__ == "__main__":
    menu()  