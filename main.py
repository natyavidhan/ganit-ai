import pygame

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Ganit AI")
running = True

canvas = pygame.Surface((800, 700))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    canvas.fill((25, 25, 25))
    screen.blit(canvas, (0, 0))
    pygame.display.update()