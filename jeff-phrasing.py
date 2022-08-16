# Jeff's phrasing dictionary for Plover.

# See README.md for instructions on how the system works.

import re

LONGEST_KEY = 1

PARTS_MATCHER = re.compile(
    r'(S?T?K?P?W?H?R?)(A?O?)-?(\*?)(E?U?)(F?)(R?P?B?L?G?T?S?D?Z?)'
)

TO_BE = {
    "present": {
        None: " are",
        "root": " be",
        "1ps": " am",
        "3ps": " is",
        "present-participle": " being",
        "past-participle": " been",
    },
    "past": {
        None: " were",
        "root": " be",
        "1ps": " was",
        "3ps": " was",
        "present-participle": " being",
        "past-participle": " been",
    },
}

TO_HAVE = {
    "present": {
        None: " have",
        "3ps": " has",
        "present-participle": " having",
        "past-participle": " had",
    },
    "past": {
        "root": " have",
        None: " had",
        "3ps": " had",
        "present-participle": " having",
        "past-participle": " had",
    }
}

STARTERS = {
    # Map of stroke -> word, verb-form.
    #  * 'b' for blank
    #  * '1p', '2p', '3p' for 1st, 2nd, 3rd person
    #  * 'p/s' for plural/singular
    "SWR": ("I", "1ps"),
    "KPWR": ("you", "2p"),
    "KWHR": ("he", "3ps"),
    "SKWHR": ("she", "3ps"),
    "KPWH": ("it", "3ps"),
    "TWR": ("we", "1pp"),
    "TWH": ("they", "3pp"),
    "STKPWHR": ("", "b3ps"),
    "STWR": ("", "b3pp"),
}

MIDDLES_BASE = {
    # Map of stroke -> (map[tense][verb-form](string, verb-form)
    "": {"present": {None: (" do", "root"), "3ps": (" does", "root")}, "past": (" did", "root")},
    "*": {"present": {None: (" don't", "root"), "3ps": (" doesn't", "root")}, "past": (" didn't", "root")},
    "A": {"present": (" can", "root"), "past": (" could", "root")},
    "A*": {"present": (" can't", "root"), "past": (" couldn't", "root")},
    "O": {"present": (" shall", "root"), "past": (" should", "root")},
    "O*": {"present": (" shall not", "root"), "past": (" shouldn't", "root")},
    "AO": {"present": (" will", "root"), "past": (" would", "root")},
    "AO*": {"present": (" won't", "root"), "past": (" wouldn't", "root")},
}

MIDDLE_MODIFIER_EXCEPTIONS = {
    "": ("", False, None),

    # To make reverse look-ups work correctly, longer results must be listed first

    "*E": ({"present": {None: " are not", "1ps": "'m not", "2p": "'re not", "3ps": " isn't", "1pp": "'re not", "3pp": "'re not", "b3pp": " are not"}, "past": {None: " weren't", "1ps": " wasn't", "3ps": " wasn't"}}, False, "present-participle"),
    "E": ({"present": {None: " are", "1ps": "'m", "2p": "'re", "3ps": "'s", "b3ps": " is", "1pp": "'re", "3pp": "'re", "b3pp": " are"}, "past": {None: " were", "1ps": " was", "3ps": " was"}}, False, "present-participle"),
    "*F": ({"present": {None: " haven't", "3ps": " hasn't"}, "past": " hadn't"}, False, "past-participle"),
    "F": ({"present": {None: " have", "1ps": "'ve", "2p": "'ve", "3ps": "'s", "b3ps": " has", "1pp": "'ve", "3pp": "'ve", "b3pp": " have"}, "past": {None: " had", "1ps": "'d", "2p": "'d", "3ps": "'d", "1pp": "'d", "3pp": "'d", "b3pp": " had"}}, False, "past-participle"),
    "*EF": ({"present": {None: " haven't been", "3ps": " hasn't been"}, "past": " hadn't been"}, False, "present-participle"),
    "EF": ({"present": {None: " have been", "1ps": "'ve been", "2p": "'ve been", "3ps": "'s been", "b3ps": " has been", "1pp": "'ve been", "3pp": "'ve been", "b3pp": " have been"}, "past": {None: " had been", "1ps": "'d been", "2p": "'d been", "3ps": "'d been", "b3ps": " had been", "1pp": "'d been", "3pp": "'d been", "b3pp": " had been"}}, False, "present-participle"),

    "UF": ("*", True, None),

    "EU": (" still", False, None),
    "EUF": (" never", False, None),

    "STWRU": (" to", False, "root"),
}

