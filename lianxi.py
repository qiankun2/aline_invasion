import sys

import pygame

def run_g():
    pygame.display.set_mode((1200,600))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print (event.key)

run_g()


