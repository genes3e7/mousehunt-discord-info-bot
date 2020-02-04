import discord


STATUS = discord.Status.online
GAMENAME = "MouseHunt"

DIVIDER = "=" * 50

# Trigger for command check
TRIGGER = "...."
HELP = "help"
HELPSYMBOL = "?"

# Everything to do with valor rift
PRESTIGESTATS = "prestigestats"
VRIFTFRAGCORE = "vriftfragcore"
ABOUTPRESTIGE = "aboutprestigebase"
VRIFTFLOORCACHE = "vriftfloorcache"
VRIFTAUGMENTATION = "vriftaugment"

# Everything to do with furoma rift
FRIFTBATTERYTABLE = "friftbatterytable"

COMMANDLIST = [
    # Triggers help box
    HELP, HELPSYMBOL,
    # Prestige base functions
    PRESTIGESTATS, ABOUTPRESTIGE,
    # Other valor rift functions
    VRIFTFRAGCORE, VRIFTFLOORCACHE, VRIFTAUGMENTATION,
    # Furoma rift functions
    FRIFTBATTERYTABLE
]

# Instant triggers to stop irritating things
DONOTIRRITATE = [
    
]

# Fun/troll triggers
REPEAT = [
    
]

KIV = "Feature under construction\nTry again later"
NOREPLY = "noreply"
ERROR = "error"
