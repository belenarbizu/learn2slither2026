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
        # Place the snake's head at a random position on the board, ensuring it is 2 blocks away from the edges
        self.head = (random.randint(2, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
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

    def game_over(self):
        # Check if the snake's head is out of bounds
        if self.head[0] < 0 or self.head[0] >= BOARD_SIZE or self.head[1] < 0 or self.head[1] >= BOARD_SIZE:
            return True

        # Check if the snake's head collides with its body
        if self.head in self.snake[1:]:
            return True

        return False

    def play_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    
        self.draw_board()
        self.clock.tick(10)  # Control the speed of the game

        return True

    def get_state(self):
        x = self.head[0]
        y = self.head[1]

        # can only provide to the agent the information visible to the snake (left, right, up, down)
        both_sides = [(0, y), (1, y), (2, y), (3, y), (4, y), (5, y), (6, y), (7, y), (8, y), (9, y)]
        up_down = [(x, 0), (x, 1), (x, 2), (x, 3), (x, 4), (x, 5), (x, 6), (x, 7), (x, 8), (x, 9)]

        # W = Wall
        # H = Snake Head
        # S = Snake body segment
        # G = Green apple
        # R = Red apple
        # 0 = Empty space