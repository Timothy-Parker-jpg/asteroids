from src.circleshape import CircleShape
from src.constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from src.logger import log_event
import pygame
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)


    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            log_event("asteroid_split")
            print("asteroid split")
            velocity_one = self.velocity.rotate(uniform(20,50))
            velocity_two = self.velocity.rotate(uniform(20,50))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            print("new_asteroid")
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_one.velocity = velocity_one * 1.2
            asteroid_two.velocity = velocity_two * 1.2
            return asteroid_one, asteroid_two
