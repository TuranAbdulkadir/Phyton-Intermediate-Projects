import pygame, random

pygame.init()
dis = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

x, y = 300, 200
x_ch, y_ch = 0, 0
snake_list, length = [], 1
foodx = round(random.randrange(0, 590) / 10.0) * 10.0
foody = round(random.randrange(0, 390) / 10.0) * 10.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: x_ch, y_ch = -10, 0
            elif event.key == pygame.K_RIGHT: x_ch, y_ch = 10, 0
            elif event.key == pygame.K_UP: x_ch, y_ch = 0, -10
            elif event.key == pygame.K_DOWN: x_ch, y_ch = 0, 10
    
    x += x_ch; y += y_ch
    dis.fill((0,0,0))
    pygame.draw.rect(dis, (0,255,0), [foodx, foody, 10, 10])
    
    snake_head = [x, y]
    snake_list.append(snake_head)
    if len(snake_list) > length: del snake_list[0]
    
    for x in snake_list: pygame.draw.rect(dis, (50,153,213), [x[0], x[1], 10, 10])
    pygame.display.update()
    
    if x == foodx and y == foody:
        foodx = round(random.randrange(0, 590) / 10.0) * 10.0
        foody = round(random.randrange(0, 390) / 10.0) * 10.0
        length += 1
    
    clock.tick(15)