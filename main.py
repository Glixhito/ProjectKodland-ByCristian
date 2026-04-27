import pygame
import sys
import traceback

from menu import Menu
from game import Game

def main():
    try:
        pygame.init()

        screen = pygame.display.set_mode((800, 600))
        font = pygame.font.SysFont("consolas", 32)

        menu = Menu(screen, font)
        menu.run()

        if menu.choice != "play":
            pygame.quit()
            sys.exit()

        game = Game()
        game.run()

    except Exception as e:
        print("ERROR CRÍTICO:", e)
        traceback.print_exc()
        input("Presiona Enter para salir...")

    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
