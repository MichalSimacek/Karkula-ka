"""Simple enemy implementation for Karkulačka! prototype.

Enemies wander around the screen and slowly home towards the player. They
inflict damage when touching the player. When hit by a projectile, they are
removed. More complex behaviour and unique boss mechanics can be added
incrementally.
"""

from __future__ import annotations

import math
import random
import pygame
from typing import Tuple


class Enemy:
    """Represents a basic enemy that moves towards the player."""

    def __init__(self, pos: Tuple[int, int], size: int = 28) -> None:
        self.x, self.y = pos
        self.size = size
        self.rect = pygame.Rect(self.x - size // 2, self.y - size // 2, size, size)
        self.color = (0, 150, 80)
        self.speed = 80.0  # slower than player
        # Random jitter to avoid uniform behaviour
        self.wander_timer = random.uniform(0.5, 2.0)

    def update(self, player: 'Player') -> None:
        """Move slightly towards the player each frame."""
        # Simple homing behaviour: vector from enemy to player
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx /= dist
            dy /= dist
        # Add a bit of randomness so that enemies don't move in perfect lines
        jitter = (random.uniform(-0.3, 0.3), random.uniform(-0.3, 0.3))
        self.x += (dx + jitter[0]) * self.speed * (1/60)
        self.y += (dy + jitter[1]) * self.speed * (1/60)
        self.rect.center = (int(self.x), int(self.y))

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the enemy as a colored square."""
        pygame.draw.rect(surface, self.color, self.rect)
