# This file exists to unify all item, location, region and entrance names across
# the project, to make renaming easier, more consistent and less error-prone.

# Item names

I_JUMP_UPGRADE = "Jump Upgrade"  # "Jump Upgrade 1/2/3" in vanilla
I_RED_ENERGY = "Red Energy"  # "Energy Jump 1" in vanilla
I_LUCKY_POTS = "Lucky Pots"
I_DOUBLE_JUMP = "Double Jump Upgrade"  # "Double Jump" and "Double Jump Upgrade 1/2" in vanilla
I_DUCKING = "Ducking"  # previously known as "Duck"
I_STICKING = "Progressive Stick Slide"  # "Sticking" and "Stick Slide" in vanilla
I_TELEPORT = "Teleport"
I_DIVE_BOMB = "Dive Bomb"  # previously known as "Smash"
I_SHOOT_FIRE = "Progressive Fire Shot"  # "Shoot Fire" and "Long Shots" in vanilla
I_LONG_SHOTS = "Long Shots"  # unused atm
I_YELLOW_ENERGY = "Yellow Energy"  # "Energy Jump 2" in vanilla
I_HATCH = "Hatch"
I_AIR_UPGRADE = "Air Upgrade"  # previously known as "Extra Air Capacity"
I_MAGNETISM = "Magnetism"  # previously known as "Money Magnet"
I_SHOOT_ICE = "Ice Shot"  # previously known as "Ice Shot"
I_TOUGHNESS = "Toughness"  # "Toughness 1/2/3" in vanilla
I_HEART = "Heart"
I_GOLD_ORB = "Gold Orb"
I_FLOWER = "Flower"

# Area names

A_BLACKCASTLE = "BlackCastle"
A_BLANCLAND = "BlancLand"
A_BONUS = "Bonus"
A_THE_BOTTOM = "The Bottom"
A_CLOUDRUN = "CloudRun"
A_COLDKEEP = "ColdKeep"
A_THE_CURTAIN = "The Curtain"
A_DARK_GROTTO = "Dark Grotto"
A_DEEPDIVE = "DeepDive"
A_DEEPTOWER = "DeepTower"
A_FARFALL = "FarFall"
A_FINAL_CLIMB = "Final Climb"
A_FIRECAGE = "FireCage"
A_GROTTO = "Grotto"
A_HIGHLANDS = "HighLands"
A_ICECASTLE = "IceCastle"
A_LIBRARY = "Library"
A_LONGBEACH = "LongBeach"
A_MOUNTSIDE = "MountSide"
A_NIGHTCLIMB = "NightClimb"
A_NIGHTWALK = "NightWalk"
A_RAINBOWDIVE = "RainbowDive"
A_SKYLANDS = "SkyLands"
A_SKYSAND = "SkySand"
A_SKY_TOWN = "Sky Town"
A_STAIRCASE = "Staircase"
A_STONECASTLE = "StoneCastle"
A_STRANGECASTLE = "StrangeCastle"
A_UNDERTOMB = "UnderTomb"

# Extra region names

R_START_REGION = "Menu"
R_DEEPDIVE_RIGHT = "DeepDive Right"

# Using a function to format location names means we can change it freely at any time,
# and not have to go through the entire codebase to update each location name.
def _locname(area, name):
    return f"{area}: {name}"

# Location names

L_SKY_TOWN_ASTROCRASH = _locname(A_SKY_TOWN, "AstroCrash High Score")
L_SKY_TOWN_JUMPBOX = _locname(A_SKY_TOWN, "JumpBox High Score")
L_SKY_TOWN_KEEPGOING = _locname(A_SKY_TOWN, "Keep Going High Score")

L_BLACKCASTLE_BOSS = _locname(A_BLACKCASTLE, "Ninja 2 Boss Drop")
L_BLACKCASTLE_FLOWER = _locname(A_BLACKCASTLE, "Final Save (Flower)")
L_BLACKCASTLE_REDBLOCKS = _locname(A_BLACKCASTLE, "Hidden Under Red Blocks")  # This could be better, but it's fine for now.

