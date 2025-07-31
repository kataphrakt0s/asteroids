import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    while True:
        screen.fill((0, 0, 0))  # Fill the screen with black

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
                
        delta_time = clock.tick(FPS)  # Limit the frame rate
        dt = delta_time / 1000  # Convert milliseconds to seconds

        pygame.display.flip()  # Update the display


if __name__ == "__main__":
    main()
