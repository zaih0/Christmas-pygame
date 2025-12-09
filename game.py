import pygame 
import sys
import time
import os

# SETUP GAME WINDOW
pygame.init()
WIDTH, HEIGHT = 0, 0
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Santa Hunt")
clock = pygame.time.Clock()
FPS = 60

# LOADING THE SHOOTY POINTER TO SHOOT THINGS WITH
CROSSHAIR_PATH = os.path.join("assets", "crosshair.png")
try:
    cross_img = pygame.image.load(CROSSHAIR_PATH).convert_alpha()
    cross_img = pygame.transform.smoothscale(cross_img, (48, 48))
    use_cross_img = True
    cross_rect = cross_img.get_rect()
    
except Exception:
    cross_img = None
    use_cross_img = False
    cross_rect = pygame.Rect(0, 0, 48, 48)

pygame.mouse.set_visible(False)


# MAIN GAMER LOOP WHERE GAME LOOP HAPPENS
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mx, my = pygame.mouse.get_pos() 
           
    screen.fill((135, 206, 235))
    
    if use_cross_img and cross_img:
        cross_rect.center = (mx, my)
        screen.blit(cross_img, cross_rect)
        
    else:
        pygame.draw.line(screen, (0, 0, 0), (mx-12, my), (mx+12, my), 2)
        pygame.draw.line(screen, (0, 0, 0), (mx, my-12), (mx, my+12), 2)
        #pygame.draw.line(screen, (255, 255, 255), (mx, my), 4)
        
    
    pygame.display.flip()
    clock.tick(FPS)

# EXIT AND CLOSING THE WINDOW
pygame.quit()
sys.exit()