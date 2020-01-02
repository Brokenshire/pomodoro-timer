# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Simple pomodoro timer GUI application using tkinter.
#
# Author: Jack Brokenshire
# Date: 30/12/2019
# Version: 2.0

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Standard import
import winsound

# Third-party imports
import tkinter.ttk
from tkinter.constants import *
import tkinter.messagebox


class Application(tkinter.ttk.Frame):
    """"A class used to represent an Application

    Simple pomodoro timer application using tkinter.

    Attributes:
        root: Frame definition.
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.
        running: A boolean indicating if application is running or not.
        pomodoro: A boolean indicating if current stage is pomodoro or break.
        time: An integer count of the timer.
        mins: An integer count of the minutes.
        secs: An integer count of the seconds.
    """

    @classmethod
    def main(cls):
        tkinter.NoDefaultRoot()
        root = tkinter.Tk()
        root.title("POMODORO TIMER")
        app = cls(root)
        app.grid(sticky=NSEW)
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        root.resizable(True, True)
        root.mainloop()

    def __init__(self, root):
        """Init Application which contains root, *args, and **kwargs."""
        super().__init__(root)
        self.create_variables()
        self.create_widgets()
        self.grid_widgets()
        self.bind("<Return>", lambda x: self.start())
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def create_variables(self):
        self.running = tkinter.BooleanVar(self, False)
        self.pomodoro = tkinter.BooleanVar(self, True)
        self.time = tkinter.IntVar(self, 1500)
        self.mins = tkinter.IntVar(self)
        self.secs = tkinter.IntVar(self)

    def create_widgets(self):
        """Creates the widgets of the application"""
        self.clock = tkinter.Label(self, text="25:00", font=("Courier", 18), width=10)
        self.time_label = tkinter.Label(self, text="min sec", font=("Courier", 10), width=10)
        self.reset_button = tkinter.Button(self, text="Reset", command=lambda: self.reset())
        self.power_button = tkinter.Button(self, text="Start", command=lambda: self.start())
        self.quit_button = tkinter.Button(self, text="Quit", command=lambda: self.quit())

    def grid_widgets(self):
        """Grids the widgets of the application"""
        options = dict(sticky=NSEW, padx=3, pady=4)
        self.clock.grid(row=0, column=1, **options)
        self.time_label.grid(row=1, column=1, **options)
        self.reset_button.grid(row=2, column=0, **options)
        self.power_button.grid(row=2, column=1, **options)
        self.quit_button.grid(row=2, column=2, **options)

    def calculate(self):
        """Calculates the current time.
        
        Returns:
            The current time in minutes and seconds.
        """
        self.mins, self.secs = divmod(self.time.get(), 60)
        return "{:02d}:{:02d}".format(self.mins, self.secs)

    def timer(self):
        """Functionality behind pomodoro timer."""
        if self.running is True:
            if self.time <= 0:
                winsound.PlaySound("alert.wav", winsound.SND_FILENAME)
                if self.pomodoro is True:
                    self.time.set(300)
                    self.pomodoro.set(False)
                else:
                    self.time.set(1500)
                    self.pomodoro.set(True)
            self.clock.configure(text=self.calculate())
            self.time -= - 1
            self.after(1000, self.timer)

    def start(self):
        """Begins the pomodoro timer."""
        self.power_button.configure(text="Stop", command=lambda: self.stop())
        self.bind("<Return>", lambda x: self.stop())
        self.running = True
        self.timer()

    def stop(self):
        """Stops the pomodoro timer"""
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.bind("<Return>", lambda x: self.start())
        self.running = False

    def reset(self):
        """Resets the pomodoro timer to 25 mins."""
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.bind("<Return>", lambda x: self.start())
        self.running = False
        self.time = 1500
        self.clock["text"] = "25:00"

    def quit(self):
        """Ask user if they want to close program."""
        if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()


if __name__ == "__main__":
    """Main loop which creates program."""
    Application.main()