L_BLANCLAND_FREEZE = _locname(A_BLANCLAND, "Bottom Left Triangle Freeze Climb")
L_BLANCLAND_KILL = _locname(A_BLANCLAND, "Top Left Kill Triangles")
L_BLANCLAND_POSTBOSS = _locname(A_BLANCLAND, "After BlancBlock")
L_BLANCLAND_BOSS = _locname(A_BLANCLAND, "BlancBlock Boss Drop")
L_BLANCLAND_FLOWER = _locname(A_BLANCLAND, "Entrance Save (Flower)")

L_BONUS_1 = _locname(A_BONUS, "Prize 1")
L_BONUS_2 = _locname(A_BONUS, "Prize 2")

L_THE_BOTTOM_CLOUD = _locname(A_THE_BOTTOM, "Near Pink Cloud")
L_THE_BOTTOM_FLOWER = _locname(A_THE_BOTTOM, "The Very Bottom (Flower)")

L_CLOUDRUN_FLOWER = _locname(A_CLOUDRUN, "Entrance Save (Flower)")
L_CLOUDRUN_UNDER = _locname(A_CLOUDRUN, "Early Balloon Underhang")
L_CLOUDRUN_MIDDLE = _locname(A_CLOUDRUN, "Middle Save")
L_CLOUDRUN_BOSS = _locname(A_CLOUDRUN, "Fluffy XR-9 Boss Drop")
L_CLOUDRUN_POSTBOSS = _locname(A_CLOUDRUN, "After Fluffy XR-9")
L_CLOUDRUN_FARRIGHT = _locname(A_CLOUDRUN, "Far Right Leap of Faith")

L_COLDKEEP_CANNON = _locname(A_COLDKEEP, "Hidden Under Frozen Cannon")
L_COLDKEEP_BOSS = _locname(A_COLDKEEP, "ColdBlob Boss Drop")
L_COLDKEEP_POSTBOSS = _locname(A_COLDKEEP, "After ColdBlob")
L_COLDKEEP_UPPER = _locname(A_COLDKEEP, "Upper Branch")
L_COLDKEEP_LOWER = _locname(A_COLDKEEP, "Lower Branch")

L_THE_CURTAIN_FLOWER = _locname(A_THE_CURTAIN, "Lower Save (Flower)")
L_THE_CURTAIN_KILL = _locname(A_THE_CURTAIN, "Top Left Edge Drop Kill Floaters")
L_THE_CURTAIN_BREAKABLE = _locname(A_THE_CURTAIN, "Hidden Breakable Floor Near Cannon")
L_THE_CURTAIN_BOSS = _locname(A_THE_CURTAIN, "Ninja 1 Boss Drop")
L_THE_CURTAIN_POSTBOSS = _locname(A_THE_CURTAIN, "After Ninja 1")

L_DARK_GROTTO_UPPER = _locname(A_DARK_GROTTO, "Upper Save Yellow Energy Climb")
L_DARK_GROTTO_CAMPSITE = _locname(A_DARK_GROTTO, "Hidden Above Campsite")
L_DARK_GROTTO_BOSS = _locname(A_DARK_GROTTO, "DarkGrottoRed Boss Drop")
L_DARK_GROTTO_POSTBOSS = _locname(A_DARK_GROTTO, "After DarkGrottoRed")
L_DARK_GROTTO_TORCHES = _locname(A_DARK_GROTTO, "Boss Room Torch Puzzle")
L_DARK_GROTTO_FLOWER = _locname(A_DARK_GROTTO, "Exit Save (Flower)")

