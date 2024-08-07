import pygame

screen = pygame.display.set_mode((1500, 900))
pygame.display.set_caption("Ganit AI")
running = True

canvas = pygame.Surface((1500, 900))

writing = []
boxes = []

boxing = False
box_init = (0, 0)
last_boxing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    mouse_down = pygame.mouse.get_pressed()[0]

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) and mouse_down:
        if not boxing:
            boxing = True
            box_init = pygame.mouse.get_pos()
    else:
        boxing = False

    if not boxing and last_boxing:
        boxes.append((box_init[0], box_init[1], pos[0]-box_init[0], pos[1]-box_init[1]))
        last_boxing = False

    if mouse_down and not boxing:
        pos = pygame.mouse.get_pos()
        writing.append(pos)

    screen.fill((0, 0, 0))
    canvas.fill((25, 25, 25))

    for pos in writing:
        pygame.draw.circle(canvas, (255, 255, 255), pos, 1)

    if boxing:
        last_boxing = True
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(canvas, (255, 255, 255), (box_init[0], box_init[1], pos[0]-box_init[0], pos[1]-box_init[1]), 1)

    for box in boxes:
        pygame.draw.rect(canvas, (255, 255, 255), box, 1)

    screen.blit(canvas, (0, 0))
    pygame.display.update()