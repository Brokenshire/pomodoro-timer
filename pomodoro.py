"""
Simple pomodoro timer GUI application using tkinter.

Author: Jack Brokenshire
Date: 30/12/2019
Version: 1.0
"""

# Standard import
import time
import winsound

# Third-party imports
import tkinter as tk
import tkinter.messagebox


class Application(tk.Frame):
    """"
    A class used to represent an Application

    Simple pomodoro timer application using tkinter.

    Attributes:
    ----------
    master: 
        frame defenition
    *args:
        variable positional arguments
    **kwargs:
        variable keyword argurments
    running: boolean
        the state of the application
    pomodoro: boolean
        the state of the pomodoro timer
    time: int
        the whole time of the application
    mins: int
        the current minutes of the application
    secs: int
        the current seconds of the application

    Methods:
    ----------
    build_interface()
        Builds the GUI interface
    calculate()
        Calculates the current time
    timer()
        Manages running of the timer
    start()
        Starts the timer
    stop()
        Stops the timer
    reset()
        Resets the timer
    quit()
        Quits the program
    """
    def __init__(self, master, *args, **kwargs):
        """
        Paramaters
        ----------
        master: 
            frame defenition
        *args:
            variable positional arguments
        **kwargs:
            variable keyword argurments
        running: boolean
            the state of the application
        pomodoro: boolean
            the state of the pomodoro timer
        time: int
            the whole time of the application
        mins: int
            the current minutes of the application
        secs: int
            the current seconds of the application
        """
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.running = False
        self.pomodoro = True
        self.time = 1500
        self.mins = 0
        self.secs = 0
        self.build_interface()

    def build_interface(self):
        """Builds the interface for the application."""
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

        self.master.bind("<Return>", lambda x: self.start())

    def calcualte(self):
        """Calcualtes the current time"""
        self.mins, self.secs = divmod(self.time, 60)
        return "{:02d}:{:02d}".format(self.mins, self.secs)

    def timer(self):
        """Functionality behind timer"""
        if self.running is True:
            if self.time <= 0:
                winsound.PlaySound("alert.wav", winsound.SND_FILENAME)
                if self.pomodoro is True:
                    self.time = 300
                    self.clock.configure(text="05:00")
                    self.pomodoro = False
                else:
                    self.time = 1500
                    self.clock.configure(text="25:00")
                    self.pomodoro = True
            self.clock.configure(text=self.calcualte())
            self.time -= 1
            self.after(1000, self.timer)

    def start(self):
        """Begins the timer"""
        self.power_button.configure(text ="Stop", command=lambda: self.stop())
        self.master.bind("<Return>", lambda x: self.stop())
        self.running = True
        self.timer()

    def stop(self):
        """Stops the timer"""
        self.power_button.configure(text ="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False

    def reset(self):
        """Resets the timer to 25 mins."""
        self.power_button.configure(text ="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
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