L_DEEPDIVE_LEFT = _locname(A_DEEPDIVE, "Left Shipwreck")
L_DEEPDIVE_CHEST = _locname(A_DEEPDIVE, "Left Shipwreck Chest")
L_DEEPDIVE_LEFTCEILING = _locname(A_DEEPDIVE, "Left Shipwreck Hidden Ceiling")
L_DEEPDIVE_TOP = _locname(A_DEEPDIVE, "Main Shaft Top")
L_DEEPDIVE_LEFTFISHNOOK = _locname(A_DEEPDIVE, "Main Shaft Hidden Frozen Fish Nook")
L_DEEPDIVE_1FISHROOM = _locname(A_DEEPDIVE, "Main Shaft Upper Frozen Fish Room")
L_DEEPDIVE_MIDDLEROOM = _locname(A_DEEPDIVE, "Main Shaft Middle Fish Room")
L_DEEPDIVE_BOTTOM = _locname(A_DEEPDIVE, "Main Shaft Bottom Spike Pit Room")
L_DEEPDIVE_CARGO = _locname(A_DEEPDIVE, "SS Eternity Cargo")
L_DEEPDIVE_BOSS = _locname(A_DEEPDIVE, "DeepDragon Boss Drop")
L_DEEPDIVE_INBLOCK = _locname(A_DEEPDIVE, "Exit Shaft Hidden Inside Block")
L_DEEPDIVE_RIGHTFISHNOOK = _locname(A_DEEPDIVE, "Exit Shaft Hidden Frozen Fish Nook")
L_DEEPDIVE_FLOWER = _locname(A_DEEPDIVE, "After DeepDragon Left (Flower)")
L_DEEPDIVE_POSTBOSS = _locname(A_DEEPDIVE, "After DeepDragon Right")
L_DEEPDIVE_SPIKEPATH = _locname(A_DEEPDIVE, "Exit Shaft Spike Path Room")

L_DEEPTOWER_DOOR = _locname(A_DEEPTOWER, "NightWalk Upper Gauntlet Heart Door")
L_DEEPTOWER_BOSS = _locname(A_DEEPTOWER, "DeepCannon Boss Drop")
L_DEEPTOWER_POSTBOSS = _locname(A_DEEPTOWER, "After DeepCannon")
L_DEEPTOWER_SPIKES = _locname(A_DEEPTOWER, "Across Spike Pit")

L_FARFALL_KILL = _locname(A_FARFALL, "Upper Left Kill Floaters")
L_FARFALL_CHEST = _locname(A_FARFALL, "First Landing Far Left Chest")
L_FARFALL_5BALLOONS = _locname(A_FARFALL, "Left Path Clockwise Balloons")
L_FARFALL_SPECIALBALLOON = _locname(A_FARFALL, "Lower Left Path Special Balloon")
L_FARFALL_PITDOOR = _locname(A_FARFALL, "Pit Gauntlet Bottom Heart Door")
L_FARFALL_PITEND = _locname(A_FARFALL, "Pit Gauntlet Save Left")
L_FARFALL_FLOWER = _locname(A_FARFALL, "Pit Gauntlet Save Right (Flower)")
L_FARFALL_YELLOWDOOR = _locname(A_FARFALL, "Pit Gauntlet Yellow Energy Heart Door")
L_FARFALL_BOSS = _locname(A_FARFALL, "FarSplitter Boss Drop")
L_FARFALL_POSTBOSS = _locname(A_FARFALL, "After FarSplitter")

L_FIRECAGE_TOLL = _locname(A_FIRECAGE, "Top Left Tollgate")
L_FIRECAGE_LEFTSAVE = _locname(A_FIRECAGE, "Bottom Left Hidden Nook")
L_FIRECAGE_CRUSHERS = _locname(A_FIRECAGE, "Double Crushers After Upper Gauntlet")
L_FIRECAGE_UPPERDOOR = _locname(A_FIRECAGE, "Upper Gauntlet Heart Door")
L_FIRECAGE_MIDDLE = _locname(A_FIRECAGE, "High Ledge After Lower Gauntlet")
L_FIRECAGE_LOWERDOOR = _locname(A_FIRECAGE, "Lower Gauntlet Heart Door")
L_FIRECAGE_RIGHTSAVE = _locname(A_FIRECAGE, "Right Save Ceiling Slide Nook")
L_FIRECAGE_POSTBOSS = _locname(A_FIRECAGE, "After FireMachine")
L_FIRECAGE_BOSS = _locname(A_FIRECAGE, "FireMachine Boss Drop")

