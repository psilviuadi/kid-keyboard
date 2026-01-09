import pygame
import sys

pygame.init()
pygame.mixer.init()

# Load a sound (replace with your own .wav file)
sound = pygame.mixer.Sound("click.wav")

# Create fullscreen window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Kid Input Sandbox")

font = pygame.font.SysFont(None, 60)
message = "Have fun!"

running = True
while running:
    screen.fill((0, 0, 0))
    text = font.render(message, True, (255, 255, 255))
    screen.blit(text, (100, 100))
    pygame.display.flip()

    for event in pygame.event.get():
        # Exit combo: Alt + F4
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            if event.key == pygame.K_F4 and (mods & pygame.KMOD_ALT):
                running = False


        # Play sound on any key or mouse press
        if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
            sound.play()
            if len(message) > 50:
                message = "GO"
            if event.type == pygame.MOUSEBUTTONDOWN:
                message += " Click"
            else:
                key_name = pygame.key.name(event.key)
                if len(key_name) == 1:
                    # Single character key
                    message += key_name.upper()
                else:
                    # Special key (home, space, return, etc.)
                    message += " " + key_name.upper()

pygame.quit()
sys.exit()