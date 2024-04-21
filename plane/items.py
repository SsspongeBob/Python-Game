import pygame
from pygame import Surface
from typing import Union, Sequence, Tuple


class Plane:
    def __init__(self, image_path: str) -> None:
        """basical class of the plane.

        Args:
          image_path(str): path to the image of plane.
        """
        self.surface = pygame.image.load(image_path).convert()
        self.surface_rect = self.surface.get_rect()
        self.initial_position = self.surface_rect.center

    def transform(self, size: Union[Tuple[float, float], Sequence[float]]):
        """Only support 'scale' currently."""
        self.surface = pygame.transform.scale(self.surface, size)
        self.surface_rect = self.surface.get_rect()
        self.initial_position = self.surface_rect.center

    def rerender(self, parent_surface: Surface, dest):
        """rerender the plane."""
        parent_surface.blit(self.surface, dest)

    @property
    def get_size(self):
        return self.surface.get_size()


class Bullet:
    pass
