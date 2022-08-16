from cProfile import run
from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
from planets import solar_system
import Orbit
import time
import numpy as np

def remap( x, oMin, oMax, nMin, nMax ):

    #range check
    if oMin == oMax:
        return None

    if nMin == nMax:
        return None

    #check reversed input range
    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    #check reversed output range
    reverseOutput = False   
    newMin = min( nMin, nMax )
    newMax = max( nMin, nMax )
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result

def menu():
    global current_animation_time
    global start_animation_time
    global end_animation_time
    global runAnimation
    runAnimation = False

    def startAnimation():
        global runAnimation
        global current_animation_time
        global end_animation_time
        current_animation_time = datetime(int(start_year.get()), int(start_month.get()), int(start_day.get()))
        end_animation_time = datetime(int(end_year.get()), int(end_month.get()), int(end_day.get()))
        runAnimation = True
        root.after(100, animation)

    def pauseAnimation():
        global runAnimation
        runAnimation = False

    def animation():
        global current_animation_time
        global end_animation_time
        global runAnimation
        current_animation_time = current_animation_time + timedelta(int(stepsize.get()))
        if current_animation_time > end_animation_time:
            runAnimation = False
            return

        silder.set(remap(current_animation_time.timestamp(), start_animation_time.timestamp(), end_animation_time.timestamp(), 0, 1000))
        move_planets(current_animation_time)
        simulation_currentData_Label.configure(text=str(current_animation_time))

        if runAnimation:
            root.after(100, animation)

    def sliderUpdate(newVal):
        global start_animation_time
        global end_animation_time
        global current_animation_time
        global runAnimation
        current_animation_time = datetime(int(start_year.get()), int(start_month.get()), int(start_day.get()))
        end_animation_time = datetime(int(end_year.get()), int(end_month.get()), int(end_day.get()))
        timefromslider = datetime.fromtimestamp(remap(float(newVal), 0, 1000, start_animation_time.timestamp(), end_animation_time.timestamp()))
        current_animation_time = timefromslider
        simulation_currentData_Label.configure(text=str(timefromslider))

        move_planets(timefromslider)

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
           orient = HORIZONTAL, length=solSystem_Background.width(), command=sliderUpdate)
    silder.grid(column=1, row=3, sticky="s")

    simulation_currentData_Label = ttk.Label(mainframe, text = "Press play to start simulation")
    simulation_currentData_Label.grid(column=1, row=2)

    #Create a frame for the pause and play buttons
    controlsFrame = ttk.Frame(mainframe)
    controlsFrame.grid(column=1, row=1)

    pauseSim_button = Button(controlsFrame, text="Pause", command=pauseAnimation)
    pauseButton_img = PhotoImage(file="pausebutton.png")
    pauseButton_img = pauseButton_img.subsample(16,16) #make the button smaller (512/16 = 32)
    pauseSim_button.config(image=pauseButton_img)
    pauseSim_button.grid(column=1, row=0)

    startSim_button = Button(controlsFrame, text="Play", command=startAnimation)
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
    stepsize = StringVar(mainframe, "30")

    planets = []
    min10 = np.log10(2.7e7) #minimum distance at the center of the plot set to 27,000,000km
    max10 = np.log10(1.496e+10)
    start_animation_time = datetime(int(start_year.get()), int(start_month.get()), int(start_day.get()))
    current_animation_time = start_animation_time
    end_animation_time = datetime(int(end_year.get()), int(end_month.get()), int(end_day.get()))

    for body in solar_system:
        x,y,z = body.orbit.get_pos_at_date(current_animation_time)
        x = x * 1.496e+8 #convert from au to km
        y = y * 1.496e+8 #convert from au to km

        if x < 0:
            x = np.log10(abs(x))
            x = x - min10
            x = x * -1
        else:
            x = np.log10(x)
            x = x - min10

        if y < 0:
            y = np.log10(abs(y))
            y = y - min10
            y = y * -1
        else:
            y = np.log10(y)
            y = y - min10

        x = remap(x, (max10 - min10) * -1, max10 - min10, 100, solSystem_Background.width() - 100)
        y = remap(y, (max10 - min10) * -1, max10 - min10, 0, solSystem_Background.height())

        planets.append(solSystem_canvas.create_oval(x,y,x + body.draw_size,y+body.draw_size,fill=body.color))
    solSystem_canvas.update()
    
    def move_planets(day):
        for i in range(len(solar_system)):
            x,y,z = solar_system[i].orbit.get_pos_at_date(day)
            x = x * 1.496e+8 #convert from au to km
            y = y * 1.496e+8 #convert from au to km
            if x < 0:
                x = np.log10(abs(x))
                x = x - min10
                x = x * -1
            else:
                x = np.log10(x)
                x = x - min10

            if y < 0:
                y = np.log10(abs(y))
                y = y - min10
                y = y * -1
            else:
                y = np.log10(y)
                y = y - min10

            x = remap(x, (max10 - min10) * -1, max10 - min10, 100, solSystem_Background.width() - 100)
            y = remap(y, (max10 - min10) * -1, max10 - min10, 0, solSystem_Background.height())
            solSystem_canvas.moveto(planets[i], x,y)
        solSystem_canvas.update()

    ttk.Label(inputFrame, text="Start Month:").grid(column=0,row=1)
    ttk.Label(inputFrame, text="Start Day:").grid(column=0,row=2)
    ttk.Label(inputFrame, text="Start Year:").grid(column=0,row=3)
    ttk.Separator(inputFrame, orient=HORIZONTAL).grid(column=0, row=4, columnspan=2)
    ttk.Label(inputFrame, text="End Month:").grid(column=0,row=5)
    ttk.Label(inputFrame, text="End Day:").grid(column=0,row=6)
    ttk.Label(inputFrame, text="End Year:").grid(column=0,row=7)
    ttk.Label(inputFrame, text="Step Size (days):").grid(column=0,row=8)
    ttk.Entry(inputFrame, textvariable=start_month).grid(column=1, row=1)
    ttk.Entry(inputFrame, textvariable=start_day).grid(column=1, row=2)
    ttk.Entry(inputFrame, textvariable=start_year).grid(column=1, row=3)
    ttk.Entry(inputFrame, textvariable=end_month).grid(column=1, row=5)
    ttk.Entry(inputFrame, textvariable=end_day).grid(column=1, row=6)
    ttk.Entry(inputFrame, textvariable=end_year).grid(column=1, row=7)
    ttk.Entry(inputFrame, textvariable=stepsize).grid(column=1, row=8)

    root.mainloop()

if __name__ == "__main__":
    menu()  
