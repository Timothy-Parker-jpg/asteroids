import pygame
from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS, LINE_WIDTH
from src.logger import log_state, log_event
from src.player import Player
from src.asteroid import Asteroid
from src.asteroid_field import AsteroidField
from src.shot import Shot

import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    AsteroidField.containers = (updatable)

    Asteroid.containers = (asteroids, drawable, updatable)

    Player.containers = (updatable,drawable)

    Shot.containers = (shots, drawable, updatable)


    ship = Player(x=SCREEN_WIDTH/2 , y=SCREEN_HEIGHT/2)

    asteroid_field = AsteroidField()



    continue_loop = True
    while continue_loop:
        log_state()
        dt = clock.tick(60) / 1000
        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            if ship.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        for item in drawable:
            item.draw(screen)
        # ship.draw(screen)
    
            # ship.update(dt)

        pygame.display.flip()
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
  
        


if __name__ == "__main__":
    main()
