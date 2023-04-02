import pygame
import json
import requests

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

# Server URL
SERVER_URL = "http://your_server_url.com/data_receiver"

# Function to send data to the server
def send_data_to_server(data):
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(SERVER_URL, data=json.dumps(data), headers=headers)
        print(f"Data sent. Server response: {response.status_code}")
    except Exception as e:
        print(f"Error sending data to server: {e}")

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Capture joystick events
        if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBALLMOTION or event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP or event.type == pygame.JOYHATMOTION:
            print("Joystick event:", event)
            send_data_to_server({"joystick_event": str(event)})

        # Capture keyboard events
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            print("Keyboard event:", event)
            send_data_to_server({"keyboard_event": str(event)})

# Clean up
for joystick in joysticks:
    joystick.quit()

pygame.joystick.quit()
pygame.quit()
