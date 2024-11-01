import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Map import Map
from Surface import Surface

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import sprites
from display import WINDOW_WIDTH as x
from display import WINDOW_HEIGHT as y

map1 = Map(sprites.Map_sprites)
map1.list_of_surface.append(Surface([(0, 2 * y / 3), (x / 16, 2 * y / 3), (x / 16, y), (0, y), (0, 2 * y / 3)]))                        #1
map1.list_of_surface.append(Surface([(x / 8, 2 * y / 3), (3 * x / 16, 2 * y / 3), (3 * x / 16, 19 * y / 24), (x / 8, 19 * y / 24),      #2
                                     (x / 8, 2 * y / 3)]))                                                                                          
map1.list_of_surface.append(Surface([(x / 8, 7 * y / 8), (7 * x / 16, 7 * y / 8), (11 * x / 24, 19 * y / 24),                            #3
                                     (13 * x / 24, 19 * y / 24), (9 * x / 16, 7 * y / 8), (7 * x / 8, 7 * y / 8), (7 * x / 8, y), 
                                     (x / 8, y), (x / 8, 7 * y / 8)]))
map1.list_of_surface.append(Surface([(x / 24, y / 3), (x / 16, y / 3), (x / 16, 11 * y / 24), (x / 8, 11 * y / 24), (x / 8, y / 2), 
                                     (x / 24, y / 2), (x / 24, y / 3)])) #4
map1.list_of_surface.append(Surface([(3 * x / 16, 11 * y / 24), (5 * x / 16, 11 * y / 24), (5 * x / 16, y / 3), (x / 3, y / 3), 
                                     (x / 3, y / 2), (3 * x / 16, y / 2), (3 * x / 16, 11 * y / 24)])) #5
map1.list_of_surface.append(Surface([(7 * x / 24, 2 * y / 3), (x / 3, 2 * y / 3), (3 * x / 8, y / 2), (11 * x / 24, y / 2), 
                                     (11 * x / 24, 7 * y / 12), (5 * x / 12, 7 * y / 12), (3 * x / 8, 3 * y / 4), (7 * x / 24, 3 * y / 4), (7 * x / 24, 2 * y / 3)])) #6
map1.list_of_surface.append(Surface([(1 * x / 8, 1 * y / 6), (13 * x / 48, 1 * y / 6), (13 * x / 48, 1 * y / 3), (1 * x / 8, 1 * y / 3), 
                                     (1 * x / 8, 1 * y / 6)])) #7
map1.list_of_surface.append(Surface([(1 * x / 3, 1 * y / 8), (5 * x / 12, 1 * y / 8), (5 * x / 12, 1 * y / 6), (1 * x / 3, 1 * y / 6), 
                                     (1 * x / 3, 1 * y / 8)])) #8
map1.list_of_surface.append(Surface([(11 * x / 24, 7 * y / 24), (13 * x / 24, 7 * y / 24), (13 * x / 24, 3 * y / 8), 
                                     (11 * x / 24, 3 * y / 8), (11 * x / 24, 7 * y / 24)])) #9
map1.list_of_surface.append(Surface([(7 * x / 12, 1 * y / 8), (2 * x / 3, 1 * y / 8), (2 * x / 3, 1 * y / 6), (7 * x / 12, 1 * y / 6), 
                                     (7 * x / 12, 1 * y / 8)])) #10
map1.list_of_surface.append(Surface([(875 * x / 1200, 100 * y / 600), (1050 * x / 1200, 100 * y / 600), (1050 * x / 1200, 200 * y / 600), 
                                     (875 * x / 1200, 200 * y / 600), (875 * x / 1200, 100 * y / 600)])) #11
map1.list_of_surface.append(Surface([(2 * x / 3, 1 * y / 3), (11 * x / 16, 1 * y / 3), (11 * x / 16, 11 * y / 24), 
                                     (13 * x / 16, 11 * y / 24), (13 * x / 16, 1 * y / 2), (2 * x / 3, 1 * y / 2), (2 * x / 3, 1 * y / 3)])) #12
map1.list_of_surface.append(Surface([(35 * x / 40, 11 * y / 24), (15 * x / 16, 11 * y / 24), (15 * x / 16, 1 * y / 3), 
                                     (23 * x / 24, 1 * y / 3), (23 * x / 24, 1 * y / 2), (35 * x / 40, 1 * y / 2), 
                                     (35 * x / 40, 11 * y / 24)])) #13
map1.list_of_surface.append(Surface([(13 * x / 24, 1 * y / 2), (5 * x / 8, 1 * y / 2), (2 * x / 3, 2 * y / 3), (17 * x / 24, 2 * y / 3), 
                                     (17 * x / 24, 3 * y / 4), (5 * x / 8, 3 * y / 4), (7 * x / 12, 7 * y / 12), (13 * x / 24, 7 * y / 12), 
                                     (13 * x / 24, 1 * y / 2)])) #14
map1.list_of_surface.append(Surface([(39 * x / 48, 2 * y / 3), (7 * x / 8, 2 * y / 3), (7 * x / 8, 19 * y / 24), (39 * x / 48, 19 * y / 24), 
                                     (39 * x / 48, 2 * y / 3)])) #15
map1.list_of_surface.append(Surface([(15 * x / 16, 2 * y / 3), (1 * x, 2 * y / 3), (1 * x, 1 * y), (15 * x / 16, 1 * y), 
                                     (15 * x / 16, 2 * y / 3)])) #16