import pygame

pygame.init()

screen = pygame.display.set_mode((1400, 1050))
stop_game = False

image = pygame.image.load('line.png').convert()
image.set_colorkey((255, 255, 255))
background = pygame.image.load('mickeyclock.jpeg').convert()
angle_sec = -270
angle_min = -270
clock = pygame.time.Clock()
while not stop_game:
    angle_sec -= 6
    screen.blit(background, (0, 0))
    if 0 >= angle_sec >= -90:
        screen.blit(pygame.transform.rotate(image, angle_sec), (1400 / 2 - 15, 1400 / 2 - (41 / 2) - 170))
    elif -90 > angle_sec >= -180:
        image_copy = pygame.transform.rotate(image, angle_sec)
        screen.blit(image_copy, ((1400 / 2) - int(image_copy.get_width()) + 25, 1050 / 2 - 15))
    elif -180 > angle_sec >= -270:
        image_copy = pygame.transform.rotate(image, angle_sec)
        screen.blit(image_copy, ((1400 / 2) - int(image_copy.get_width()) + 25, (1050 / 2) - int(image_copy.get_height()) + 25))
    elif -270 > angle_sec > -360:
        image_copy = pygame.transform.rotate(image, angle_sec)
        screen.blit(image_copy, (1400 / 2 - 15, (1050 / 2) - int(image_copy.get_height()) + 25))
    if angle_sec == (-354):
        angle_sec = 6
    if angle_sec == (-270):
        angle_min -= 6
    
    if 0 >= angle_min >= -90:
        screen.blit(pygame.transform.rotate(image, angle_min), (1400 / 2 - 15, 1400 / 2 - (41 / 2) - 170))
    elif -90 > angle_min >= -180:
        image_copy = pygame.transform.rotate(image, angle_min)
        screen.blit(image_copy, ((1400 / 2) - int(image_copy.get_width()) + 25, 1050 / 2 - 15))
    elif -180 > angle_min >= -270:
        image_copy = pygame.transform.rotate(image, angle_min)
        screen.blit(image_copy, ((1400 / 2) - int(image_copy.get_width()) + 25, (1050 / 2) - int(image_copy.get_height()) + 25))
    elif -270 > angle_min > -360:
        image_copy = pygame.transform.rotate(image, angle_min)
        screen.blit(image_copy, (1400 / 2 - 15, (1050 / 2) - int(image_copy.get_height()) + 25))
    if angle_min == (-354):
        angle_min = 6
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(1400 / 2, 1050 / 2, 10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            stop_game = True
    pygame.display.update()
    clock.tick(1)