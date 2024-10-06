import pygame
import math

point_color = (214, 87, 70)
line_color = (242, 172, 50)

def draw(window, start_angle, points, radius):
    angles = [round(start_angle + i * 360/points, 1) for i in range(points)]
    print(angles)

    previous: set[float, float]
    first: set[float, float]

    for (i, angle) in enumerate(angles):
        radians = math.radians(angle)
        cos = math.cos(radians)
        sin = math.sin(radians)

        x = cos * radius + 250
        y = sin * radius + 250

        pygame.draw.circle(window, point_color, (x, y), 4)

        if i != 0:
            pygame.draw.line(window, line_color, (x, y), previous)

        else:
            first = (x, y)
            pygame.draw.line(window, line_color, (x, y), (250, 250))

        if i == len(angles) - 1:
            pygame.draw.line(window, line_color, (x, y), first)


        previous = (x, y)

pygame.init()


window = pygame.display.set_mode((500, 500))

pygame.display.update()

running = True

clock = pygame.time.Clock()

angle = 0.5
points = 1

FPS = 120
font = pygame.font.SysFont(None, 36)
speed = 50/FPS

while running:
    clock.tick(FPS)

    angle += speed

    if abs(angle % 90) < speed:
        points += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((96, 96, 96))
    pygame.draw.circle(window, (0, 0, 0), (250, 250), 230)
    pygame.draw.circle(window, (96, 96, 96), (250, 250), 229)
    pygame.draw.line(window, (0, 0, 0), (0, 250), (500, 250))
    pygame.draw.line(window, (0, 0, 0), (250, 0), (250, 500))

    draw(window, angle, points, 230)
    points_text = font.render(f"Points: {points}", True, (255, 255, 255))
    window.blit(points_text, (10, 10))
    pygame.display.flip()

pygame.quit()