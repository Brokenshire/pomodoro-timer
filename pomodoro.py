"""
Simple pomodoro timer GUI application using tkinter.

Author: Jack Brokenshire
Date: 30/12/2019
Version: 1.0
"""

# Standard import
import time

# Third-party imports
import tkinter as tk
import tkinter.messagebox
from winsound import *


class Application(tk.Frame):
    """"Simple pomodoro timer application using tkinter."""
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.running = False
        self.pomodoro = True
        self.time = 15
        self.mins = 0
        self.secs = 0
        self.build_interface()

    def build_interface(self):
        """The interface function."""
        self.clock = tk.Label(self, text="25:00", font=("Courier", 20), width=10)
        self.clock.grid(row=0, column=1, stick="S")

        self.time_label = tk.Label(self, text="min sec", font=("Courier", 10), width=15)
        self.time_label.grid(row=1, column=1, sticky="N")

        self.power_button = tk.Button(self, text="Start", command=lambda: self.start())
        self.power_button.grid(row=2, column=0, sticky="NE")

        self.reset_button = tk.Button(self, text="Reset", command=lambda: self.reset())
        self.reset_button.grid(row=2, column=1, sticky="NW")

        self.quit_button = tk.Button(self, text="Quit", command=lambda: self.quit())
        self.quit_button.grid(row=2, column=3, sticky="NE")

        self.master.bind("<Return>", lambda: self.start())

    def calcualte(self):
        """Calcualtes the time"""
        self.mins, self.secs = divmod(self.time, 60)
        return "{:02d}:{:02d}".format(self.mins, self.secs)

    def timer(self):
        """Calculates the time to be displayed"""
        if self.running is True:
            if self.time <= 0:
                play = lambda: PlaySound("alert.wav", SND_FILENAME)
                if self.pomodoro is True:
                    self.timer = 300
                    self.clock.configure(text="05:00")
                    self.pomodoro = False
                else:
                    self.timer = 1500
                    self.clock.configure(text="25:00")
                    self.pomodoro = True
            else:
                self.clock.configure(text=self.calcualte())
                self.time -= 1
                self.after(1000, self.timer)

    def start(self):
        """Begins the timer"""
        self.power_button.configure(text ="Stop", command=lambda: self.stop())
        self.master.bind("<Return>", lambda: self.stop())
        self.running = True
        self.timer()

    def stop(self):
        """Stops the timer"""
        self.power_button.configure(text ="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda: self.start())
        self.running = False

    def reset(self):
        """Resets the timer to 25 mins."""
        self.power_button.configure(text ="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda: self.start())
        self.running = False
        self.time = 1500
        self.clock["text"] = "25:00"

    def quit(self):
        """Ask user if they want to close program."""
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
   

if __name__ == "__main__":
    """Main loop which creates program."""
    root = tk.Tk()
    root.title("POMODORO TIMER")
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()