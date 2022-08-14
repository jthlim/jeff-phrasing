# Jeff's phrasing dictionary for Plover.

# See README.md for instructions on how the system works.

import re

LONGEST_KEY = 1

PARTS_MATCHER = re.compile(
    r'(S?T?K?P?W?H?R?)(A?O?)-?(\*?)(E?U?)(F?)(R?P?B?L?G?T?S?D?Z?)'
)

STARTERS = {
    # Map of stroke -> word, verb-form.
    #  * '1p', '2p', '3p' for 1st, 2nd, 3rd person
    #  * 'p/s' for plural/singular
    "SWR": ("I", "1ps"),
    "KPWR": ("you", "2p"),
    "KWHR": ("he", "3ps"),
    "SKWHR": ("she", "3ps"),
    "KPWH": ("it", "3ps"),
    "TWR": ("we", "1pp"),
    "TWH": ("they", "3pp"),
    "STKPWHR": ("", "3ps"),
    "STWR": ("", "3pp"),
}

MIDDLE_EXCEPTIONS = {
    "": ("", False),
    "F": (" never", False),
    "E": (" really", False),
    "U": (" just", False),
    "UF": ("*", True),
    "EU": (" all", False),
    "EUF": (" still", False),
}

MIDDLES_BASE = {
    # Map of stroke -> (map[tense][verb-form](string, verb-form)
    "": {"present": {None: (" do", "inf"), "3ps": (" does", "inf")}, "past": (" did", "inf")},
    "*": {"present": {None: (" don't", "inf"), "3ps": (" doesn't", "inf")}, "past": (" didn't", "inf")},
    "A": {"present": (" can", "inf"), "past": (" could", "inf")},
    "A*": {"present": (" can't", "inf"), "past": (" couldn't", "inf")},
    "O": {"present": (" shall", "inf"), "past": (" should", "inf")},
    "O*": {"present": (" shall not", "inf"), "past": (" shouldn't", "inf")},
    "AO": {"present": (" will", "inf"), "past": (" would", "inf")},
    "AO*": {"present": (" won't", "inf"), "past": (" wouldn't", "inf")},
}

MIDDLES_DECORATORS = {
    "": "*",
    "*": "*",
    "F": "* never",
    "*F": "* even",
    "E": "* really",
    "*E": "* really",
    "EF": " really*",
    "*EF": " really*",
    "U": "* just",
    "*U": "* just",
    "UF": " just*",
    "*UF": " just*",
    "EU": "* all",
    "*EU": "* all",
    "EUF": " still*",
    "*EUF": " still*",
}

