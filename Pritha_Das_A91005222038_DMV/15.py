#Program to draw an animated circle having keyboard interaction
import pygame
import sys

#taking user inputs
radius = int(input("Enter radius of the circle: "))
speed = int(input("Enter movement speed (e.g. 5): "))

#initial setup
pygame.init()
font = pygame.font.SysFont(None, 24)

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Interactive Circle ")

#initial position (center)
x, y = width // 2, height // 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print("Key pressed:", pygame.key.name(event.key))  

    #key press handling
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed

    
    screen.fill((255, 255, 255))

    #drawing axes
    pygame.draw.line(screen, (0, 0, 0), (0, height//2), (width, height//2), 1)
    pygame.draw.line(screen, (0, 0, 0), (width//2, 0), (width//2, height), 1)

    #drawing circle
    pygame.draw.circle(screen, (255, 105, 180), (x, y), radius)  
    
    # Axis labels
    x_label = font.render("X-axis", True, (0, 0, 0))
    y_label = font.render("Y-axis", True, (0, 0, 0))

    # Position labels
    screen.blit(x_label, (width - 70, height//2 + 5))   # X-axis label
    screen.blit(y_label, (width//2 + 5, 10))            # Y-axis label
    pygame.display.update()
    clock.tick(60)