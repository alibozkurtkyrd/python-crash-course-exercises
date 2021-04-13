import sys
import pygame
from raindrop import Raindrop

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ayarlar, screen, raindrops):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop
    screen.fill(ayarlar.bg_color)

    raindrops.draw(screen)

    # Make the most recently drawn screen visible
    pygame.display.flip()

def get_number_raindrop_x(ayarlar, raindrop_width):
    """Determine the number of raindrop that fit in a row."""
    available_space_x = ayarlar.screen_width - (raindrop_width * 0.6)
    number_raindrop_x = int(available_space_x / (1.0 * raindrop_width))
    return number_raindrop_x

def get_number_rows(ayarlar, raindrop_height):
    """Determine the number of rows of raindrops that fit on the screen."""
    available_space_y = ayarlar.screen_height - (0.5 * raindrop_height)
    number_rows = int(available_space_y / (1.0 * raindrop_height))
    return number_rows

def create_raindrop(ayarlar, screen, raindrops, raindrop_number, row_number):
    """Create a raindrop and place it in the row."""
    raindrop = Raindrop(ayarlar, screen)
    raindrop_width = raindrop.rect.width
    raindrop.x = 0.5 * raindrop_width + raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrop.y = 0.5 * raindrop.rect.height + raindrop.rect.height * row_number
    #raindrop.rect.y = raindrop.y # look at line 38 we need to store x direction but why we do not need y direction.
    raindrops.add(raindrop)

def create_fleet(ayarlar, screen, raindrops):
    """Create a full fleet of aliens."""
    # Create a raindrop and find the number of raindrops in a row.
    raindrop = Raindrop(ayarlar, screen)
    number_raindrops_x = get_number_raindrop_x(ayarlar, raindrop.rect.width)

    number_rows = get_number_rows(ayarlar, raindrop.rect.height)

    # Create the first row of raindrops.
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            create_raindrop(ayarlar, screen, raindrops, raindrop_number,
                            row_number)
            
def check_fleet_edges(ayarlar, raindrops, screen):
    """Respond appropriately if any aliens have reached an edge."""
    
    for raindrop in raindrops.sprites():
    
        if raindrop.check_edges():
            raindrops.remove(raindrop)
            

def update_raindrops(ayarlar, raindrops, screen):
    """Update the positions of all raindrops in the flee."""
    check_fleet_edges(ayarlar, raindrops, screen)
    if len(raindrops) == 0:
        create_fleet(ayarlar, screen, raindrops)
    raindrops.update()

