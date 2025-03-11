from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
        return super().draw(screen)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self,dt):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            velocity_a = pygame.math.Vector2.rotate(self.velocity, -angle)
            velocity_b = pygame.math.Vector2.rotate(self.velocity, angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1=Asteroid(self.position.x, self.position.y, radius)
            new_asteroid1.velocity = velocity_a * 1.2
            new_asteroid2=Asteroid(self.position.x, self.position.y, radius)
            new_asteroid2.velocity = velocity_b * 1.2



