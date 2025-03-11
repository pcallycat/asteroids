import circleshape
import pygame
from constants import *


class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, SHOT_RADIUS)
        self.velocity = pygame.Vector2()

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
        return super().draw(screen)

    def update(self, dt):
        self.position += self.velocity * dt


