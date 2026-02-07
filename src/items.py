"""Definitions of collectible items for Karkulačka! prototype.

Items provide bonuses to the player when picked up. For this prototype we
implement a simple health potion. Future items can grant mana, buffs or
unlock abilities inspired by Czech fairy tales.
"""

from __future__ import annotations

import pygame
from typing import Tuple


class HealthPotion:
    """An item that restores a portion of the player's health upon pickup."""

    def __init__(self, pos: Tuple[int, int], size: int = 16, heal_amount: int = 20) -> None:
        self.x, self.y = pos
        self.size = size
        self.heal_amount = heal_amount
        self.rect = pygame.Rect(self.x - size // 2, self.y - size // 2, size, size)
        self.color = (200, 50, 200)

    def draw(self, surface: pygame.Surface) -> None:
        """Render the health potion as a small square."""
        pygame.draw.rect(surface, self.color, self.rect)

    def on_pickup(self, player: 'Player') -> None:
        """Heal the player when picked up."""
        player.heal(self.heal_amount)
