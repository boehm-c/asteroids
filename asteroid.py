from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        rand_ang = random.uniform(20, 50)
        new_left_asteroid.velocity = self.velocity.rotate(-rand_ang) * 1.2
        new_right_asteroid.velocity = self.velocity.rotate(rand_ang) * 1.2