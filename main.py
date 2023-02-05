import pygame, sys
from pygame.locals import QUIT

def trackBorders(carx,cary,originx,originy):
  if cary > 260 or (cary < 190 and ):
    carx = originx
    cary = originy
    carangle = 0
  return carx,cary
redx = 50
redy = 220
redspeedx = 0
redspeedy = 0
redcarangle = 0
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
bluecar = pygame.transform.scale(pygame.image.load("images/Blue Car.png"),(25,15))
redcar = pygame.transform.scale(pygame.image.load("images/Red Car.png"), (25,15))
racetrack = pygame.transform.scale(pygame.image.load("images/RaceTrack.png"),(400,300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
          print(redcarangle)
          if event.key == pygame.K_w:
            redspeedy = redcarangle/100
            redspeedx = 1 + redspeedy
            if redcarangle == 90 or redcarangle == -90:
              redspeedx = 0
          if redspeedx != 0 or redspeedy != 0:
            if event.key == pygame.K_a and redcarangle > -90:
              redcarangle -= 30
              redcar = pygame.transform.rotate(redcar, 30)
              redspeedy = redcarangle/100
              redspeedx = 1 + redspeedy
              if redcarangle == 90 or redcarangle == -90:
                redspeedx = 0
            if event.key == pygame.K_d and redcarangle < 90:
              redcarangle += 30
              redcar = pygame.transform.rotate(redcar, -30)
              redspeedy = redcarangle/100
              redspeedx = 1 + redspeedy
              if redcarangle == 90 or redcarangle == -90:
                redspeedx = 0
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_w:
            redspeedx = 0
            redspeedy = 0
    redx,redy = trackBorders(redx,redy,50,220) 
    redx += redspeedx
    redy += redspeedy
    DISPLAYSURF.fill((255,255,255))
    DISPLAYSURF.blit(racetrack, (0,0))
    DISPLAYSURF.blit(bluecar, (50, 240))
    DISPLAYSURF.blit(redcar, (redx, redy))
    pygame.display.update()