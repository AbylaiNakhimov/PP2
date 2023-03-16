import pygame

pygame.init()
red = (255, 0, 0)
monitor = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PP2 pygame")
pygame.display.set_icon(pygame.image.load("icon.png"))
monitor.fill((25, 172, 55))

done = False
x = 30
y = 30
def Draw_Circle(x, y):
    monitor.fill((25, 172, 55))
    pygame.draw.circle(monitor, red, (x, y), 25)
pygame.draw.circle(monitor, red, (x, y), 25)
pygame.draw.rect(monitor, red, (200, 200, 30,40) )
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN):
            y += 40
            if y >= 600:
                y = 20
            Draw_Circle(x, y)
        else:
            Draw_Circle(x, y)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 40
            if y <= 0:
                y = 580
            Draw_Circle(x, y)
        else:
            Draw_Circle(x, y)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= 40
            if x <= 0:
                x = 800
            Draw_Circle(x, y)
        else:
            Draw_Circle(x, y)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += 40
            if x >= 780:
                x = 20
            Draw_Circle(x, y)
        else:
            Draw_Circle(x, y)
    pygame.display.update()
pygame.quit()