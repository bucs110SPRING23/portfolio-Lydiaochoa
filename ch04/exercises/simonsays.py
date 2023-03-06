import random 
import pygame 

pygame.init () 
screen = pygame.display.set_mode()
width, height = screen.get_window_size()
hitbox_width =  width / 2 
hitbox_height = height / 2 

hitboxes = {
    "red": pygame.Rect(0,0, hitbox_width, hitbox_height)
    "green": pygame.Rect(0,0, hitbox_width, hitbox_height)
    "blue": pygame.Rect(0,0, hitbox_width, hitbox_height)
    "purple": pygame.Rect(0,0, hitbox_width, hitbox_height)
}

hitboxes["blue"].topleft = hitboxes["red"].topright
hitboxes["green"].topright = hitboxes["red"].bottomright
hitboxes["purple"].topleft = hitboxes["red"].bottomright

font = pygame.font.sysFont("Arial", 24)
done = False
result = []
turns = 0 
order = list(hitboxes.keys())
random.shuffle(order)

while not done: # have to responfd to every possible event 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True #or break
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                random.shiffle(order)
                turns = len(order)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hitboxes["red"].collidepoint(event.pos):result.append("red")
            elif hitboxes["green"].collidepoint(event.pos):result.append("green")
            elif hitboxes["blue"].collidepoint(event.pos):result.append("blue")
            elif hitboxes["purple"].collidepoint(event.pos):result.append("purple")
    #infinite loops
# pygame.rect (x and y coords, width, and height )
# rectanges do not track visuals
if turns == 0 : 


for c, hb in hitboxes.items():
    box 