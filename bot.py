import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line Tracing Bot Simulator")

bot_x, bot_y = WIDTH // 2, HEIGHT - 50
bot_angle = 0  

clock = pygame.time.Clock()

drawing = False
line_points = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            line_points = [event.pos]

        if event.type == pygame.MOUSEMOTION and drawing:
            line_points.append(event.pos)

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

    screen.fill(WHITE)

    if len(line_points) >= 2:
        pygame.draw.lines(screen, BLACK, False, line_points, 5)

        if not drawing:
            for i in range(len(line_points) - 1):
                start_point = line_points[i]
                end_point = line_points[i + 1]

                dx = end_point[0] - bot_x
                dy = end_point[1] - bot_y
                angle_to_line = math.atan2(dy, dx)

                bot_angle = angle_to_line

                bot_speed = 2
                bot_x += bot_speed * math.cos(bot_angle)
                bot_y += bot_speed * math.sin(bot_angle)

    pygame.draw.circle(screen, GREEN, (int(bot_x), int(bot_y)), 20)
    pygame.display.flip()
    clock.tick(60)
