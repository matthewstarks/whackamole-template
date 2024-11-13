import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        color = "black"

        screen.fill("light green")
        for i in range(1, 16):
            pygame.draw.line(screen, color, (0, i * 32), (640, i * 32))
        for i in range(1, 20):
            pygame.draw.line(screen, color, (i * 32, 0), (i * 32, 640))
        screen.blit(mole_image, mole_image.get_rect(topleft = (0, 0)))
        molex = 0
        moley = 0


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = x // 32
                    col = y // 32
                    if row == molex and col == moley:
                        molex = random.randint(0, 19)
                        moley = random.randint(0, 15)
                        screen.fill("light green")
                        for i in range(1, 16):
                            pygame.draw.line(screen, color, (0, i * 32), (640, i * 32))
                        for i in range(1, 20):
                            pygame.draw.line(screen, color, (i * 32, 0), (i * 32, 640))
                        screen.blit(mole_image, mole_image.get_rect(topleft=(molex * 32, moley * 32)))
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