MIDDLES_MODIFIERS = {
    "": ("*", True, None),
    "*": ("*", True, None),

    "*E": ({tense: {form: "*" + TO_BE[tense][form] for form in TO_BE[tense]} for tense in TO_BE}, True, "present-participle"),
    "E": ({tense: {form: "*" + TO_BE[tense][form] for form in TO_BE[tense]} for tense in TO_BE}, True, "present-participle"),
    "*EF": ({tense: {form: "*" + TO_HAVE[tense][form] + " been" for form in TO_HAVE[tense]} for tense in TO_HAVE}, True, "present-participle"),
    "EF": ({tense: {form: "*" + TO_HAVE[tense][form] + " been" for form in TO_HAVE[tense]} for tense in TO_HAVE}, True, "present-participle"),
    "*F": ({tense: {form: "*" + TO_HAVE[tense][form] for form in TO_HAVE[tense]} for tense in TO_HAVE}, True, "past-participle"),
    "F": ({tense: {form: "*" + TO_HAVE[tense][form] for form in TO_HAVE[tense]} for tense in TO_HAVE}, True, "past-participle"),

    "*EU": (" still*", True, None),
    "EU": ("* still", True, None),
    "*EUF": ("* even", True, None),
    "EUF": ("* never", True, None),

    "*U": ("* !", True, None),
    "U": ("* !", True, None),
    "*UF": (" just*", True, None),
    "UF": ("* just", True, None),
}

