import pygame

pygame.init()

screen = pygame.display.set_mode((700, 600))
stop_game = False
y = 50
x = 50
clock = pygame.time.Clock()
while not stop_game:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            stop_game = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 0 + 50:
        y -= 20
    if pressed[pygame.K_DOWN] and y < 600 - 50:
        y += 20
    if pressed[pygame.K_RIGHT] and x < 700 - 50:
        x += 20
    if pressed[pygame.K_LEFT] and x > 0 + 50:
        x -= 20
    pygame.draw.circle(screen, (255, 0, 0), [x, y], 50, 50)

    pygame.display.flip()
    clock.tick(15)