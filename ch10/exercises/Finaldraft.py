
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

pygame.init
w = 10000
h = 1000
screen = pygame.display.set_mode((w,h))
screencords = pygame.display.get_window_size()
pygame.event.get() 
screen.fill("chartreuse4")
pygame.display.flip() 

pygame.draw.rect(screen,"cadetblue2",(0,400,w,400))
pygame.display.flip()
pygame.draw.circle(screen,"green",(380,40))
pygame.display.flip()
pygame.time.wait(2000)

class frog:
    player = pygame.draw.circle()
    