L_GROTTO_POSTBOSS = _locname(A_GROTTO, "After GrottoRed")
L_GROTTO_BOSS = _locname(A_GROTTO, "GrottoRed Boss Drop")
L_GROTTO_FLOWER = _locname(A_GROTTO, "Entrance Save (Flower)")
L_GROTTO_MURAL = _locname(A_GROTTO, "Above Murals")
L_GROTTO_POSTBOSS2 = _locname(A_GROTTO, "After GrottoEye")
L_GROTTO_BOSS2 = _locname(A_GROTTO, "GrottoEye Boss Drop")

L_HIGHLANDS_PLATFORM = _locname(A_HIGHLANDS, "Cliff Jump Platform Below Curtain")  # "Jumped off the cliff in HighLands."

L_ICECASTLE_LEFTOUTER = _locname(A_ICECASTLE, "Left Outer Wall")
L_ICECASTLE_SPIKEFUNNEL = _locname(A_ICECASTLE, "Entrance Gauntlet Nook Above Spike Funnel")
L_ICECASTLE_ENTRYDOOR = _locname(A_ICECASTLE, "Entrance Gauntlet Heart Door")
L_ICECASTLE_FLOWER = _locname(A_ICECASTLE, "Bottom Left Save (Flower)")
L_ICECASTLE_YELLOWDOOR = _locname(A_ICECASTLE, "Upper Yellow Energy Heart Door")
L_ICECASTLE_UNDERSIDE = _locname(A_ICECASTLE, "Exit Underside Path")
L_ICECASTLE_TINYDOOR = _locname(A_ICECASTLE, "Central Tiny Platforms Heart Door")
L_ICECASTLE_CANNONDOOR = _locname(A_ICECASTLE, "Lower Snowball Cannon Heart Door")
L_ICECASTLE_SPIKEFLOOR = _locname(A_ICECASTLE, "Lower Hidden Path in Spike Floor")
L_ICECASTLE_POSTBOSS = _locname(A_ICECASTLE, "After IceBall")
L_ICECASTLE_BOSS = _locname(A_ICECASTLE, "IceBall Boss Drop")
L_ICECASTLE_TOPRIGHT = _locname(A_ICECASTLE, "Top Right Really Secret Path")

L_LIBRARY_UPPER = _locname(A_LIBRARY, "Upper Shelves")
L_LIBRARY_FLOWER = _locname(A_LIBRARY, "Lower Shelves (Flower)")

L_LONGBEACH_FLOWER = _locname(A_LONGBEACH, "Below Entrance Save (Flower)")

L_MOUNTSIDE_FLOWER = _locname(A_MOUNTSIDE, "Entrance Save (Flower)")
L_MOUNTSIDE_DOOR = _locname(A_MOUNTSIDE, "Gauntlet Heart Door")

L_NIGHTCLIMB_BOSS = _locname(A_NIGHTCLIMB, "NightSpirit Boss Drop")
L_NIGHTCLIMB_CANNONS = _locname(A_NIGHTCLIMB, "Hidden Nook Behind Cannons")
L_NIGHTCLIMB_TOP = _locname(A_NIGHTCLIMB, "Above Upper Save")
L_NIGHTCLIMB_DUCK = _locname(A_NIGHTCLIMB, "Topmost Duck Statues")
L_NIGHTCLIMB_UPPERSAVE = _locname(A_NIGHTCLIMB, "Upper Save")
L_NIGHTCLIMB_FLOWER = _locname(A_NIGHTCLIMB, "Below Upper Save (Flower)")
L_NIGHTCLIMB_RIGHT = _locname(A_NIGHTCLIMB, "Right Grass Platform")
L_NIGHTCLIMB_CHEST = _locname(A_NIGHTCLIMB, "Bottom Right Snowy Branch Chest")

