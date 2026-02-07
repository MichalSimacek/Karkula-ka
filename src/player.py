"""Player entity for Karkulačka! prototype.

Handles user input, movement, health, mana and spellcasting. The player can
move using WASD, cast a basic spell with the left mouse button and pick up
items that restore health or mana.
"""

from __future__ import annotations

import pygame
from typing import Tuple, List

from spells import Projectile, BasicSpell


class Player:
    """Represents the player's character."""

    def __init__(self, pos: Tuple[int, int], size: int = 32) -> None:
        self.x, self.y = pos
        self.size = size
        self.rect = pygame.Rect(self.x - size // 2, self.y - size // 2, size, size)
        self.color = (220, 20, 60)
        self.speed = 200.0  # pixels per second
        self.health = 100
        self.max_health = 100
        self.mana = 50
        self.max_mana = 50
        self.projectiles: List[Projectile] = []
        self.basic_spell = BasicSpell()
        self.delta_time = 0.016

    def handle_event(self, event: pygame.event.EventType) -> None:
        """Handle input events for movement and spellcasting."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Cast basic spell on left click
            mouse_pos = pygame.mouse.get_pos()
            proj = self.basic_spell.cast((self.rect.centerx, self.rect.centery), mouse_pos)
            if proj is not None:
                self.projectiles.append(proj)

    def update(self, width: int, height: int) -> None:
        """Update the player's position and projectiles."""
        # Compute delta time for consistent movement
        self.delta_time = pygame.time.get_ticks() / 1000.0  # naive but works for small prototype
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_s]:
            dy += 1
        if keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_d]:
            dx += 1
        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.7071
            dy *= 0.7071
        self.x += dx * self.speed * (1/60)  # 1/60 approximates delta time step
        self.y += dy * self.speed * (1/60)
        # Keep player inside screen boundaries
        self.x = max(self.size // 2, min(width - self.size // 2, self.x))
        self.y = max(self.size // 2, min(height - self.size // 2, self.y))
        # Update rect position
        self.rect.center = (int(self.x), int(self.y))
        # Update projectiles
        for proj in self.projectiles[:]:
            proj.update()
            # Remove projectile if it goes off screen
            if not (0 <= proj.x <= width and 0 <= proj.y <= height):
                self.projectiles.remove(proj)

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the player and its projectiles."""
        pygame.draw.rect(surface, self.color, self.rect)
        for proj in self.projectiles:
            proj.draw(surface)

    def take_damage(self, amount: float) -> None:
        """Reduce the player's health by the given amount."""
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount: int) -> None:
        """Restore health up to maximum."""
        self.health = min(self.max_health, self.health + amount)

    def restore_mana(self, amount: int) -> None:
        """Restore mana up to maximum."""
        self.mana = min(self.max_mana, self.mana + amount)
