import pygame
import tkinter as tk
from tkinter import *

# import your controller

def main():
    import pygame
    import tkinter as tk
    # Create the entire GUI program
    program = CounterProgram()

    # Start the GUI event loop
    program.window.mainloop()

class CounterProgram:

    def __init__(self):
        self.window = tk.Tk()
        self.my_counter = None  # All attributes should be initialize in init
        self.create_widgets()

    def create_widgets(self):
        self.my_counter = tk.Label(self.window, text="0")
        self.my_counter.grid(row=0, column=0)

        increment_button = tk.Button(self.window, text="Add 1 to counter")
        increment_button.grid(row=1, column=0)
        increment_button['command'] = self.increment_counter

        quit_button = tk.Button(self.window, text="Quit")
        quit_button.grid(row=2, column=0)
        quit_button['command'] = self.window.destroy

    def increment_counter(self):
        self.my_counter['text'] = str(int(self.my_counter['text']) + 1)

if __name__ == "__main__":
    main()


# def main():
#     pygame.init() ok i think tkinter stuff goes here 
    # Create an instance on your controller object
root.mainloop()

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######



# https://codefather.tech/blog/if-name-main-python/
if __name__ == "__main__":
   from landscape import land()
   main()