L_NIGHTWALK_UPPEREND = _locname(A_NIGHTWALK, "End of Upper Gauntlet")
L_NIGHTWALK_NESTFLOWER = _locname(A_NIGHTWALK, "Starting Nest (Flower)")
L_NIGHTWALK_LOWERFLOWER = _locname(A_NIGHTWALK, "Lower Save (Flower)")
L_NIGHTWALK_SKYRED = _locname(A_NIGHTWALK, "Cloud Climb Near Bird Temple")
L_NIGHTWALK_FIRST = _locname(A_NIGHTWALK, "First Item")
L_NIGHTWALK_BREAKABLE = _locname(A_NIGHTWALK, "Breakable Grass Block Near First Item")
L_NIGHTWALK_CHEST = _locname(A_NIGHTWALK, "Upper Gauntlet Middle Chest")
L_NIGHTWALK_SKYTEMPLE = _locname(A_NIGHTWALK, "Above Bird Temple")
L_NIGHTWALK_GROUNDTEMPLE = _locname(A_NIGHTWALK, "Bird Temple")
L_NIGHTWALK_TORCHES = _locname(A_NIGHTWALK, "Bird Temple Torch Puzzle")
L_NIGHTWALK_UPPERFLOWER = _locname(A_NIGHTWALK, "Upper Save (Flower)")

L_RAINBOWDIVE_4TH = _locname(A_RAINBOWDIVE, "Fourth Prize")
L_RAINBOWDIVE_3RD = _locname(A_RAINBOWDIVE, "Third Prize")
L_RAINBOWDIVE_2ND = _locname(A_RAINBOWDIVE, "Second Prize")
L_RAINBOWDIVE_1ST = _locname(A_RAINBOWDIVE, "First Prize")

L_SKYLANDS_CHEST = _locname(A_SKYLANDS, "Left Chest")
L_SKYLANDS_TOLL = _locname(A_SKYLANDS, "Bottom Left Tollgate")
L_SKYLANDS_DUCK = _locname(A_SKYLANDS, "Middle Duck Statues")
L_SKYLANDS_BALLOONS = _locname(A_SKYLANDS, "Bottom Balloon Sequence")
L_SKYLANDS_PORTAL = _locname(A_SKYLANDS, "Portal from NightWalk")
L_SKYLANDS_DOOR = _locname(A_SKYLANDS, "Bottom Right Heart Door")
L_SKYLANDS_TOPRIGHT = _locname(A_SKYLANDS, "Top Right Underhang")

L_SKYSAND_LEFTSTATUE = _locname(A_SKYSAND, "Hidden Nook Under Left Roof Statue")
L_SKYSAND_FLOWER = _locname(A_SKYSAND, "Bottom Left Outer Cactus (Flower)")
L_SKYSAND_BOTTOMSAVE = _locname(A_SKYSAND, "Bottom Save")
L_SKYSAND_POSTBOSS = _locname(A_SKYSAND, "After SkyMummy")
L_SKYSAND_BOSS = _locname(A_SKYSAND, "SkyMummy Boss Drop")
L_SKYSAND_UPPERDOOR = _locname(A_SKYSAND, "Upper Gauntlet Heart Door")
L_SKYSAND_YELLOW = _locname(A_SKYSAND, "Upper Gauntlet Yellow Energy Nook")
L_SKYSAND_LOWERDOOR = _locname(A_SKYSAND, "Lower Gauntlet Heart Door")
L_SKYSAND_CHEST = _locname(A_SKYSAND, "Right Roof Chest")

L_SKY_TOWN_YELLOW = _locname(A_SKY_TOWN, "Left Yellow Energy Underhang")
L_SKY_TOWN_RED = _locname(A_SKY_TOWN, "Left Red Energy Tower")
L_SKY_TOWN_SHOP1 = _locname(A_SKY_TOWN, "Shop Item 1")
L_SKY_TOWN_SHOP2 = _locname(A_SKY_TOWN, "Shop Item 2")
L_SKY_TOWN_SHOP3 = _locname(A_SKY_TOWN, "Shop Item 3")
L_SKY_TOWN_SHOP4 = _locname(A_SKY_TOWN, "Shop Item 4")
L_SKY_TOWN_SHOP5 = _locname(A_SKY_TOWN, "Shop Item 5")
L_SKY_TOWN_SHOP6 = _locname(A_SKY_TOWN, "Shop Item 6")
L_SKY_TOWN_SHOP7 = _locname(A_SKY_TOWN, "Shop Item 7")
L_SKY_TOWN_SHOP8 = _locname(A_SKY_TOWN, "Shop Item 8")
L_SKY_TOWN_TOWER = _locname(A_SKY_TOWN, "Entrance Lookout Tower")
L_SKY_TOWN_FLOWER = _locname(A_SKY_TOWN, "Entrance Save (Flower)")
L_SKY_TOWN_PITLEFT = _locname(A_SKY_TOWN, "Pit Left Room")
L_SKY_TOWN_PITBOTTOM = _locname(A_SKY_TOWN, "Pit Bottom")
L_SKY_TOWN_PITRIGHT = _locname(A_SKY_TOWN, "Pit Right Room")

