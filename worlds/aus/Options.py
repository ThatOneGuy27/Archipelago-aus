from dataclasses import dataclass
from Options import Choice, Option, Toggle, Range, PerGameCommonOptions, DeathLinkMixin

class IsCool(Toggle):
    """Determines whether the user is cool and checked this option. [Testing only, no gameplay effect.]"""
    display_name = "Is Cool"


class GoldOrbsRequired(Range):
    """
    How many gold orbs are required for BlackCastle, and thus, to goal
    
    Must be between 0 and 10.
    """
    display_name = "Gold Orb Requirement"
    default = 7
    range_start = 0
    range_end = 10
    
class DifficultySelector(Range):
    """
    The difficulty the game will be set to.
    0 = Simple
    1 = Regular
    2 = Difficult
    3 = Masterful
    4 = Insanity (Masterful + one hit kill)
    
    This game can be VERY difficult, only choose a higher difficulty if you know what you're doing!
    """
    display_name = "Difficulty"
    default = 1
    range_start = 0
    range_end = 4
    
    
@dataclass
class AUSOptions(PerGameCommonOptions, DeathLinkMixin):
    is_cool: IsCool
    gold_orbs_required: GoldOrbsRequired
    difficulty: DifficultySelector
  
  