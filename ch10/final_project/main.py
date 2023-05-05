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

class myProgram:

    def __init__(self):
        self.window = tk.Tk()
        self.my_button = None  # All attributes should be initialize in init
        self.create_widgets()

    def create_widgets(self):
        self.my_counter = tk.Label(self.window, text="start game?")
        self.my_counter.grid(row=0, column=0)

        player_button = tk.Button(self.window, text="yes")
        player_button.grid(row=1, column=0)
        player_button['command'] = self.increment_counter

        quit_button = tk.Button(self.window, text="Quit")
        quit_button.grid(row=2, column=0)
        quit_button['command'] = self.window.destroy

if __name__ == "__main__":
    main()


# def main():
#     pygame.init() ok i think tkinter stuff goes here 
    # Create an instance on your controller object
root.mainloop()

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######



# # https://codefather.tech/blog/if-name-main-python/
# if __name__ == "__main__":
#    from landscape import land()
#    main()

