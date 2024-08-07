import pygame

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Ganit AI")
running = True

canvas = pygame.Surface((800, 700))
writing = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    mouse_down = pygame.mouse.get_pressed()[0]
    if mouse_down:
        pos = pygame.mouse.get_pos()
        writing.append(pos)

    screen.fill((0, 0, 0))
    canvas.fill((25, 25, 25))
    for pos in writing:
        pygame.draw.circle(canvas, (255, 255, 255), pos, 1)
    screen.blit(canvas, (0, 0))
    pygame.display.update()