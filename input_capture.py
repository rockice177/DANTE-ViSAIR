import pygame

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Set up joystick support
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

joysticks = [pygame.joystick.Joystick(x) for x in range(joystick_count)]
for joystick in joysticks:
    joystick.init()

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Capture joystick events
        if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBALLMOTION or event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP or event.type == pygame.JOYHATMOTION:
            print("Joystick event:", event)

        # Capture keyboard events
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            print("Keyboard event:", event)

# Clean up
for joystick in joysticks:
    joystick.quit()

pygame.joystick.quit()
pygame.quit()
