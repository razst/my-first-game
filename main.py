import pygame
import time

# screen size 
WINDOW_W = 250
WINDOW_H = 164
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

BK_COLOR = (68,132,88)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My First Game")

bk_image = pygame.image.load("background.jpg")

play = True
while play:
  # screen.fill(BK_COLOR)
  screen.blit(bk_image,(0,0))
#   pygame.draw.line(screen,(255,255,255),[0,100],[WINDOW_W,100],2)
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

pygame.quit()
