# Jeff's phrasing dictionary for Plover.

# Starters:
# 
# SWR: "I"
# KPWR: "you"
# KWHR: "he"
# SKWHR: "she"
# KPWH: "it"
# STKPWHR: "" (empty, 3rd person singular)
# TWR: "we"
# TWH: "they"
# SKWR: "" (empty, 3rd person plural)

# Choices inspired by:
# * https://books.google.com/ngrams/graph?content=shouldn%27t%2Chaven%27t%2Cwouldn%27t%2Ccouldn%27t%2Ccan%27t%2Cwon%27t%2Cdon%27t&year_start=1800&year_end=2019&corpus=26&smoothing=3&direct_url=t1%3B%2Cshould%20not%3B%2Cc0%3B.t1%3B%2Chave%20not%3B%2Cc0%3B.t1%3B%2Cwould%20not%3B%2Cc0%3B.t1%3B%2Ccould%20not%3B%2Cc0%3B.t1%3B%2Ccan%20not%3B%2Cc0%3B.t1%3B%2Cwill%20not%3B%2Cc0%3B.t1%3B%2Cdo%20not%3B%2Cc0#t1%3B%2Cshould%20not%3B%2Cc0%3B.t1%3B%2Chave%20not%3B%2Cc0%3B.t1%3B%2Cwould%20not%3B%2Cc0%3B.t1%3B%2Ccould%20not%3B%2Cc0%3B.t1%3B%2Ccan%20not%3B%2Cc0%3B.t1%3B%2Cwill%20not%3B%2Cc0%3B.t1%3B%2Cdo%20not%3B%2Cc0
# * https://books.google.com/ngrams/graph?content=should%2Chave%2Cwould%2Ccould%2Ccan%2Cwill%2Cdo&year_start=1800&year_end=2019&corpus=26&smoothing=3&direct_url=t1%3B%2Cshould%3B%2Cc0%3B.t1%3B%2Chave%3B%2Cc0%3B.t1%3B%2Cwould%3B%2Cc0%3B.t1%3B%2Ccould%3B%2Cc0%3B.t1%3B%2Ccan%3B%2Cc0%3B.t1%3B%2Cwill%3B%2Cc0%3B.t1%3B%2Cdo%3B%2Cc0#t1%3B%2Cshould%3B%2Cc0%3B.t1%3B%2Chave%3B%2Cc0%3B.t1%3B%2Cwould%3B%2Cc0%3B.t1%3B%2Ccould%3B%2Cc0%3B.t1%3B%2Ccan%3B%2Cc0%3B.t1%3B%2Cwill%3B%2Cc0%3B.t1%3B%2Cdo%3B%2Cc0
# * https://books.google.com/ngrams/graph?content=just%2Ceven%2Creally&year_start=1800&year_end=2019&corpus=26&smoothing=3&direct_url=t1%3B%2Cjust%3B%2Cc0%3B.t1%3B%2Ceven%3B%2Cc0%3B.t1%3B%2Creally%3B%2Cc0#t1%3B%2Cjust%3B%2Cc0%3B.t1%3B%2Ceven%3B%2Cc0%3B.t1%3B%2Creally%3B%2Cc0
# 
# EUF
# ---
# 000 — <empty>
# 001 — x even (except for 'do', which just becomes 'do')
# 010 - just x
# 011 - x just
# 100 - really x
# 101 - x really
# 110 - still x
# 111 - x still
#
# AO*
# 000 - do/did
# 001 - don’t/didn’t 
# 010 - shall/should
# 011 - shan’t/shouldn’t 
# 100 - can/could
# 101 - can’t/couldn’t 
# 110 - will/would
# 111 - won’t/wouldn't
#
# Exception: “do” is AOEUF - 00001

import re
from plover import log

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
    "STWR": ("", "3ps"),
    "STKPWHR": ("", "3pp"),
}

MIDDLE_EXCEPTIONS = {
    "": ("", None),
    "F": (" even", None),
    "E": (" really", None),
    "U": (" just", None),
    "EU": (" still", None),
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
    "F": "* even",
    "E": "* really",
    "EF": " really*",
    "U": "* just",
    "UF": " just*",
    "EU": "* still",
    "EUF": " still*",
}

