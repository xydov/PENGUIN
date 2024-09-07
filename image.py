from PIL import Image
import pygame

def display_image_pygame(image_path):
    """Display an image using Pygame."""
    pygame.init()
    img = pygame.image.load(image_path)
    screen = pygame.display.set_mode(img.get_size())
    screen.blit(img, (0, 0))
    pygame.display.flip()
    pygame.time.wait(5000)  # Display the image for 5 seconds
    pygame.quit()

# Example usage
display_image_pygame("./pictures/resized_logo.png")

