import pygame
pygame.init()

monitor = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PP2 pygame")
pygame.display.set_icon(pygame.image.load("icon.png"))
font = pygame.font.Font(None, 86)

check = True
while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
        elif event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            print(key_name)

    monitor.fill((25, 172, 55))
    text = font.render("Press any key", True, (0, 0, 0))
    monitor.blit(text, (800 / 2 - text.get_width() / 2, 600 / 2 - text.get_height() / 2))
    pygame.display.update()

pygame.quit()
