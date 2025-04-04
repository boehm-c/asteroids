from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def set_velocity(self, player_rotation):
        self.rotation = player_rotation
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
    
    def update(self, dt):
        self.position += self.velocity * PLAYER_SHOOT_SPEED * dt