ENDERS = {
    "": ("present", ""),
    "D": ("past", ""),

    # RB: To ask
    "RB": ("present", {None: " ask", "3ps": " asks", "present-participle": " asking", "past-participle": " asked"}),
    "RBD": ("past", {None: " asked", "root": " ask", "present-participle": " asking", "past-participle": " asked"}),

    # B: To be (the)
    "B": ("present", TO_BE["present"]),
    "BT": ("present", {key: TO_BE["present"][key] + " the" for key in TO_BE["present"]}),
    "BD": ("past", TO_BE["past"]),
    "BTD": ("past", {key: TO_BE["past"][key] + " the" for key in TO_BE["past"]}),

    # BL - To believe
    "BL": ("present", {None: " believe", "3ps": " believes", "present-participle": " believing", "past-participle": " believed"}),
    "BLT": ("present", {None: " believe that", "3ps": " believes that", "present-participle": " believing that", "past-participle": " believed that"}),
    "BLD": ("past", {None: " believed", "root": " believe", "present-participle": " believing", "past-participle": " believed"}),
    "BLTD": ("past", {None: " believed that", "root": " believe that", "present-participle": " believing that", "past-participle": " believed that"}),

    # BG - To come (to)
    "BG": ("present", {None: " come", "3ps": " comes", "present-participle": " coming", "past-participle": " come"}),
    "BGT": ("present", {None: " come to", "3ps": " comes to", "present-participle": " coming to", "past-participle": " come to"}),
    "BGD": ("past", {None: " came", "root": " come", "present-participle": " coming", "past-participle": " come"}),
    "BGTD": ("past", {None: " came to", "root": " come to", "present-participle": " coming to", "past-participle": " come to"}),

    # RP - To do (it)
    "RP": ("present", {None: " do", "3ps": " does", "present-participle": " doing", "past-participle": " done"}),
    "RPT": ("present", {None: " do it", "3ps": " does it", "present-participle": " doing it", "past-participle": " done it"}),
    "RPD": ("past", {None: " did", "root": " do", "present-participle": " doing", "past-participle": " done"}),
    "RPTD": ("past", {None: " did it", "root": " do it", "present-participle": " doing it", "past-participle": " done it"}),

    # LS - To feel (like)
    "LS": ("present", {None: " feel", "3ps": " feels", "present-participle": " feeling", "past-participle": " felt"}),
    "LTS": ("present", {None: " feel like", "3ps": " feels like", "present-participle": " feeling like", "past-participle": " felt like"}),
    "LSZ": ("past", {None: " felt", "root": " feel", "present-participle": " feeling", "past-participle": " felt"}),
    "LTSDZ": ("past", {None: " felt like", "root": " feel like", "present-participle": " feeling like", "past-participle": " felt like"}),

    # PBLG - To find (that)
    "PBLG": ("present", {None: " find", "3ps": " finds", "present-participle": " finding", "past-participle": " found"}),
    "PBLGT": ("present", {None: " find that", "3ps": " finds that", "present-participle": " finding that", "past-participle": " found that"}),
    "PBLGD": ("past", {None: " found", "root": " find", "present-participle": " finding", "past-participle": " found"}),
    "PBLGTD": ("past", {None: " found that", "root": " find that", "present-participle": " finding that", "past-participle": " found that"}),

    # RG: To forget (to)
    "RG": ("present", {None: " forget", "3ps": " forgets", "present-participle": " forgetting", "past-participle": " forgotten"}),
    "RGT": ("present", {None: " forget to", "3ps": " forgets to", "present-participle": " forgetting to", "past-participle": " forgotten to"}),
    "RGD": ("past", {None: " forgot", "root": " forget", "present-participle": " forgetting", "past-participle": " forgotten"}),
    "RGTD": ("past", {None: " forgot to", "root": " forget to", "present-participle": " forgetting to", "past-participle": " forgotten to"}),

    # GS: To get (to)
    "GS": ("present", {None: " get", "3ps": " gets", "present-participle": " getting", "past-participle": " got"}),
    "GTS": ("present", {None: " get to", "3ps": " gets to", "present-participle": " getting to", "past-participle": " got to"}),
    "GSZ": ("past", {None: " got", "root": " get", "present-participle": " getting", "past-participle": " got"}),
    "GTSDZ": ("past", {None: " got to", "root": " get to", "present-participle": " getting to", "past-participle": " got to"}),

    # GZ: To give
    "GZ": ("present", {None: " give", "3ps": " gives", "present-participle": " giving", "past-participle": " given"}),
    "GDZ": ("past", {None: " gave", "root": " give", "present-participle": " giving", "past-participle": " given"}),

    # G: To go (to)
    "G": ("present", {None: " go", "3ps": " goes", "present-participle": " going", "past-participle": " gone"}),
    "GT": ("present", {None: " go to", "3ps": " goes to", "present-participle": " going to", "past-participle": " gone to"}),
    "GD": ("past", {None: " went", "root": " go", "present-participle": " going", "past-participle": " gone"}),
    "GTD": ("past", {None: " went to", "root": " go to", "present-participle": " going to", "past-participle": " gone to"}),

    # T - To have (to)
    "T": ("present", {None: " have", "3ps": " has", "present-participle": " having", "past-participle": " had"}),
    "TS": ("present", {None: " have to", "3ps": " has to", "present-participle": " having to", "past-participle": " had to"}),
    "TD": ("past", {None: " had", "root": " have", "present-participle": " having", "past-participle": " had"}),
    "TSDZ": ("past", {None: " had to", "root": " have to", "present-participle": " having to", "past-participle": " had to"}),

    # PB: To know (that)
    "PB": ("present", {None: " know", "3ps": " knows", "present-participle": " knowing", "past-participle": " known"}),
    "PBT": ("present", {None: " know that", "3ps": " knows that", "present-participle": " knowing that", "past-participle": " known that"}),
    "PBD": ("past", {None: " knew", "root": " know", "present-participle": " knowing", "past-participle": " known"}),
    "PBTD": ("past", {None: " knew that", "root": " know that", "present-participle": " knowing that", "past-participle": " known that"}),

    # BLG - To like
    "BLG": ("present", {None: " like", "3ps": " likes", "present-participle": " liking", "past-participle": " liked"}),
    "BLGT": ("present", {None: " like to", "3ps": " likes to", "present-participle": " liking to", "past-participle": " liked to"}),
    "BLGD": ("past", {None: " liked", "root": " like", "present-participle": " liking", "past-participle": " liked"}),
    "BLGTD": ("past", {None: " liked to", "root": " like to", "present-participle": " liking to", "past-participle": " liked to"}),

    # LZ - To live
    "LZ": ("present", {None: " live", "3ps": " lives", "present-participle": " living", "past-participle": " lived"}),
    "LDZ": ("past", {None: " lived", "root": " live", "present-participle": " living", "past-participle": " lived"}),

    # L - To look
    "L": ("present", {None: " look", "3ps": " looks", "present-participle": " looking", "past-participle": " looked"}),
    "LD": ("past", {None: " looked", "root": " look", "present-participle": " looking", "past-participle": " looked"}),

    # LG - To love
    "LG": ("present", {None: " love", "3ps": " loves", "present-participle": " loving", "past-participle": " loved"}),
    "LGD": ("past", {None: " loved", "root": " love", "present-participle": " loving", "past-participle": " loved"}),

    # LT - To let
    "LT": ("present", {None: " let", "3ps": " lets", "present-participle": " letting", "past-participle": " let"}),
    "LTD": ("past", {None: " let", "present-participle": " letting", "past-participle": " let"}),

    # RPBL - To make (the)
    "RPBL": ("present", {None: " make", "3ps": " makes", "present-participle": " making", "past-participle": " made"}),
    "RPBLT": ("present", {None: " make the", "3ps": " makes the", "present-participle": " making the", "past-participle": " made the"}),
    "RPBLD": ("past", {None: " made", "root": " make", "present-participle": " making", "past-participle": " made"}),
    "RPBLTD": ("past", {None: " made the", "root": " make the", "present-participle": " making the", "past-participle": " made the"}),

    # PL - To may
    # These do not combine well with do/can/shall/will
    "PL": ("present", " may"),
    "PLT": ("present", " may have"),
    "PLD": ("past", {None: " might", "root": " may"}),
    "PLTD": ("past", {None: " might have", "root": " may have"}),

    # PBL - To mean (that)
    "PBL": ("present", {None: " mean", "3ps": " means", "present-participle": " meaning", "past-participle": " meant"}),
    "PBLT": ("present", {None: " mean that", "3ps": " means that", "present-participle": " meaning that", "past-participle": " meant that"}),
    "PBLD": ("past", {None: " meant", "root": " mean", "present-participle": " meaning", "past-participle": " meant"}),
    "PBLTD": ("past", {None: " meant that", "root": " mean that", "present-participle": " meaning that", "past-participle": " meant that"}),

    # PLZ - To move
    "PLZ": ("present", {None: " move", "3ps": " moves", "present-participle": " moving", "past-participle": " moved"}),
    "PLDZ": ("past", {None: " moved", "root": " move", "present-participle": " moving", "past-participle": " moved"}),

    # RPG: To need (to)
    "RPG": ("present", {None: " need", "3ps": " needs", "present-participle": " needing", "past-participle": " needed"}),
    "RPGT": ("present", {None: " need to", "3ps": " needs to", "present-participle": " needing to", "past-participle": " needed to"}),
    "RPGD": ("past", {None: " needed", "root": " need", "present-participle": " needing", "past-participle": " needed"}),
    "RPGTD": ("past", {None: " needed to", "root": " need to", "present-participle": " needing", "past-participle": " needed to"}),

    # RL - To recall
    "RL": ("present", {None: " recall", "3ps": " recalls", "present-participle": " recalling", "past-participle": " recalled"}),
    "RLD": ("past", {None: " recalled", "root": " recall", "present-participle": " recalling", "past-participle": " recalled"}),

    # RLS - To realize (that)
    "RLS": ("present", {None: " realize", "3ps": " realizes", "present-participle": " realizing", "past-participle": " realized"}),
    "RLTS": ("present", {None: " realize that", "3ps": " realizes that", "present-participle": " realizing that", "past-participle": " realized that"}),
    "RLSZ": ("past", {None: " realized", "root": " realize", "present-participle": " realizing", "past-participle": " realized"}),
    "RLTSDZ": ("past", {None: " realized that", "root": " realize that", "present-participle": " realizing that", "past-participle": " realized that"}),

    # RPL - To remember (that)
    "RPL": ("present", {None: " remember", "3ps": " remembers", "present-participle": " remembering", "past-participle": " remembered"}),
    "RPLT": ("present", {None: " remember that", "3ps": " remembers that", "present-participle": " remembering that", "past-participle": " remembered that"}),
    "RPLD": ("past", {None: " remembered", "root": " realize", "present-participle": " remembering", "past-participle": " remembered"}),
    "RPLTD": ("past", {None: " remembered that", "root": " remember that", "present-participle": " remembering that", "past-participle": " remembered that"}),

    # R - To run
    "R": ("present", {None: " run", "3ps": " runs", "present-participle": " running", "past-participle": " run"}),
    "RD": ("past", {None: " ran", "root": " run", "present-participle": " running", "past-participle": " run"}),

    # BS - To say (that)
    "BS": ("present", {None: " say", "3ps": " says", "present-participle": " saying", "past-participle": " said"}),
    "BTS": ("present", {None: " say that", "3ps": " says that", "present-participle": " saying that", "past-participle": " said that"}),
    "BSZ": ("past", {None: " said", "root": " say", "present-participle": " saying", "past-participle": " said"}),
    "BTSDZ": ("past", {None: " said that", "root": " say that", "present-participle": " saying that", "past-participle": " said that"}),

    # S - To see
    "S": ("present", {None: " see", "3ps": " sees", "present-participle": " seeing", "past-participle": " seen"}),
    "SZ": ("past", {None: " saw", "root": " see", "present-participle": " seeing", "past-participle": " seen"}),

    # PLS - To seem (to)
    "PLS": ("present", {None: " seem", "3ps": " seems", "present-participle": " seeming", "past-participle": " seemed"}),
    "PLTS": ("present", {None: " seem to", "3ps": " seems to", "present-participle": " seeming to", "past-participle": " seemed to"}),
    "PLSZ": ("past", {None: " seemed", "root": " seem", "present-participle": " seeming", "past-participle": " seemed"}),
    "PLTSDZ": ("past", {None: " seemed to", "root": " seem to", "present-participle": " seeming to", "past-participle": " seemed to"}),

    # RT - To take
    "RBT": ("present", {None: " take", "3ps": " takes", "present-participle": " taking", "past-participle": " taken"}),
    "RBTD": ("past", {None: " took", "root": " take", "present-participle": " taking", "past-participle": " taken"}),

    # RLT - To tell
    "RLT": ("present", {None: " tell", "3ps": " tells", "present-participle": " telling", "past-participle": " told"}),
    "RLTD": ("past", {None: " told", "root": " tell", "present-participle": " telling", "past-participle": " told"}),

    # PBG - To think (that)
    "PBG": ("present", {None: " think", "3ps": " thinks", "present-participle": " thinking", "past-participle": " thought"}),
    "PBGT": ("present", {None: " think that", "3ps": " thinks that", "present-participle": " thinking that", "past-participle": " thought that"}),
    "PBGD": ("past", {None: " thought", "root": " think", "present-participle": " thinking", "past-participle": " thought"}),
    "PBGTD": ("past", {None: " thought that", "root": " think that", "present-participle": " thinking that", "past-participle": " thought that"}),

    # RT - To try (to)
    "RT": ("present", {None: " try", "3ps": " tries", "present-participle": " trying", "past-participle": " tried"}),
    "RTS": ("present", {None: " try to", "3ps": " tries to", "present-participle": " trying to", "past-participle": " tried to"}),
    "RTD": ("past", {None: " tried", "root": " try", "present-participle": " trying", "past-participle": " tried"}),
    "RTSDZ": ("past", {None: " tried to", "root": " try to", "present-participle": " trying to", "past-participle": " tried to"}),

    # PBG - To understand (the)
    "RPB": ("present", {None: " understand", "3ps": " understands", "present-participle": " understanding", "past-participle": " understood"}),
    "RPBT": ("present", {None: " understand the", "3ps": " understands the", "present-participle": " understanding the", "past-participle": " understood the"}),
    "RPBD": ("past", {None: " understood", "root": " understand", "present-participle": " understanding", "past-participle": " understood"}),
    "RPBTD": ("past", {None: " understood the", "root": " understand the", "present-participle": " understanding the", "past-participle": " understood the"}),

    # Z - To use
    "Z": ("present", {None: " use", "3ps": " uses", "present-participle": " using", "past-participle": " used"}),
    "DZ": ("past", {None: " used", "root": " use", "present-participle": " using", "past-participle": " used"}),

    # P: To want (to)
    "P": ("present", {None: " want", "3ps": " wants", "present-participle": " wanting", "past-participle": " wanted"}),
    "PT": ("present", {None: " want to", "3ps": " wants to", "present-participle": " wanting to", "past-participle": " wanted to"}),
    "PD": ("past", {None: " wanted", "root": " want", "present-participle": " wanting", "past-participle": " wanted"}),
    "PTD": ("past", {None: " wanted to", "root": " want to", "present-participle": " wanting to", "past-participle": " wanted to"}),

    # RBG - To work
    "RBG": ("present", {None: " work", "3ps": " works", "present-participle": " working", "past-participle": " worked"}),
    "RBGD": ("past", {None: " worked", "root": " work", "present-participle": " working", "past-participle": " worked"}),
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

    base = MIDDLES_BASE[vowels1 + star]
    middle_word, updated_verb_form = lookup_data(
        lookup_data(base, tense), verb_form)

    modifier = MIDDLE_MODIFIER_EXCEPTIONS.get(
        starter + vowels1 + star + vowels2 + f)
    if not modifier:
        modifier = MIDDLE_MODIFIER_EXCEPTIONS.get(vowels1 + star + vowels2 + f)
    if not modifier:
        modifier = MIDDLES_MODIFIERS[star + vowels2 + f]
    modifier_format, use_base_verb_form, modifier_verb_update = modifier

    if use_base_verb_form:
        if updated_verb_form:
            verb_form = updated_verb_form

    middle_word = lookup_data(lookup_data(
        modifier_format, tense), verb_form).replace('*', middle_word, 1)

    if '!' in middle_word:
        result = middle_word.replace('!', result)
    else:
        result += middle_word

    if modifier_verb_update:
        verb_form = modifier_verb_update

    ending = lookup_data(verb, verb_form)
    if ending == None:
        raise KeyError

    result += ending

    return result


def lookup_data(data, key):
    if type(data) is not dict:
        return data

    result = data.get(key)
    if result != None:
        return result

    if key[0] == 'b':
        result = data.get(key[1:])
        if result != None:
            return result

    return data.get(None)

# Proper reverse lookup support.
#
# This will show phrasing strokes in Plover's suggestions window.


REVERSE_STARTERS = { "": {"": True}}
REVERSE_MIDDLES_BASE = {}
REVERSE_MODIFIERS = {}
REVERSE_ENDERS = {}
REPLACEMENTS = []
REPLACEMENTS_SET = {}

for key in STARTERS:
    word = STARTERS[key][0]
    REVERSE_STARTERS.setdefault(word, {})
    REVERSE_STARTERS[word][key] = True

POSSIBLE_REVERSE_MATCH = re.compile(r"[a-zI ']+")
HYPHEN_OMIT_PATTERN = re.compile(r"[AO*EU-]")


def add_reverse_middles_base(stroke, data):
    if type(data) is dict:
        for k in data:
            add_reverse_middles_base(stroke, data[k])
        return

    word = data[0].strip()
    if ' ' in word:
        replacement = word.replace(' ', '_')
        if word not in REPLACEMENTS_SET:
            REPLACEMENTS.append((word, replacement))
            REPLACEMENTS_SET[word] = True
        word = replacement

    REVERSE_MIDDLES_BASE.setdefault(word, {})
    REVERSE_MIDDLES_BASE[word][stroke] = True


def add_reverse_middle_modifiers(stroke, data):
    if type(data) is dict:
        for k in data:
            add_reverse_middle_modifiers(stroke, data[k])
        return

    word = data.replace('*', '').strip()

    replacement = word

    if ' ' in word:
        replacement = replacement.replace(' ', '_')

    REVERSE_MODIFIERS.setdefault(replacement, {})
    REVERSE_MODIFIERS[replacement][stroke] = True

    if not data.startswith(' ') and not data.startswith('*') and data != '':
        replacement = ' ' + replacement

    if replacement != word:
        if word not in REPLACEMENTS_SET:
            REPLACEMENTS.append((word, replacement))
            REPLACEMENTS_SET[word] = True


def add_reverse_enders(stroke, data):
    if type(data) is dict:
        for k in data:
            add_reverse_enders(stroke, data[k])
        return

    word = data.strip()
    REVERSE_ENDERS.setdefault(word, {})
    REVERSE_ENDERS[word][stroke] = True


for key in MIDDLE_MODIFIER_EXCEPTIONS:
    add_reverse_middle_modifiers(key, MIDDLE_MODIFIER_EXCEPTIONS[key][0])

for key in MIDDLES_BASE:
    add_reverse_middles_base(key, MIDDLES_BASE[key])

for key in MIDDLES_MODIFIERS:
    add_reverse_middle_modifiers(key, MIDDLES_MODIFIERS[key][0])

for key in ENDERS:
    add_reverse_enders(key, ENDERS[key][1])


def reverse_match(result, full_text, prefix):
    try:
        if lookup([prefix]).strip() == full_text:
            result.append((prefix,))
    except KeyError:
        pass


def add_verb_stroke(prefix, suffix):
    # This check enables finding `STRWU` special prefix words.
    if suffix.startswith(prefix):
        return suffix

    # This check prevents adding in extra '-' when it will cause issues in lookup().
    if HYPHEN_OMIT_PATTERN.search(prefix) or HYPHEN_OMIT_PATTERN.search(suffix):
        return prefix + suffix

    return prefix + '-' + suffix


def reverse_verb_match(result, full_text, text, prefix):
    if len(text) > 0:
        if text[0] == '_':
            text = text[1:]
        text = text.replace('_', ' ')

    if text not in REVERSE_ENDERS:
        return

    prefix = prefix.replace('**', '*', 1)
    for stroke in REVERSE_ENDERS[text]:
        reverse_match(result, full_text, add_verb_stroke(prefix, stroke))


def reverse_modifier_match(result, full_text, text, prefix):
    word = text.split(' ', 1)[0]

    match = PARTS_MATCHER.fullmatch(prefix)
    has_starter = match.group(1) != '' if match else False

    if not has_starter:
        if word in REVERSE_STARTERS:
            for stroke in REVERSE_STARTERS[word]:
                subject_stroke = add_verb_stroke(stroke, prefix)

                for reverse_modifier_stroke in REVERSE_MODIFIERS['!']:
                    reverse_verb_match(result, full_text, text.replace(
                        word, '', 1).strip(), add_verb_stroke(subject_stroke, reverse_modifier_stroke))
    else:
        if word in REVERSE_MODIFIERS:
            for stroke in REVERSE_MODIFIERS[word]:
                reverse_verb_match(result, full_text, text.replace(
                    word, '', 1).strip(), add_verb_stroke(prefix, stroke))

        if '_' in word:
            word = word.split('_', 1)[0]
            for stroke in REVERSE_MODIFIERS[word]:
                reverse_verb_match(result, full_text, text.replace(
                    word, '', 1).strip(), add_verb_stroke(prefix, stroke))

        for stroke in REVERSE_MODIFIERS['']:
            reverse_verb_match(result, full_text, text,
                            add_verb_stroke(prefix, stroke))


def reverse_middle_base_match(result, full_text, text, prefix):
    for word in REVERSE_MIDDLES_BASE:
        if word in text:
            for stroke in REVERSE_MIDDLES_BASE[word]:
                reverse_modifier_match(result, full_text, text.replace(
                    word, '', 1).strip(), prefix + stroke)

    reverse_modifier_match(result, full_text, text, prefix)


def reverse_lookup(text):
    if not POSSIBLE_REVERSE_MATCH.fullmatch(text):
        return []

    full_text = text

    for key, replacement in REPLACEMENTS:
        text = text.replace(key, replacement)

    if len(text.split(' ')) > 6:
        return []

    result = []

    words = text.split(' ', 1)
    if words[0] in REVERSE_STARTERS:
        remainder = words[1].strip() if len(words) > 1 else ''
        for stroke in REVERSE_STARTERS[words[0]]:
            reverse_middle_base_match(result, full_text, remainder, stroke)
    else:
        for stroke in REVERSE_STARTERS['']:
            reverse_middle_base_match(result, full_text, text, stroke)

    return result