L_STAIRCASE_5FLOWERS = _locname(A_STAIRCASE, "5 Flowers Reward")
L_STAIRCASE_10FLOWERS = _locname(A_STAIRCASE, "10 Flowers Reward")
L_STAIRCASE_15FLOWERS = _locname(A_STAIRCASE, "15 Flowers Reward")
L_STAIRCASE_20FLOWERS = _locname(A_STAIRCASE, "20 Flowers Reward")

L_STONECASTLE_FLOWER = _locname(A_STONECASTLE, "Entrance Save (Flower)")
L_STONECASTLE_UPPER = _locname(A_STONECASTLE, "Upper Path Fire Shooters")
L_STONECASTLE_DOOR = _locname(A_STONECASTLE, "Stone Walkers Heart Door")
L_STONECASTLE_HIDDEN = _locname(A_STONECASTLE, "Stone Walkers Hidden Nook")
L_STONECASTLE_BOSS = _locname(A_STONECASTLE, "StoneHead Boss Drop")
L_STONECASTLE_BOSS2 = _locname(A_STONECASTLE, "StoneEye Boss Drop")
L_STONECASTLE_POSTBOSS = _locname(A_STONECASTLE, "After StoneHead")
L_STONECASTLE_POSTBOSS2 = _locname(A_STONECASTLE, "After StoneEye")

L_STRANGECASTLE_END = _locname(A_STRANGECASTLE, "End of Gauntlet")
L_STRANGECASTLE_DOOR = _locname(A_STRANGECASTLE, "Gauntlet Heart Door")

L_UNDERTOMB_LEFT = _locname(A_UNDERTOMB, "End of Left Gauntlet")
L_UNDERTOMB_LEFTDOOR = _locname(A_UNDERTOMB, "Left Gauntlet Heart Door")
L_UNDERTOMB_RIGHTDOOR = _locname(A_UNDERTOMB, "Right Gauntlet Heart Door")

# Entrances ("connections")

def _entname(area, description="", append_entrance=True):
    return f"{area}{f' {description}' if description else ''}{f' Entrance' if append_entrance else ''}"

C_NIGHTCLIMB = _entname(A_NIGHTCLIMB)
C_DEEPDIVE = _entname(A_DEEPDIVE)
C_MOUNTSIDE = _entname(A_MOUNTSIDE)
C_SKYSAND = _entname(A_SKYSAND)
C_FARFALL = _entname(A_FARFALL)
C_FIRECAGE = _entname(A_FIRECAGE)
C_BLANCLAND = _entname(A_BLANCLAND)
C_DEEPDIVE_RIGHT = _entname(R_DEEPDIVE_RIGHT)
C_THE_CURTAIN = _entname(A_THE_CURTAIN)
C_DARK_GROTTO = _entname(A_DARK_GROTTO)
C_STRANGECASTLE = _entname(A_STRANGECASTLE)
C_THE_BOTTOM = _entname(A_THE_BOTTOM)
C_LONGBEACH_UPPER = _entname(A_LONGBEACH, "Upper")
C_LONGBEACH_MIDDLE = _entname(A_LONGBEACH, "Middle")
C_LONGBEACH_LOWER = _entname(A_LONGBEACH, "Lower")
C_BLACKCASTLE = _entname(A_BLACKCASTLE)

# Victory

VICTORY = "Victory"
