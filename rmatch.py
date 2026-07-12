import sys

crewmate = "#85f2f5"
impostor = "#f7191b"
neutral = "#cc913b"
coven = "#8a5fc2"

crewmate_roles = [
    "adrenaline", "altruist", "astral", "bane", "carrier", "catcher", "convener",
    "copycat", "crusader", "decryptor", "detour", "dictator", "donut delivery", "double agent",
    "forensic", "fortune teller", "goose", "helper", "imitator", "inquirer", "inquisitor",
    "insight", "inspector", "investigator", "journalist", "judge", "lazy guy", "markseeker",
    "marshall", "mathematician", "mayor", "mechanic", "medic", "merchant",
    "monarch", "negotiator", "perceiver", "portal maker", "president",
    "ricochet", "sentinel", "sheriff", "snitch", "speedrunner", "spy",
    "super star", "survivor", "swapper", "time master", "tornado", "veteran",
    "vigilante",
]

impostor_roles = [
    "abyssbringer", "arrogance", "assumer", "augmenter", "blackmailer",
    "bomber", "bounty hunter", "butcher", "centralizer", "changeling",
    "cleaner", "consigliere", "councillor", "devourer", "disperser",
    "duellist", "echo", "escapist", "exclusionary", "exorcist",
    "fabricator", "gambler", "gangster", "godfather", "greedy", "hitman",
    "kamikaze", "kidnapper", "killing machine", "librarian", "lightning",
    "loner", "lurker", "mercenary", "ninja", "ocultist", "penguin", "perplexer",
    "postponer", "rift maker", "sapper", "scavenger", "silencer", "sniper",
    "stealth", "swooper", "trickster", "twister", "vampire", "venerer",
    "ventriloquist", "vindicator", "visionary", "wasp", "wiper", "witch",
    "yin yanger", "zombie",
]

neutral_roles = [
    "accumulator", "agitator", "amogus", "arsonist", "auditor",
    "backstabber", "bandit", "berserker", "blockade", "blood knight",
    "bubble", "clerk", "cultist", "curser", "collector", "dealer",
    "demon", "doomsayer", "doppelganger", "duality", "eclipse", "enderman",
    "executioner", "follower", "gaslighter", "god", "hater",
    "head hunter", "hex master", "impartial", "infection", "innocent",
    "investor", "jackal", "jackpot", "jester", "jinx",
    "juggernaut", "lawyer", "magician", "magistrate", "maverick",
    "medusa", "necro-guesser", "necromancer", "nonplus", "note killer", "opportunist",
    "pawn", "pelican", "pickpocket", "plaguebearer", "poisoner",
    "provocateur", "quarry", "quiz master", "ritualist", "rogue",
    "romantic", "room rusher", "samurai", "schrödinger's cat", "serial killer",
    "simon", "soul collector", "soul hunter", "specter", "stalker",
    "terrorist", "thanos", "the glitch", "thief", "tiger",
    "tremor", "vector", "vengeance", "virus", "vortex",
    "weapon master", "weatherman", "werewolf", "wraith",
]

coven_roles = [
    "banshee", "dreamweaver", "empress", "enchanter", "goddess",
    "illusionist", "moon dancer", "poache", "potion master",
    "reaper", "shadow", "spellcaster", "summoner", "coven leader",
]

addons = [
    "anti-tp", "antidote", "autopsy", "bait", "banana man", "bewilder",
    "blessed", "circumvent", "commited", "concealer", "constricted",
    "disco", "double shot", "dynamo", "energetic", "finder", "flash",
    "fragile", "gravestone", "haste", "hidden", "last impostor", "lazy",
    "listener", "looter", "loyal", "lucky", "magnet", "messenger", "mimic",
    "mischievous", "necroview", "nimble", "noisy", "oblivious", "onbound",
    "physicist", "reach", "reroll", "schizophrenic", "seer", "sleuth",
    "spurt", "stained", "stealer", "sunglasses", "swift", "tiebreaker",
    "torch", "unbound", "underdog", "venom", "watcher", "workhorse",
]

ghost_roles = [
    "bloodmoon", "facilitator", "haunter", "meeting angel",
    "minion", "phantasm", "shade", "warden",
]

def hex_to_ansi(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f"\033[38;2;{r};{g};{b}m"

def cprint(text, color="#ffffff"):
    reset = "\033[0m"
    print(f"{hex_to_ansi(color)}{text}{reset}")

# Find whether or not the input is a real role
def find_role(role):
    role_lower = role.lower()

    factions = [
        ("crewmate", crewmate_roles, crewmate),
        ("impostor", impostor_roles, impostor),
        ("neutral", neutral_roles, neutral),
        ("coven", coven_roles, coven),
    ]

    for faction, roles, color in factions:
        if role_lower in roles:
            article = "an" if faction == "impostor" else "a"
            cprint(
                f"{role.title()} is {article} {faction.title()} role",
                color
            )
            return

    if role_lower in addons:
        cprint(f"{role.title()} is an Addon", "#ffffff")
        return

    if role_lower in ghost_roles:
        cprint(f"{role.title()} is a Ghost role", "#ffffff")
        return

    cprint(f'"{role.title()}" does not exist', "#ff0000")

# Match a sequence of scrambled letters with a role name
def match_role(letters):
    letters = letters.lower()

    groups = [
        ("Crewmate", crewmate_roles, crewmate),
        ("Impostor", impostor_roles, impostor),
        ("Neutral", neutral_roles, neutral),
        ("Coven", coven_roles, coven),
    ]

    print("Match result:")

    for faction, roles, color in groups:
        matches = []

        for role in roles:
            role_letters = list(role.replace(" ", "").replace("-", ""))
            temp = role_letters.copy()
            valid = True

            for char in letters:
                if char in temp:
                    temp.remove(char)
                else:
                    valid = False
                    break

            if valid:
                matches.append(role)

        matches.sort(key=lambda x: (len(x.replace(" ", "").replace("-", "")), x))

        for role in matches:
            cprint(
                f" - {role.title()}: {faction}",
                color
            )

def find_and_match(role):
    find_role(role)
    print("")
    match_role(role)
    print("")

if len(sys.argv) < 2:
    role = input("Match role: ")
else:
    role = " ".join(sys.argv[1:])

if role in ("decryptor", "decrypt"):
    print("\nContinuous mode activated. Have fun decrypting!")
    while True:
        role = input("Match role: ")
        if role in ("stop", "terminate"): break
        find_and_match(role)

find_and_match(role)
