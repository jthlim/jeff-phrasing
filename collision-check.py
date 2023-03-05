import json
import re

import importlib
jeff_phrasing = importlib.import_module("jeff-phrasing")

PARTS_MATCHER = re.compile(
    r'(S?T?K?P?W?H?R?)(A?O?)-?(\*?)(E?U?)(F?)(R?P?B?L?G?T?S?D?Z?)'
)

# These are strokes that are okay to remove, typically because they are mis-stroke entries
# spellchecker: disable
AUDITED_STROKES = {
    "SWR": True,          # 'Somewhere' -- Use 'SW-R' instead
    "SWR-S": True,        # 'Somewheres' -- use 'SW-RS' instead
    "KPWRAEUT": True,     # 'Grate'   -- '`TKPWRAEUT`
    "KPWROUR": True,      # 'Your'    -- 'KWROUR'
    "KWHR": True,         # 'Why'     -- 'KWR'
    "KWHRAOERL": True,    # 'Clearly' -- 'KHRAOERL'
    "KWHRE": True,        # 'Yes'     -- 'KWRE'
    "TWHA": True,         # 'That'    -- 'THA'
    "KWHRAOER": True,     # 'Year'    -- 'KWRAOER'
    "SKWHRAR": True,      # 'Scholar' -- 'SKHRAR'
    "TWRAGS": True,       # 'Tradition' -- 'TRAGS'
    "KPWHAOUPBT": True,   # 'Community' -- 'KPHAOUPBT'
    "KPWHEUPBGS": True,   # 'Combination' -- 'KPWEUPBGS'
    "SWR-PBT": True,      # 'Haven't' -- 'SR-PBT'
    "TWRAOEUD": True,     # 'Divide' -- 'TKWAOEUD'
    "SKWHRAEUB": True,    # 'Jane' -- 'SKWRAEUB'
    "KWHREBGT": True,     # 'Collect' -- 'KHREBGT'
    "KPWRAOELD": True,    # 'Yield' -- 'KWRAOELD'
    "STKPWHRAEU": True,   # 'Display' -- 'STKPHRAUE'
    "TWRAFR": True,       # 'Transfer' -- 'TRAFR'
    "TWHEPL": True,       # 'Them' -- 'THEPL'
    "SKWHREPL": True,     # 'Generally' -- 'SKWHREPBL'
    "KPWHRAEUPB": True,   # 'Complain' -- "KPHRAEUPB"
    "KPWHRAEUPBG": True,  # 'Complaining' -- "KPHRAEUPBG"
    "STPHRAEUPB": True,   # 'Explain' -- "SPHRAUEPB"
    "STPHRAOUGS": True,   # 'Institution' -- "STPHAOUGS"
    "STPHRAOER": True,    # 'Sphere' -- "STPAOER"
    "STPAEUS": True,      # 'Space' -- "SPAEUS"
    "STPAEURL": True,     # 'Fairly' -- "TPAEURL"
    "STHAEUR": True,      # 'Their' -- "THAEUR"
    "STKPWHRURBGS": True, # 'Jurisdiction' -- "SKWRURBGS"

    # Things that seem better alternates already exist
    "STKPWHR-FPLT": True,  # "!" -- expect TP-BG, or other form to be used.
    "SWHEPB": True,        # "when is" -- "WH-S" seems easier
    "SKPET": True,         # "and the" -- probably a typo entry for "SKP-T"

    # Things that are superceded by this phrasing system.
    "KPWROEU": True,    # "I don't"
    "KWHROEPB": True,   # "I don't know"
    "SWRAOE": True,     # "we have"
    "SWROEPBT": True,   # "won't have"
    "STHAEUD": True,    # "said that"
    "SWHAE": True,      # "what she"
    "SWHE": True,       # "when she"
    "STHAE": True,      # "that she"
    "SWRE": True,       # "where she"
    "SWHOE": True,      # "who she"
    "SKPEUBS": True,    # "and I said"
    "SKPEUBG": True,    # "and I can"
    "SKPEBG": True,     # "and he can"
    "SKPUBG": True,     # "and you can"
    "SKPUF": True,      # "and you have"
    "SKPEURBD": True,   # "and I should"
    "SKPEUFS": True,    # "and I was"

    # Things that are identitcal
    "SKPE": True,       # "and he"
    "SKPEU": True,      # "and I"
    "SKPU": True,       # "and you"

    # Things that are okay to lose:
    "TWHAPBG": True,    # "thwang"
    "TWHABG": True,     # "thwack"
}
# spellchecker: enable


def increment_collision_counter(dict, key, collision_count):
    dict[key] = dict.get(key, 0) + collision_count


with open("main.json") as main_data:
    main_dict = json.load(main_data)
    print("Loaded dict with %d entries" % len(main_dict))

    defined_strokes = {}
    simple_defined_strokes = {}

    for strokes in main_dict:
        if strokes in AUDITED_STROKES:
            continue

        if strokes in jeff_phrasing.NON_PHRASE_STROKES:
            continue

        if '/' in strokes:
            continue

        match = PARTS_MATCHER.match(strokes)
        if not match:
            continue

        # Tally full form
        starter, v1, star, v2, f, ending = match.groups()
        key = starter + "-" + ending
        dict = defined_strokes.get(key)
        if not dict:
            dict = {}
            defined_strokes[key] = dict

        dict[strokes] = main_dict[strokes]

        # Tally simple form.
        if (star + v2) not in jeff_phrasing.SIMPLE_PRONOUNS:
            continue

        key = starter + v1 + '-' + ending
        dict = simple_defined_strokes.get(key)
        if not dict:
            dict = {}
            simple_defined_strokes[key] = dict

        dict[strokes] = main_dict[strokes]

    starter_collisions = {}
    ender_collisions = {}
    simple_starter_collisions = {}

    count = 0

    # Full form
    for starter in jeff_phrasing.STARTERS:
        enders = jeff_phrasing.STARTERS[starter][2]
        if enders == None:
            enders = jeff_phrasing.ENDERS
        for ender in enders:
            key = starter + "-" + ender
            if key in defined_strokes:
                collision_count = len(defined_strokes[key])
                print('Match on %s' % key)
                print(defined_strokes[key])
                print('')
                increment_collision_counter(
                    starter_collisions, starter, collision_count)
                increment_collision_counter(
                    ender_collisions, ender, collision_count)
                count = count + collision_count

    # Simple form
    for starter in jeff_phrasing.SIMPLE_STARTERS:
        for ender in jeff_phrasing.ENDERS:
            key = starter + "-" + ender
            if key in simple_defined_strokes:
                collision_count = len(simple_defined_strokes[key])
                print('Alt match on %s' % key)
                print(simple_defined_strokes[key])
                print('')
                increment_collision_counter(
                    simple_starter_collisions, starter, collision_count)
                increment_collision_counter(
                    ender_collisions, ender, collision_count)
                count = count + collision_count

    print('Collisions caused by starters')
    for k in starter_collisions:
        print(' %s: %d' % (k, starter_collisions[k]))

    print('')
    print('Collisions caused by simple-starters')
    for k in simple_starter_collisions:
        print(' %s: %d' % (k, simple_starter_collisions[k]))

    print('')
    print('Collisions caused by enders')
    for k in ender_collisions:
        print(' %s: %d' % (k, ender_collisions[k]))

    print('')
    print('Total collisions: %d' % count)