ENDERS = {
    "": ("present", ""),
    "D": ("past", ""),

    # B: To be (the)
    "B": ("present", {"inf": " be", "1ps": " am", "2p": " are", "3ps": " is", "1pp": " are", "3pp": " are"}),
    "BT": ("present", {"inf": " be the", "1ps": " am the", "2p": " are the", "3ps": " is the", "1pp": " are the", "3pp": " are the"}),
    "BD": ("past", {"inf": " be", "1ps": " was", "2p": " were", "3ps": " was", "1pp": " were", "3pp": " were"}),
    "BTD": ("past", {"inf": " be the", "1ps": " was the", "2p": " were the", "3ps": " was the", "1pp": " were the", "3pp": " were the"}),

    # BL - To believe
    "BL": ("present", {None: " believe", "3ps": " believes"}),
    "BLT": ("present", {None: " believe that", "3ps": " believes that"}),
    "BLD": ("past", {None: " believed", "inf": " believe"}),
    "BLTD": ("past", {None: " believed that", "inf": " believe that"}),

    # BG - To come (to)
    "BG": ("present", {None: " come", "3ps": " comes"}),
    "BGT": ("present", {None: " come to", "3ps": " comes to"}),
    "BGD": ("past", {None: " came", "inf": " come"}),
    "BGTD": ("past", {None: " came to", "inf": " come to"}),

    # LS - To feel (like)
    "LS": ("present", {None: " feel", "3ps": " feels"}),
    "LTS": ("present", {None: " feel like", "3ps": " feels like"}),
    "LSZ": ("past", {None: " felt", "inf": " feel"}),
    "LTSDZ": ("past", {None: " felt like", "inf": " feel like"}),

    # PBLG - To find (that)
    "PBLG": ("present", {None: " find", "3ps": " finds"}),
    "PBLGT": ("present", {None: " find that", "3ps": " finds that"}),
    "PBLGD": ("past", {None: " found", "inf": " find"}),
    "PBLGTD": ("past", {None: " found that", "inf": " find that"}),

    # RG: To forget (to)
    "RG": ("present", {None: " forget", "3ps": " forgets"}),
    "RGT": ("present", {None: " forget to", "3ps": " forgets to"}),
    "RGD": ("past", {None: " forgot", "inf": " forget"}),
    "RGTD": ("past", {None: " forgot to", "inf": " forget to"}),

    # GS: To get (to)
    "GS": ("present", {None: " get", "3ps": " gets"}),
    "GTS": ("present", {None: " get to", "3ps": " gets to"}),
    "GSZ": ("past", {None: " got", "inf": " get"}),
    "GTSDZ": ("past", {None: " got to", "inf": " get to"}),

    # GZ: To give
    "GZ": ("present", {None: " give", "3ps": " gives"}),
    "GDZ": ("past", {None: " gave", "inf": " give"}),

    # G: To go (to)
    "G": ("present", {None: " go", "3ps": " goes"}),
    "GT": ("present", {None: " go to", "3ps": " goes to"}),
    "GD": ("past", {None: " went", "inf": " go"}),
    "GTD": ("past", {None: " went to", "inf": " go to"}),

    # T - To have (to)
    "T": ("present", {None: " have", "3ps": " has"}),
    "TS": ("present", {None: " have to", "3ps": " has to"}),
    "TD": ("past", {None: " had", "inf": " have"}),
    "TSDZ": ("past", {None: " had to", "inf": " have to"}),

    # PB: To know (that)
    "PB": ("present", {None: " know", "3ps": " knows"}),
    "PBT": ("present", {None: " know that", "3ps": " knows that"}),
    "PBD": ("past", {None: " knew", "inf": " know"}),
    "PBTD": ("past", {None: " knew that", "inf": " know that"}),

    # BLG - To like
    "BLG": ("present", {None: " like", "3ps": " likes"}),
    "BLGT": ("present", {None: " like to", "3ps": " likes to"}),
    "BLGD": ("past", {None: " liked", "inf": " like"}),
    "BLGTD": ("past", {None: " liked to", "inf": " like to"}),

    # LZ - To live
    "LZ": ("present", {None: " live", "3ps": " lives"}),
    "LDZ": ("past", {None: " lived", "inf": " live"}),

    # L - To look
    "L": ("present", {None: " look", "3ps": " looks"}),
    "LD": ("past", {None: " looked", "inf": " look"}),

    # LG - To love
    "LG": ("present", {None: " love", "3ps": " loves"}),
    "LGD": ("past", {None: " loved", "inf": " love"}),

    # LT - To let
    "LT": ("present", {None: " let", "3ps": " lets"}),
    "LTD": ("past", " let"),

    # RPBL - To make (the)
    "RPBL": ("present", {None: " make", "3ps": " makes"}),
    "RPBLT": ("present", {None: " make the", "3ps": " makes the"}),
    "RPBLD": ("past", {None: " made", "inf": " make"}),
    "RPBLTD": ("past", {None: " made the", "inf": " make the"}),

    # PL - To may
    # These do not combine well with do/can/shall/will
    "PL": ("present", " may"),
    "PLT": ("present", " may have"),
    "PLD": ("past", {None: " might", "inf": " may"}),
    "PLTD": ("past", {None: " might have", "inf": " may have"}),

    # PLZ - To move
    "PLZ": ("present", {None: " move", "3ps": " moves"}),
    "PLDZ": ("past", {None: " moved", "inf": " move"}),

    # RPG: To need (to)
    "RPG": ("present", {None: " need", "3ps": " needs"}),
    "RPGT": ("present", {None: " need to", "3ps": " needs to"}),
    "RPGD": ("past", {None: " needed", "inf": " need"}),
    "RPGTD": ("past", {None: " needed to", "inf": " need to"}),

    # RL - To recall
    "RL": ("present", {None: " recall", "3ps": " recalls"}),
    "RLT": ("present", {None: " recall that", "3ps": " recalls that"}),
    "RLD": ("past", {None: " recalled", "inf": " recall"}),
    "RLTD": ("past", {None: " recalled that", "inf": " recall that"}),

    # RLS - To realize (that)
    "RLS": ("present", {None: " realize", "3ps": " realizes"}),
    "RLTS": ("present", {None: " realize that", "3ps": " realizes that"}),
    "RLSZ": ("past", {None: " realized", "inf": " realize"}),
    "RLTSDZ": ("past", {None: " realized that", "inf": " realize that"}),

    # RPL - To remember (that)
    "RPL": ("present", {None: " remember", "3ps": " remembers"}),
    "RPLT": ("present", {None: " remember that", "3ps": " remembers that"}),
    "RPLD": ("past", {None: " remembered", "inf": " realize"}),
    "RPLTD": ("past", {None: " remembered that", "inf": " remember that"}),

    # R - To run
    "R": ("present", {None: " run", "3ps": " runs"}),
    "RD": ("past", {None: " ran", "inf": " run"}),

    # BS - To say
    "BS": ("present", {None: " say", "3ps": " says"}),
    "BSZ": ("past", {None: " said", "inf": " say"}),

    # S - To see
    "S": ("present", {None: " see", "3ps": " sees"}),
    "SZ": ("past", {None: " saw", "inf": " see"}),

    # PLS - To seem (to)
    "PLS": ("present", {None: " seem", "3ps": " seems"}),
    "PLTS": ("present", {None: " seem to", "3ps": " seems to"}),
    "PLSZ": ("past", {None: " seemed", "inf": " seem"}),
    "PLTSDZ": ("past", {None: " seemed to", "inf": " seem to"}),

    # RT - To take
    "RBT": ("present", {None: " take", "3ps": " takes"}),
    "RBTD": ("past", {None: " took", "inf": " take"}),

    # PBG - To think (that)
    "PBG": ("present", {None: " think", "3ps": " thinks"}),
    "PBGT": ("present", {None: " think that", "3ps": " thinks that"}),
    "PBGD": ("past", {None: " thought", "inf": " think"}),
    "PBGTD": ("past", {None: " thought that", "inf": " think that"}),

    # RT - To try (to)
    "RT": ("present", {None: " try", "3ps": " tries"}),
    "RTS": ("present", {None: " try to", "3ps": " tries to"}),
    "RTD": ("past", {None: " tried", "inf": " try"}),
    "RTSDZ": ("past", {None: " tried to", "inf": " try to"}),

    # PBG - To understand (the)
    "RPB": ("present", {None: " understand", "3ps": " understands"}),
    "RPBT": ("present", {None: " understand the", "3ps": " understands the"}),
    "RPBD": ("past", {None: " understood", "inf": " understand"}),
    "RPBTD": ("past", {None: " understood the", "inf": " understand the"}),

    # Z - To use
    "Z": ("present", {None: " use", "3ps": " uses"}),
    "DZ": ("past", {None: " used", "inf": " use"}),

    # P: To want (to)
    "P": ("present", {None: " want", "3ps": " wants"}),
    "PT": ("present", {None: " want to", "3ps": " wants to"}),
    "PD": ("past", {None: " wanted", "inf": " want"}),
    "PTD": ("past", {None: " wanted to", "inf": " want to"}),

    # RBG - To work
    "RBG": ("present", {None: " work", "3ps": " works"}),
    "RBGD": ("past", {None: " worked", "inf": " work"}),
}


