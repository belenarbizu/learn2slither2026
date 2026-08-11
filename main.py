from game import Game
import pygame

def main():
    game = Game()
    running = True

    while running and not game.game_over():
        running = game.play_game()

    pygame.quit()

if __name__ == "__main__":
    main()