ENDERS = {
    "": ("present", ""),
    "D": ("past", ""),

    # B: To be
    "B": ("present", { "inf": " be", "1ps": " am", "2p": " are", "3ps": " is", "1pp": " are", "3pp": " are" }),
    "BD": ("past", { "inf": " be","1ps": " was", "2p": " were", "3ps": " was", "1pp": " were", "3pp": " were" }),

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

    # GT: To get
    "GT": ("present", {None: " get", "3ps": " gets"}),
    "GTD": ("past", {None: " got", "inf": " get"}),

    # GZ: To give
    "GZ": ("present", {None: " give", "3ps": " gives"}),
    "GDZ": ("past", {None: " gave", "inf": " give"}),

    # G: To go
    "G": ("present", {None: " go", "3ps": " goes"}),
    "GD": ("past", {None: " went", "inf": " go"}),

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
    "BLGD": ("past", {None: " liked", "inf": " like"}),

    # L - To look
    "L": ("present", {None: " look", "3ps": " looks"}),
    "LD": ("past", {None: " looked", "inf": " look"}),

    # LG - To love
    "LG": ("present", {None: " love", "3ps": " loves"}),
    "LGD": ("past", {None: " loved", "inf": " love"}),

    # LT - To let
    "LT": ("present", {None: " let", "3ps": " lets"}),
    "LTD": ("past", " let"),

    # RPBL - To make
    "RPBL": ("present", {None: " make", "3ps": " makes"}),
    "RPBLD": ("past", {None: " made", "inf": " make"}),

    # RPG: To need (to)
    "RPG": ("present", {None: " need", "3ps": " needs"}),
    "RPGT": ("present", {None: " need to", "3ps": " needs to"}),
    "RPGD": ("past", {None: " needed", "inf": " need"}),
    "RPGTD": ("past", {None: " needed to", "inf": " need to"}),

    # RL - To recall
    "RL": ("present", {None: " recall", "3ps": " recalls"}),
    "RLD": ("past", {None: " recalled", "inf": " recall"}),

    # RLS - To realize (that)
    "RLS": ("present", {None: " realize", "3ps": " realizes"}),
    "RLTS": ("present", {None: " realize that", "3ps": " realizes that"}),
    "RLSZ": ("past", {None: " realized", "inf": " realize"}),
    "RLTSDZ": ("past", {None: " realized that", "inf": " realize that"}),

    # RLT - To relate
    "RLT": ("present", {None: " relate", "3ps": " relates"}),
    "RLTD": ("past", {None: " related", "inf": " relate"}),

    # RPL - To remember (that)
    "RPL": ("present", {None: " remember", "3ps": " remembers"}),
    "RPLT": ("present", {None: " remember that", "3ps": " remembers that"}),
    "RPLD": ("past", {None: " remembered", "inf": " realize"}),
    "RPLTD": ("past", {None: " remembered that", "inf": " remember that"}),

    # R - To run
    "R": ("present", {None: " run", "3ps": " runs"}),
    "RD": ("past", {None: " ran", "inf": " run"}),

    # RT - To try
    "RT": ("present", {None: " try", "3ps": " tries"}),
    "RTD": ("past", {None: " tried", "inf": " try"}),

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

    # PBG - To think (that)
    "PBG": ("present", {None: " think", "3ps": " thinks"}),
    "PBGT": ("present", {None: " think that", "3ps": " thinks that"}),
    "PBGD": ("past", {None: " thought", "inf": " think"}),
    "PBGTD": ("past", {None: " thought that", "inf": " think that"}),

    # PBG - To understand (that)
    "RPB": ("present", {None: " understand", "3ps": " understands"}),
    "RPBT": ("present", {None: " understand that", "3ps": " understands that"}),
    "RPBD": ("past", {None: " understood", "inf": " understand"}),
    "RPBTD": ("past", {None: " understood that", "inf": " understand that"}),

    # Z - To use
    "Z": ("present", {None: " use", "3ps": " uses"}),
    "DZ": ("present", {None: " used", "3ps": " use"}),

    # P: To want (to)
    "P": ("present", {None: " want", "3ps": " wants"}),
    "PT": ("present", {None: " want to", "3ps": " wants to"}),
    "PTD": ("present", {None: " wanted to", "inf": " want to"}),
    "PD": ("present", {None: " wanted", "inf": " want"}),

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
    middle_result = MIDDLE_EXCEPTIONS.get(middle_key)
    
    middle_word = None
    updated_verb_form = None

    if middle_result != None:
        middle_word, updated_verb_form = middle_result
    else:
        base = MIDDLES_BASE[vowels1 + star]
        middle_word, updated_verb_form = lookup_data(lookup_data(base, tense), verb_form)
        log.info('middle_word: %s updated_verb_form: %s' % (middle_word, updated_verb_form))
        decorator = MIDDLES_DECORATORS[vowels2 + f]
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
