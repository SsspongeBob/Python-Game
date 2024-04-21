import pygame
from items import Plane
from actions import get_initial_position, detect_to_move, check_for_outline

# init and get the window_rect
pygame.init()
window = pygame.display.set_mode((800, 600))
window.fill("white")
clock = pygame.time.Clock()
pygame.display.set_caption("python game")

# load the plane
plane = Plane(image_path="/Users/dinggao/Pictures/plane.png")
plane.transform(size=(30, 30))
plane.surface_rect.center = (
    window.get_rect().center
)  # set the center the same to the window
plane_initial_position = plane.initial_position  # get the initial position

# add the plane to curtain
plane.rerender(window, plane.surface_rect)

# add the bullet
bullet_rect = pygame.Rect(0, 0, 5, 15)
bullet_rect.midbottom = plane.surface_rect.midtop
bullet_initial_position = bullet_rect.center  # get the initial position
pygame.draw.rect(window, "red", bullet_rect, border_radius=5)
# set the default moving speed of bullet
speed = 2

# render the items initialy
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # plane
    # detect the keyboard event
    detect_to_move(plane.surface_rect)
    plane.rerender(window, plane.surface_rect)

    # bullet
    check_for_outline([bullet_initial_position], [bullet_rect], type=["bullet"])
    bullet_rect = bullet_rect.move(0, -speed)
    pygame.draw.rect(window, "red", bullet_rect, border_radius=5)

    # update the items
    pygame.display.update()

    clock.tick(60)
    # refrech the screen
    window.fill("white")

pygame.quit()
