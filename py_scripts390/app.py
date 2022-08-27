#!I:\PYTHON_50\prj-12-asteroid-shooter-pygame\py_scripts390\.venv390\Scripts\python.exe
import pygame
import sys

# game init
pygame.init()
WINOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Meteor shooter')
clock = pygame.time.Clock()

# ship import
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()
ship_surf_rotated = pygame.transform.rotate(ship_surf, 45)
ship_surf_scaled = pygame.transform.scale(ship_surf, (600, 50))
ship_reversed_surf = pygame.transform.flip(ship_surf, False, True)
ship_rect = ship_surf.get_rect(center=(WINOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# importing images & background
bg_surf = pygame.image.load('./graphics/background.png').convert()

# laser import
laser_surf = pygame.image.load('./graphics/laser.png').convert_alpha()
laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)

# import text
font = pygame.font.Font('./graphics/subatomic.ttf', 50)
# White can be replace with tuple (255,255,255)
text_surf = font.render('Space', True, 'White')
# create a surface
test_surf = pygame.Surface((400, 100))
# Need to attach surface to display surface. Both of surfaces are black as well
text_rect = text_surf.get_rect(midbottom=(WINOW_WIDTH / 2, WINDOW_HEIGHT - 80))

# drawing
test_rect = pygame.Rect(100, 200, 400, 500)

while True:
    # run forever => keeps our game running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # framerate limit
    clock.tick(120)

    # update
    laser_rect.y -= 10

    # drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_surf, (0, 0))

    display_surface.blit(text_surf, text_rect)
    display_surface.blit(laser_surf, laser_rect)

    # rect drawing
    # pygame.draw.rect(display_surface, 'purple',
    #                  test_rect, width=10, border_radius=5)
    # pygame.draw.lines(display_surface, 'red', False, [
    #                   (0, 0), (200, 0), (300, 100)], width=1)
    pygame.draw.rect(display_surface, (255, 255, 255),
                     text_rect.inflate(30, 30), width=8, border_radius=5)
    # display_surface.blit(ship_reversed_surf, ship_rect)
    # display_surface.blit(ship_surf_scaled, ship_rect)
    display_surface.blit(ship_surf_rotated, ship_rect)
    # draw the final frame
    pygame.display.update()
