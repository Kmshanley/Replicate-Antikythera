from tkinter import *
from tkinter import ttk
from embedded_test import animatePlanet
def menu():
    root = Tk()
    root.title("Test GUI")

    mainStyle = ttk.Style()
    mainStyle.configure('My.TFrame',background = "black")

    mainframe = ttk.Frame(root, height=600, width=800, padding="8 6 100 100", style="My.TFrame")
    subframe = ttk.Frame(mainframe)
    mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="Welcome to Antikythera", font=25, foreground="red", background="black").grid(column=0,row=0,sticky=E)
    ttk.Button(mainframe, text="Earth & Moon", command=lambda: animatePlanet()).grid(column=0,row=2,sticky=W)
    
    root.mainloop()

if __name__ == "__main__":
    menu()  