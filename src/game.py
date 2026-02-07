"""Core game loop and state management for Karkulačka! prototype.

The Game class encapsulates the main game state, including the active level,
player, enemies and UI. It handles updating and drawing of all game objects.

"""

from __future__ import annotations

import pygame
from typing import Optional

from level import Level


class Game:
    """High level controller for game state and rendering."""

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.level: Optional[Level] = None
        self._init_level()
        # UI fonts
        self.font = pygame.font.Font(None, 24)
        self.big_font = pygame.font.Font(None, 32)

    def _init_level(self) -> None:
        """Initialize a new level and its entities."""
        self.level = Level(self.screen.get_size())

    def handle_event(self, event: pygame.event.EventType) -> None:
        """Handle input events and forward to active entities.

        Args:
            event: Pygame event object.
        """
        if self.level is not None:
            self.level.handle_event(event)

    def update(self) -> None:
        """Update the game state each frame."""
        if self.level is not None:
            self.level.update()

    def draw(self) -> None:
        """Render the current frame to the screen."""
        if self.level is None:
            return
        # Clear screen with dark colour
        self.screen.fill((20, 20, 20))
        # Draw the level and its entities
        self.level.draw(self.screen)
        # Draw UI (HP bar, mana bar etc.)
        self._draw_ui()

    def _draw_ui(self) -> None:
        """Render simple UI elements such as health and mana bars."""
        if self.level is None or self.level.player is None:
            return
        player = self.level.player
        # Health bar
        bar_width, bar_height = 200, 20
        x, y = 10, 10
        # Background bar
        pygame.draw.rect(self.screen, (60, 60, 60), (x, y, bar_width, bar_height))
        # Filled portion based on current health
        health_ratio = max(player.health, 0) / player.max_health
        pygame.draw.rect(
            self.screen,
            (200, 50, 50),
            (x, y, int(bar_width * health_ratio), bar_height),
        )
        health_text = self.font.render(f"HP: {int(player.health)}/{player.max_health}", True, (255, 255, 255))
        self.screen.blit(health_text, (x + 5, y))
        # Mana bar just below health
        y += bar_height + 5
        pygame.draw.rect(self.screen, (60, 60, 60), (x, y, bar_width, bar_height))
        mana_ratio = max(player.mana, 0) / player.max_mana
        pygame.draw.rect(
            self.screen,
            (50, 50, 200),
            (x, y, int(bar_width * mana_ratio), bar_height),
        )
        mana_text = self.font.render(f"Mana: {int(player.mana)}/{player.max_mana}", True, (255, 255, 255))
        self.screen.blit(mana_text, (x + 5, y))
