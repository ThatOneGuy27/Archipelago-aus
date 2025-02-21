from BaseClasses import MultiWorld, Region
from .Names import *

def link_aus_areas(world: MultiWorld, player: int):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# (Region name, list of exits)
aus_regions = [
    (R_START_REGION, [C_NIGHTCLIMB, C_DEEPDIVE, C_MOUNTSIDE, C_SKYSAND, C_FARFALL]),
    (A_NIGHTCLIMB, []),
    (A_DEEPDIVE, [C_FIRECAGE, C_BLANCLAND, C_DEEPDIVE_RIGHT]),
    (A_FIRECAGE, []),
    (A_MOUNTSIDE, [C_THE_CURTAIN, C_DARK_GROTTO]),
    (A_THE_CURTAIN, [C_LONGBEACH_UPPER]),
    (A_SKYSAND, []),
    (A_DARK_GROTTO, [C_LONGBEACH_MIDDLE]),
    (A_FARFALL, [C_STRANGECASTLE, C_THE_BOTTOM]),
    (A_STRANGECASTLE, []),
    (A_THE_BOTTOM, []),
    (A_BLANCLAND, []),
    (R_DEEPDIVE_RIGHT, [C_LONGBEACH_LOWER]),
    (A_LONGBEACH, [C_BLACKCASTLE]),
    (A_BLACKCASTLE, []),
]

# (Entrance, region pointed to)
mandatory_connections = [
    (C_NIGHTCLIMB, A_NIGHTCLIMB),
    (C_DEEPDIVE, A_DEEPDIVE),
    (C_MOUNTSIDE, A_MOUNTSIDE),
    (C_SKYSAND, A_SKYSAND),
    (C_FARFALL, A_FARFALL),
    (C_FIRECAGE, A_FIRECAGE),
    (C_BLANCLAND, A_BLANCLAND),
    (C_DEEPDIVE_RIGHT, R_DEEPDIVE_RIGHT),
    (C_THE_CURTAIN, A_THE_CURTAIN),
    (C_DARK_GROTTO, A_DARK_GROTTO),
    (C_STRANGECASTLE, A_STRANGECASTLE),
    (C_THE_BOTTOM, A_THE_BOTTOM),
    (C_LONGBEACH_UPPER, A_LONGBEACH),
    (C_LONGBEACH_MIDDLE, A_LONGBEACH),
    (C_LONGBEACH_LOWER, A_LONGBEACH),
    (C_BLACKCASTLE, A_BLACKCASTLE),
]
