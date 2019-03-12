import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("My first game")

x=50
y=50
width=40
height=60
vol=5

clock=pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
PI = 3.14

done = False
clock = pygame.time.Clock()

while not done:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x>vol:
        x=x-vol
    if keys[pygame.K_RIGHT]:
        x=x+vol
    if keys[pygame.K_UP]:
        y=y-vol
    if keys[pygame.K_DOWN]:
        y=y+vol


    #without trace
    screen.fill((0,0,0))          
    
    pygame.draw.rect(screen, (255,0,0), [x, y, width, height])
    pygame.display.update()
    clock.tick(60)

pygame.quit()