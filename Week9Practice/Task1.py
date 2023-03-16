import pygame
pygame.init()

monitor = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PP2 pygame")
pygame.display.set_icon(pygame.image.load("icon.png"))
check = True

while check:
  
  monitor.fill((0, 0, 255))

  pygame.display.update()
  for action in pygame.event.get():
    if action.type == pygame.QUIT:
      check = False
      pygame.quit()
