import random

import pygame

BOARD_SIZE = 10

class Game:
    def __init__(self, block_size=40):
        self.w = BOARD_SIZE * block_size
        self.h = BOARD_SIZE * block_size
        self.block_size = block_size

        pygame.init()
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Learn2Slither")

        self.clock = pygame.time.Clock()

        self.snake = []
        self.green_apples = []
        self.red_apple = []

        self.place_snake()
        self.place_food()
        self.draw_board()


    def place_snake(self):
        self.head = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
        self.snake = [self.head, (self.head[0] - 1, self.head[1]), (self.head[0] - 2, self.head[1])]


    def place_food(self):
        while len(self.green_apples) < 2:
            new_apple = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
            if new_apple not in self.snake and new_apple not in self.green_apples:
                self.green_apples.append(new_apple)

        while len(self.red_apple) < 1:
            new_apple = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
            if new_apple not in self.snake and new_apple not in self.green_apples and new_apple not in self.red_apple:
                self.red_apple.append(new_apple)


    def draw_board(self):
        self.screen.fill("black")

        for body in self.snake:
            pygame.draw.rect(self.screen, "blue", (body[0] * self.block_size, body[1] * self.block_size, self.block_size, self.block_size))

        for apple in self.green_apples:
            pygame.draw.rect(self.screen, "green", (apple[0] * self.block_size, apple[1] * self.block_size, self.block_size, self.block_size))

        for apple in self.red_apple:
            pygame.draw.rect(self.screen, "red", (apple[0] * self.block_size, apple[1] * self.block_size, self.block_size, self.block_size))

        pygame.display.flip()


def main():
    game = Game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()