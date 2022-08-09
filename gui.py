from tkinter import *
from tkinter import ttk
from embedded_test import animatePlanet
from orbitSimTestMenu import *
def menu():

    def inner_planets_callback():
        print(day.get() + month.get() + year.get())
        sim_inner_planets(year=year.get(),month=month.get(),day=day.get())

    def outer_planets_callback():
        sim_outer_planets(year=year.get(),month=month.get(),day=day.get())
    
    root = Tk()
    root.title("Test GUI")
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    mainframe = ttk.Frame(root, height=600, width=800, padding="8 6 100 100")
    subframe = ttk.Frame(mainframe)
    mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    mainStyle = ttk.Style()
    mainStyle.configure('DRK.TLabel',foreground="white", background="black")


    month = StringVar(mainframe, "")
    day = StringVar(mainframe,"")
    year = StringVar(mainframe, "")
    
    ttk.Label(mainframe, text="Year:").grid(column=1,row=1)
    ttk.Label(mainframe, text="Month:").grid(column=1,row=2)
    ttk.Label(mainframe, text="Day:").grid(column=1,row=3)

    ttk.Entry(mainframe, textvariable=year).grid(column=2, row=1)
    ttk.Entry(mainframe, textvariable=month).grid(column=2, row=2)
    ttk.Entry(mainframe, textvariable=day).grid(column=2, row=3)

    ttk.Label(mainframe, text="Welcome to Antikythera", font=50).grid(column=0,row=0,sticky=E)
    ttk.Button(mainframe, text="Inner Plannets (~3YR)", command=inner_planets_callback).grid(column=0,row=2,sticky=W)
    ttk.Button(mainframe, text="Outer Plannets (~200YR)", command=outer_planets_callback).grid(column=0,row=3,sticky=W)
    
    root.mainloop()

if __name__ == "__main__":
    menu()  