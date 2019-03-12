import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("My first game")
clock=pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
PI = 3.14

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
  for event in pygame.event.get(): # User did something
    if event.type == pygame.QUIT: # If user clicked close
        done = True # Flag that we are done so we exit this loop
  
    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # --- Go ahead and update the screen with what we've drawn.
    # --- Limit to 60 frames per second

    #pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
    pygame.draw.line(screen, WHITE, [10, 30], [290, 15])
    pygame.draw.line(screen, WHITE, [10, 50], [290, 35])
        
        #aaline згладжена лінія, товщина в цьому
        # випадку не задається
    pygame.draw.aaline(screen, WHITE, [10, 70], [290, 55])

    pygame.draw.arc(screen, WHITE, (10, 50, 280, 100), 0, PI)
    pygame.draw.arc(screen, PINK, (50, 30, 200, 150), PI, 2*PI, 3)
    # (100, 100) координати центра
        # 50 - радіус

    pygame.draw.circle(screen, YELLOW, (100, 100), 50)
    pygame.draw.circle(screen, PINK, (200, 100), 50, 10)

    screen.fill(PINK)

    pygame.display.update()

    clock.tick(60)