def lookup(key):
    match = PARTS_MATCHER.match(key[0])
    starter, vowels1, star, vowels2, f, ender = match.groups()
    if not match:
        raise KeyError

    starter_lookup = STARTERS.get(starter)
    if not starter_lookup:
        raise KeyError

    ender_lookup = ENDERS.get(ender)
    if not ender_lookup:
        raise KeyError

    result, verb_form = starter_lookup
    tense, verb = ender_lookup

    middle_key = vowels1 + star + vowels2 + f
    middle_exception = MIDDLE_EXCEPTIONS.get(middle_key)

    base = MIDDLES_BASE[vowels1 + star]
    middle_word, updated_verb_form = lookup_data(
        lookup_data(base, tense), verb_form)

    if middle_exception:
        decorator, allow_verb_update = middle_exception
        if not allow_verb_update:
            updated_verb_form = None
    else:
        decorator = MIDDLES_DECORATORS[star + vowels2 + f]

    middle_word = decorator.replace('*', middle_word)

    result += middle_word

    if updated_verb_form:
        verb_form = updated_verb_form

    ending = lookup_data(verb, verb_form)
    if ending == None:
        raise KeyError

    result += ending

    return result


def lookup_data(data, key):
    if type(data) is not dict:
        return data

    result = data.get(key)
    if result:
        return result

    return data.get(None)

