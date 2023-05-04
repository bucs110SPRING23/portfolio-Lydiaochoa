
import pygame 
# import tkinter as tk
# from tkinter import ttk

# global my_counter


# def create_user_interface(application_window):
#     global my_counter

#     my_counter = ttk.Label(application_window, text="0")
#     my_counter.grid(row=0, column=0)

#     class playerbuttons: 
#         window = tk.Tk()
#         create_user_interface(window)
#         player_button = ttk.Button(application_window, text = "jump")
#         player_button.grid(row=1, column=0)
#         quit_button = ttk.Button(application_window, text="Quit")
#         quit_button.grid(row=2, column=0)
#         quit_button['command'] = window.destroy

#         window.mainloop()

import tkinter as tk
from tkinter import ttk

def main():
    # Create the entire GUI program
    program = frogs()

    # Start the GUI event loop
    program.window.mainloop()

class frogs():

    def __init__(self):
        self.window = tk.Tk()
        self.my_counter = None  # All attributes should be initialize in init
        self.create_widgets()

    def create_widgets(self):
        self.my_counter = ttk.Label(self.window, text="0")
        self.my_counter.grid(row=0, column=0)

        increment_button = ttk.Button(self.window, text="Add 1 to counter")
        increment_button.grid(row=1, column=0)
        increment_button['command'] = self.increment_counter

        quit_button = ttk.Button(self.window, text="Quit")
        quit_button.grid(row=2, column=0)
        quit_button['command'] = self.window.destroy

    def increment_counter(self):
        self.my_counter['text'] = str(int(self.my_counter['text']) + 1)

if __name__ == "__main__":
    main()
pygame.init
w = 10000
h = 1000
screen = pygame.display.set_mode((w,h))
screencords = pygame.display.get_window_size()
pygame.event.get() 
screen.fill("chartreuse4")
pygame.display.flip() 

class river:
    pygame.draw.rect(screen,"cadetblue2",(0,400,w,400))
    pygame.display.flip()
    pygame.time.wait(2000)

class frog:
    player = pygame.draw.circle()
    
