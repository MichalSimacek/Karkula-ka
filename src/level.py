"""Level module containing a simple procedurally generated room.

This implementation is intentionally lightweight. A `Level` holds a player,
enemies and items, and is responsible for updating and drawing them. In a
complete version of the game, this module would generate rooms, handle
transitions, puzzles and boss fights inspired by Czech fairy tales.
"""

from __future__ import annotations

import random
import pygame
from typing import List, Tuple

from player import Player
from enemy import Enemy
from items import HealthPotion


class Level:
    """Represents a single room or level in the game."""

    def __init__(self, screen_size: Tuple[int, int]) -> None:
        self.width, self.height = screen_size
        self.player = Player(pos=(self.width // 2, self.height // 2))
        # Spawn a handful of enemies at random positions
        self.enemies: List[Enemy] = []
        for _ in range(5):
            x = random.randint(50, self.width - 50)
            y = random.randint(50, self.height - 50)
            self.enemies.append(Enemy((x, y)))
        # Place some health potions
        self.items: List[HealthPotion] = []
        for _ in range(3):
            x = random.randint(50, self.width - 50)
            y = random.randint(50, self.height - 50)
            self.items.append(HealthPotion((x, y)))

    def handle_event(self, event: pygame.event.EventType) -> None:
        """Delegate input events to the player."""
        self.player.handle_event(event)

    def update(self) -> None:
        """Update all entities in the level."""
        self.player.update(self.width, self.height)
        for enemy in self.enemies:
            enemy.update(self.player)
        # Check collisions between player and enemies
        for enemy in self.enemies:
            if enemy.rect.colliderect(self.player.rect):
                self.player.take_damage(1 * self.player.delta_time)  # continuous damage
        # Check collisions with items
        for item in self.items[:]:
            if item.rect.colliderect(self.player.rect):
                item.on_pickup(self.player)
                self.items.remove(item)

        # Check collisions between player's projectiles and enemies
        for proj in self.player.projectiles[:]:
            proj_rect = pygame.Rect(int(proj.x - proj.radius), int(proj.y - proj.radius), proj.radius * 2, proj.radius * 2)
            for enemy in self.enemies[:]:
                if enemy.rect.colliderect(proj_rect):
                    # Remove enemy and projectile
                    try:
                        self.player.projectiles.remove(proj)
                    except ValueError:
                        pass
                    try:
                        self.enemies.remove(enemy)
                    except ValueError:
                        pass
                    break

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the level background and all entities."""
        # Draw simple background
        surface.fill((34, 40, 49))
        # Draw items
        for item in self.items:
            item.draw(surface)
        # Draw enemies
        for enemy in self.enemies:
            enemy.draw(surface)
        # Draw player on top
        self.player.draw(surface)