# Proper reverse lookup support.
#
# This will show in Plover's suggestions window.


REVERSE_STARTERS = {}
REVERSE_MIDDLES_BASE = {}
REVERSE_ADVERBS = {}
REVERSE_ENDERS = {}

for key in STARTERS:
    word = STARTERS[key][0]
    REVERSE_STARTERS.setdefault(word, {})
    REVERSE_STARTERS[word][key] = True

POSSIBLE_REVERSE_MATCH = re.compile(r"[a-zI ']+")


def add_reverse_middles_base(stroke, data):
    if type(data) is dict:
        for k in data:
            add_reverse_middles_base(stroke, data[k])
        return

    word = data[0].replace('*', '').strip()
    REVERSE_MIDDLES_BASE.setdefault(word, {})
    REVERSE_MIDDLES_BASE[word][stroke] = True


def add_reverse_enders(stroke, data):
    if type(data) is dict:
        for k in data:
            add_reverse_enders(stroke, data[k])
        return

    word = data.strip()
    REVERSE_ENDERS.setdefault(word, {})
    REVERSE_ENDERS[word][stroke] = True


for key in MIDDLES_BASE:
    add_reverse_middles_base(key, MIDDLES_BASE[key])

for key in MIDDLES_DECORATORS:
    word = MIDDLES_DECORATORS[key].replace('*', '').strip()
    REVERSE_ADVERBS.setdefault(word, {})
    REVERSE_ADVERBS[word][key] = True

for key in MIDDLE_EXCEPTIONS:
    word = MIDDLE_EXCEPTIONS[key][0].replace('*', '').strip()
    REVERSE_ADVERBS.setdefault(word, {})
    REVERSE_ADVERBS[word][key] = True

for key in ENDERS:
    add_reverse_enders(key, ENDERS[key][1])


def reverse_match(result, full_text, prefix):
    if lookup([prefix]).strip() == full_text:
        result.append((prefix,))


def reverse_verb_match(result, full_text, text, prefix):
    if text not in REVERSE_ENDERS:
        return

    prefix = prefix.replace('**', '*')
    for stroke in REVERSE_ENDERS[text]:
        reverse_match(result, full_text, prefix + stroke)


def reverse_decorator_match(result, full_text, text, prefix):
    word = text.split(' ', 1)[0]

    if word in REVERSE_ADVERBS:
        for stroke in REVERSE_ADVERBS[word]:
            reverse_verb_match(result, full_text, text.replace(
                word, '').strip(), prefix + stroke)

    for stroke in REVERSE_ADVERBS['']:
        reverse_verb_match(result, full_text, text, prefix + stroke)


def reverse_middle_base_match(result, full_text, text, prefix):
    for word in REVERSE_MIDDLES_BASE:
        if word in text:
            for stroke in REVERSE_MIDDLES_BASE[word]:
                reverse_decorator_match(result, full_text, text.replace(
                    word, '').strip(), prefix + stroke)

    reverse_decorator_match(result, full_text, text, prefix)


def reverse_lookup(text):
    if not POSSIBLE_REVERSE_MATCH.fullmatch(text):
        return []

    if len(text.split(' ')) > 6:
        return []

    result = []

    words = text.split(' ', 1)
    if words[0] in REVERSE_STARTERS:
        remainder = words[1] if len(words) > 1 else ''
        for stroke in REVERSE_STARTERS[words[0]]:
            reverse_middle_base_match(result, text, remainder, stroke)
    else:
        for stroke in REVERSE_STARTERS['']:
            reverse_middle_base_match(result, text, text, stroke)

    return result
