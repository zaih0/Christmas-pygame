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

# SHOTS AND SCORES VARIABLES
score = 0
shots_fired = 0
hits = 0
shoot_cooldown = 0.35   # flash stays longer
last_shot_time = 0.0
muzzle_flash_timer = 0.0

# MAKE FLASH STAY WHERE MOUSE WAS CLICKED
flash_pos = (0, 0)


# MAIN GAME LOOP
running = True
while running:
    dt = clock.get_time() / 1000.0

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # PRESS ESC TO EXIT GAME
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # 🔫 SHOOTING WITH LEFT MOUSE CLICK
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            shots_fired += 1
            score += 1   # temporary until enemies added

            muzzle_flash_timer = shoot_cooldown
            last_shot_time = time.time()

            # SAVE MOUSE POSITION FOR FLASH
            flash_pos = pygame.mouse.get_pos()

    # GET WHERE THE MOUSE IS
    mx, my = pygame.mouse.get_pos() 

    # BACKGROUND?
    screen.fill((135, 206, 235))

    # DRAW SHOOTY POINTER
    if use_cross_img and cross_img:
        cross_rect.center = (mx, my)
        screen.blit(cross_img, cross_rect)
    else:
        pygame.draw.line(screen, (255, 192, 203), (mx-12, my), (mx+12, my), 2)
        pygame.draw.line(screen, (255, 192, 203), (mx, my-12), (mx, my+12), 2)
        pygame.draw.circle(screen, (255, 255, 255), (mx, my), 4)

    # BIG GUN EFFECT GO BOOM
    if muzzle_flash_timer > 0:
        muzzle_flash_timer -= dt 

        progress = max(0, muzzle_flash_timer / shoot_cooldown)
        alpha = max(0, int(255 * (progress ** 0.5)))  # MAKES SHOT TAKE SLOWER TO DISSAPPEAR
        flash_radius = 24 + int(16 * progress)

        flash_surf = pygame.Surface((flash_radius*2, flash_radius*2), pygame.SRCALPHA)
        pygame.draw.circle(
            flash_surf,
            (255, 255, 0, alpha),
            (flash_radius, flash_radius),
            flash_radius
        )

        # USE LAST FLASH POINT !
        fx, fy = flash_pos
        screen.blit(flash_surf, (fx - flash_radius, fy - flash_radius))

    pygame.display.flip()
    clock.tick(FPS)

# GAME STOP NOW
pygame.quit()
sys.exit()
