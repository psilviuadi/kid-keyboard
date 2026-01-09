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
    
    # Handle multi-line rendering
    lines = message.split('\n')
    y_offset = 100
    for line in lines:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (100, y_offset))
        y_offset += 70
    
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
            lines = message.split('\n')
            if len(lines[-1]) > 50:
                message += "\n"
            if len(lines) > 10:
                message = ""
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