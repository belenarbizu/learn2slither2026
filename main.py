from game import Game
import pygame

def main():
    game = Game()
    running = True

    while running and not game.game_over():
        state = game.get_state()
        print("Current State:", state)  # Print the current state for debugging
        running = game.play_game()

    pygame.quit()

if __name__ == "__main__":
    main()