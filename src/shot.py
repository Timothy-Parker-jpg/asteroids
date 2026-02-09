from src.circleshape import CircleShape
from src.constants import SHOT_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def rotate(self,dt):
        self.rotation += (dt * PLAYER_TURN_SPEED)
