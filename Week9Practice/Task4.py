import pygame
import random

pygame.init()

monitor = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PP2 pygame")
pygame.display.set_icon(pygame.image.load("icon.png"))
monitor.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

for i in range(10):
    rect = pygame.Rect(random.randint(0, 800), random.randint(0, 600), random.randint(10, 200), random.randint(10, 200))
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.rect(monitor, color, rect)

pygame.image.save(monitor, "example.png")

pygame.quit()
