import pygame

def start_input_capture():
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
            if event.type in (pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP, pygame.JOYHATMOTION):
                print("Joystick event:", event)

            # Capture keyboard events
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                print("Keyboard event:", event)

    # Clean up
    for joystick in joysticks:
        joystick.quit()

    pygame.joystick.quit()
    pygame.quit()

if __name__ == "__main__":
    start_input_capture()
