import sys

import pygame

from star import Star

from random import randint

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
     

def update_screen(settings, screen, stars):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)
    
    stars.draw(screen)
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def get_number_stars_x(settings, star_width):
    """Determine the number of stars that fit in a row."""
    available_space_x = settings.screen_width - 1 * star_width # I multiplying by 1 rather 2 because star.py line 18 we multiplied with 0.5 rather than 2
    number_stars_x = int(available_space_x / ( 1.5 * star_width))
    return number_stars_x

def get_number_rows(settings, star_height):
    """Determine the number of rows of stars that fit on the screen."""
    available_space_y = (settings.screen_height)
                         #( 1 * star_height)) I am not subsratting this because image size is so big
    number_rows = int(available_space_y / (1.5 * star_height))
    return number_rows

def create_star(settings, screen, stars, star_number, row_number):
    """Create a star and place it in the row."""
    star = Star(settings, screen)
    star_width = star.rect.width
    star.x = star_width + 1 * star_width * star_number
    star.rect.x = star.x                                        # I have to multiplying by 1.5 rather than 2 because image is so big
    star.rect.y = star.rect.height + 1 * star.rect.height * row_number
    stars.add(star)

def create_fleet(settings, screen, stars):
    """Create a full fleet of aliens."""
    # Create a star and find the number of stars in a row.
    star = Star(settings, screen)
    number_stars_x = get_number_stars_x(settings, star.rect.width)
    random_number_1 = randint(1, number_stars_x)
    print("x ekseni-random_1:", random_number_1)
    
    number_rows = get_number_rows(settings, star.rect.height)
    random_number_2 = randint(1, number_rows)
    print("y ekseni random_2", random_number_2)

    # Create the first row of stars.
    for row_number in range(random_number_2):
        for star_number in range(random_number_1):
            create_star(settings, screen, stars, star_number,
                        row_number)
