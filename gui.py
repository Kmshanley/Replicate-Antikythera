from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
from planets import solar_system
import Orbit
import time
import numpy as np

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

    v1 = DoubleVar()
    silder = ttk.Scale(mainframe, variable = v1, 
           from_ = 0, to = 1000, 
           orient = HORIZONTAL, length=solSystem_Background.width())
    silder.grid(column=1, row=3, sticky="s")

    simulation_currentData_Label = ttk.Label(mainframe, text = "Press play to start simulation")
    simulation_currentData_Label.grid(column=1, row=2)

    #Create a frame for the pause and play buttons
    controlsFrame = ttk.Frame(mainframe)
    controlsFrame.grid(column=1, row=1)

    pauseSim_button = Button(controlsFrame, text="Pause")
    pauseButton_img = PhotoImage(file="pausebutton.png")
    pauseButton_img = pauseButton_img.subsample(16,16) #make the button smaller (512/16 = 32)
    pauseSim_button.config(image=pauseButton_img)
    pauseSim_button.grid(column=1, row=0)

    startSim_button = Button(controlsFrame, text="Play")
    playButton_img = PhotoImage(file="playbutton.png")
    playButton_img = playButton_img.subsample(16,16) #make the button smaller (512/16 = 32)
    startSim_button.config(image=playButton_img)
    startSim_button.grid(column=0, row=0)

    start_month = StringVar(mainframe, "1")
    start_day = StringVar(mainframe,"1")
    start_year = StringVar(mainframe, "2001")
    end_month = StringVar(mainframe, "1")
    end_day = StringVar(mainframe,"1")
    end_year = StringVar(mainframe, "2005")

    planets = []
    min10 = np.log10(2.7e7)
    for body in solar_system:
        date = datetime(int(start_year.get()), int(start_month.get()), int(start_day.get()))
        x,y,z = body.orbit.get_pos_at_date(date)
        r = np.hypot(x,y)
        r = np.log(r) - min10
        theta = np.rad2deg(np.arctan2(y,x))
        theta = np.radians(theta)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        x = (x + 425)
        y = (y + 325)
        planets.append(solSystem_canvas.create_oval(x,y,x+15,y+15,fill="blue"))
    solSystem_canvas.update()
    
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