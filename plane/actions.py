import pygame
from pygame import Rect
from typing import Iterable, Tuple


# get the initial position
def get_initial_position(rect: Rect):
    """get the initial position

    Return:
        rect.center: the initial center of the item
    """
    return rect.center


# detect the keyboard events
def detect_to_move(surface_rect: Rect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        surface_rect.y -= 1
    if keys[pygame.K_a]:
        surface_rect.x -= 1
    if keys[pygame.K_s]:
        surface_rect.y += 1
    if keys[pygame.K_d]:
        surface_rect.x += 1


# check if the item off the screen
def check_for_outline(
    initial_position: Iterable[Tuple[int, int]], rect: Iterable[Rect]
):
    for item in zip(initial_position, rect):
        if item[1].top < 0:
            # initial to the origin position
            item[1].center = item[0]
