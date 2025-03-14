from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
import random
import pygame

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vec1, vec2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            x, y = self.position
            ast1, ast2 = Asteroid(x, y, new_radius), Asteroid(x, y, new_radius)
            ast1.velocity = vec1 * 1.2
            ast2.velocity = vec2 * 1.2
    