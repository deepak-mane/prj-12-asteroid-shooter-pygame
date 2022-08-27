#!I:\PYTHON_50\prj-12-asteroid-shooter-pygame\py_scripts390\.venv390\Scripts\python.exe
import pygame
import sys

pygame.init()
WINOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Meteor shooter')
clock = pygame.time.Clock()

# importing images & background
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINOW_WIDTH / 2, WINDOW_HEIGHT / 2))
print(ship_rect)


bg_surf = pygame.image.load('./graphics/background.png').convert()

# import text
font = pygame.font.Font('./graphics/subatomic.ttf', 50)
# White can be replace with tuple (255,255,255)
text_surf = font.render('Space', True, 'White')


# create a surface
test_surf = pygame.Surface((400, 100))
# Need to attach surface to display surface. Both of surfaces are black as well
text_rect = text_surf.get_rect(midbottom=(WINOW_WIDTH / 2, WINDOW_HEIGHT - 80))

while True:  # run forever => keeps our game running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # framerate limit
    clock.tick(120)

    # mouse input
    print(pygame.mouse.get_pos())
    print(pygame.mouse.get_pressed())
    ship_rect.center = pygame.mouse.get_pos()
    # 2 . Updates
    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_surf, (0, 0))
    display_surface.blit(ship_surf, ship_rect)
    display_surface.blit(text_surf, text_rect)

    # 3 . Show the frame to the player / update the display surface
    pygame.display.update()
