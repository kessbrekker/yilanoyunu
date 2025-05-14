import pygame
import random
import sys

pygame.init()

# Oyun ekranı boyutları
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yılan Oyunu")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*block, BLOCK_SIZE, BLOCK_SIZE))

def draw_apple(position):
    pygame.draw.rect(screen, (255, 0, 0), (*position, BLOCK_SIZE, BLOCK_SIZE))

def random_position():
    x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return (x, y)

def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (BLOCK_SIZE, 0)
    apple = random_position()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                    direction = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                    direction = (0, BLOCK_SIZE)
                elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                    direction = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                    direction = (BLOCK_SIZE, 0)

        # Yılanın başını hareket ettir
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Duvara veya kendine çarpma kontrolü
        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake
        ):
            break  # Oyun biter

        snake.insert(0, new_head)

        # Elma yeme kontrolü
        if new_head == apple:
            score += 1
            apple = random_position()
            while apple in snake:
                apple = random_position()
        else:
            snake.pop()  # Kuyruğu kısalt

        screen.fill((0, 0, 0))
        draw_snake(snake)
        draw_apple(apple)
        score_text = font.render(f"Skor: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        clock.tick(5)

    # Oyun bitti ekranı
    screen.fill((0, 0, 0))
    msg = font.render("Oyun Bitti! Skor: {}".format(score), True, (255, 0, 0))
    screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - msg.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

if __name__ == "__main__":
    main()