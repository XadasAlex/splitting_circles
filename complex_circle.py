import pygame
import math

# Define constants
WINDOW_SIZE = 500
CENTER = WINDOW_SIZE // 2
RADIUS = 230
POINT_COLOR = (214, 87, 70)
LINE_COLOR = (242, 172, 50)
BACKGROUND_COLOR = (96, 96, 96)
CIRCLE_COLOR = (0, 0, 0)
FPS = 120
FONT_SIZE = 36
SPEED = 50 / FPS

def draw(window, start_angle, points, radius):
    angles = [round(start_angle + i * 360 / points, 1) for i in range(points)]
    print(angles)

    previous = None
    first = None

    for i, angle in enumerate(angles):
        radians = math.radians(angle)
        cos = math.cos(radians)
        sin = math.sin(radians)

        x = cos * radius + CENTER
        y = sin * radius + CENTER

        pygame.draw.circle(window, POINT_COLOR, (x, y), 4)

        if i != 0:
            pygame.draw.line(window, LINE_COLOR, (x, y), previous)
        else:
            first = (x, y)
            pygame.draw.line(window, LINE_COLOR, (x, y), (CENTER, CENTER))

        if i == len(angles) - 1:
            pygame.draw.line(window, LINE_COLOR, (x, y), first)

        previous = (x, y)

pygame.init()

window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.update()

running = True
clock = pygame.time.Clock()

angle = 0.5
points = 1

font = pygame.font.SysFont(None, FONT_SIZE)

while running:
    clock.tick(FPS)
    angle += SPEED

    if abs(angle % 90) < SPEED:
        points += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BACKGROUND_COLOR)
    pygame.draw.circle(window, CIRCLE_COLOR, (CENTER, CENTER), RADIUS)
    pygame.draw.circle(window, BACKGROUND_COLOR, (CENTER, CENTER), RADIUS - 1)
    pygame.draw.line(window, CIRCLE_COLOR, (0, CENTER), (WINDOW_SIZE, CENTER))
    pygame.draw.line(window, CIRCLE_COLOR, (CENTER, 0), (CENTER, WINDOW_SIZE))

    draw(window, angle, points, RADIUS)
    points_text = font.render(f"Points: {points}", True, (255, 255, 255))
    window.blit(points_text, (10, 10))
    pygame.display.flip()

pygame.quit()
