import pygame

from asteroid import Asteroid
from asteroid_field import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, drawable, updateable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for a in asteroids:
            if a.check_collision(player):
                print("Game over!")
                return
            
            for s in shots:
                if a.check_collision(s):
                    s.kill()
                    a.split()

        for u in updateable:
            u.update(dt)

        for d in drawable:
            d.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
