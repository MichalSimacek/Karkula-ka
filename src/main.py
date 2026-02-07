"""Entry point for the Karkulačka! game prototype.

This module sets up the Pygame window, displays a simple main menu and starts the
game loop. The menu uses an image provided by the user as a background.
When the player presses a key or clicks the mouse, the game begins.
"""

import os
import sys
import pygame

# Add the src directory to the import path when running from project root
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from game import Game


def load_main_menu_image() -> pygame.Surface:
    """Load the main menu background image.

    Returns:
        pygame.Surface: The loaded image surface.
    """
    assets_path = os.path.join(os.path.dirname(current_dir), "assets")
    image_path = os.path.join(assets_path, "main_menu.png")
    try:
        image = pygame.image.load(image_path).convert_alpha()
    except FileNotFoundError:
        # If the image is missing, fill the screen with a placeholder colour
        image = pygame.Surface((800, 600))
        image.fill((50, 50, 50))
    return image


def main() -> None:
    """Initialize Pygame and run the main menu/game loop."""
    pygame.init()
    pygame.display.set_caption("Karkulačka! – prototyp")

    # Window size and display
    width, height = 960, 540
    screen = pygame.display.set_mode((width, height))

    # Load background for menu
    menu_image = load_main_menu_image()
    menu_image = pygame.transform.scale(menu_image, (width, height))

    # Font for menu text
    font = pygame.font.Font(None, 36)

    clock = pygame.time.Clock()
    running = True
    game_started = False

    # Instantiate the Game object here but don't start updating until user starts
    game = Game(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not game_started and event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                game_started = True
            if game_started:
                # Forward input events to the game
                game.handle_event(event)

        if not game_started:
            # Draw menu
            screen.blit(menu_image, (0, 0))
            title_surf = font.render("Karkulačka!", True, (255, 255, 255))
            prompt_surf = font.render("Stiskněte libovolnou klávesu pro start", True, (255, 255, 255))
            screen.blit(title_surf, ((width - title_surf.get_width()) // 2, height // 4))
            screen.blit(prompt_surf, ((width - prompt_surf.get_width()) // 2, height // 2))
        else:
            game.update()
            game.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
