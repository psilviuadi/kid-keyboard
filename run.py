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
text = font.render("Have fun!", True, (255, 255, 255))

running = True
while running:
    screen.fill((0, 0, 0))
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

pygame.quit()
sys.exit()