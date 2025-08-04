import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen: pygame.display):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        self.create_new_asteroid(self, random_angle)
        self.create_new_asteroid(self, -random_angle)
        
        
    def create_new_asteroid(self, parent, rotate_by):
        radius = parent.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(parent.position.x, parent.position.y, radius)
        angle = parent.velocity.rotate(rotate_by)
        asteroid.velocity = angle * 1.2
