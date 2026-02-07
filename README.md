# Karkulačka!

Karkulačka! je 2D dobrodružná hra inspirovaná českými pohádkami.  
Hráč se ujme role Matěje Karkuláka – učedníka z Pohádkového archivu, který omylem vypustil temnou inkoustovou bytost.  
Každý level reprezentuje známou pohádku a vaším úkolem je obnovit rovnováhu tím, že projdete světem pohádek, posbíráte kouzelné artefakty, porazíte bosse a znovu sepíšete zkažené příběhy.

Tento projekt obsahuje první prototyp hry postavený na [Pygame](https://www.pygame.org/). Kód je strukturován tak, aby bylo možné hru dále rozšiřovat o další pohádky, nepřátele, kouzla a předměty.

## Struktura projektu

```
├── assets/             # Grafické a zvukové podklady
│   └— main_menu.png  # Obrázek pro hlavní menu (poskytnutý uživatelem)
├── src/                # Zdrojové kódy hry
│   ├── main.py        # Spouštěcí skript a hlavní smyčka
│   ├── game.py        # Třída Game, která řídí stavy hry (menu, úroveň)
│   ├— player.py      # Třída Player pro hráče
│   ├— enemy.py       # Jednoduchá implementace nepřítele
│   ├— level.py       # Třía Level, generuje mapu a spravuje entit
│   ├— spells.py      # Základní systém kouzel
│   └— items.py       # Ukázkové předměty# Karkulačka!

Karkulačka! je 2D dobrodružná hra inspirovaná českými pohádkami.  
Hráč se ujme role Matěje Karkuláka – učedníka z Pohádkového archivu, který omylem vypustil temnou inkoustovou bytost.  
Každý level reprezentuje známou pohádku a vaším úkolem je obnovit rovnováhu tím, že projdete světem pohádek, posbíráte kouzelné artefakty, porazíte bosse a znovu sepíšete zkažené příběhy.

Tento projekt obsahuje první prototyp hry postavený na [Pygame](https://www.pygame.org/). Kód je strukturován tak, aby bylo možné hru dále rozšiřovat o další pohádky, nepřátele, kouzla a předměty.

## Struktura projektu

```
├—— assets/             # Grafické a zvukové podklady
│   └— main_menu.png  # Obrázek pro hlavní menu (poskytnutý uživatelem)
├—— src/                # Zdrojové kódy hry
│   ├— main.py        # Spouštěcí skript a hlavní smyčka
│   ├— game.py        # Třída Game, která řídí stavy hry (menu, úroveň)
│   ├— player.py      # Třída Player pro hráče
│   ├— enemy.py       # Jednoduchá implementace nepřítele
│   ├— level.py       # Třía Level, generuje mapu a spravuje entit
│   ├— spells.py      # Základní systém kouzel
│   └— items.py       # Ukázkové předměty
├—— README.md          # Tento soubor s popisem
└— requirements.txt   # Seznam závislostí
```

### Spuštění hry

1. Ujistěte se, že máte nainstalován Python 3.9 nebo novější.  
2. Nainstalujte závislosti pomocí příkazu:

   ```bash
   pip install -r requirements.txt
   ```

3. Spusťte hru z adresáře `src`:

   ```bash
   python3 main.py
   ```

### Ovládání

| Akce                | Klávesnice        |
|--------------------|-------------------|
| Pohyb              | **W**, **A**, **S**, **D** |
| Útok (kouzlo)      | Levé tlačitko myši |
| Interakce          | **E**             |
| Pauza/Menu         | **Esc**           |

Podrobnější ovládání a možnost remapování lze snadno doplnit v souboru `game.py`.

### Poznámka k prototypu

Tento prototyp se zaměřuje na základní mechaniky: zobrazení hlavního menu, jednoduchý pohyb hráče, základního nepřátele a sbírání předmětů. Kód je modularizovaný tak, aby bylo jednoduché přidávat nové funkce podle rozsáhlého návrhu (další úroúvně, kouzla, předměty, mini‑hry atp.).
├── README.md          # Tento soubor s popisem
└— requirements.txt   # Seznam závislostí
```

### Spuštění hry

1. Ujistěte se, že máte nainstalován Python 3.9 nebo novější.  
2. Nainstalujte závislosti pomocí příkazu:

   ```bash
   pip install -r requirements.txt
   ```

3. Spusťte hru z adresáře `src`:

   ```bash
   python3 main.py
   ```

### Ovládání

| Akce                | Klávesnice        |
|--------------------|-------------------|
| Pohyb              | **W**, **A**, **S**, **D** |
| Útok (kouzlo)      | Levé tlačitko myši |
| Interakce          | **E**             |
| Pauza/Menu         | **Esc**           |

Podrobnější ovládání a možnost remapování lze snadno doplnit v souboru `game.py`.

### Poznámka k prototypu

Tento prototyp se zaměřuje na základní mechaniky: zobrazení hlavního menu, jednoduchý pohyb hráče, základního nepřátele a sbírání předmětů. Kód je modularizovaný tak, aby bylo jednoduché přidávat nové funkce podle rozsáhlého návrhu (další úroúvně, kouzla, předměty, mini‑hry atp.).
