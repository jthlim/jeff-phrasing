# Jeff's phrasing dictionary for Plover

# Background

In many systems, there are strokes possible where the phrases formed are
typically unusable. For example, the verb endings or tense could mismatch, such
as: `I really doesn't wanted`.

This phrasing dictionary automatically matches tenses and verb forms,
which makes it easier to learn and memorize. You can write the following
phrases in a single stroke:
* `KWHRG`: `He goes`
* `KWHRO*EGD`: `He shouldn't really go`
* `SWR-RPB`: `I understand`
* `SWRA*EUFRPB`: `I still can't understand`
* `SWRGD`: `I went`
* `SWRAOUGD`: `I would just go`

Many decisions on the word choices were taken from statistical data and
Google Books N-gram Viewer.

This dictionary takes inspiration from Jade and Aerick's phrasing systems,
and is currently a work in progress. Expect changes in future versions.

# System

The phrase is constructed with:

1. A starter (`I`, `you`, `he`, `she`, `it`, `we`, `they`)
2. An optional `do`/`shall`/`will`/`can` or their negative or past tense forms combined with `really`/`just`/`still`/`even`
3. A verb ending e.g. `have`,`go`
4. An optional suffix word 

For example: `SWR*ERPGT`: `I don't really need to` 

1. `SWR` is the starter: 'I'
2. `*E` is 'don't really'
3. `RPG` is 'need'
4. `T` is 'to'

The phrase will always be constructed in a manner that seems grammatically correct:

Example 1:
  * `SWRG`: produces `I go`
  * `SWRGD`: produces `I went` (`-D` for past tense)
  * `SWRAGD`: produces ` I could go` -- the addition of 'can' in past tense becomes 'could' and 'went' changes to 'go'.

Example 2:
  *  `SWREB`: produces `I really am`
  *  `SWREBD`: produces `I really was`
  *  `SWROEBD`: produces `I should really be`

## Starters

Starters are all formed on the left hand side of the board:
```
🆂🆃🅿🅷 🄾 🄵🄿🄻🅃🄳
🆂🅺🆆🆁 🄾 🅁🄱🄶🅂🅉
　　　🄰🄾 🄴🅄
```

* `SWR`: I
* `KPWR`: you
* `KWHR`: he
* `SKWHR`: she
* `KPWH`: it
* `TWH`: they
* `STWR`: <empty -- third person singular form>
* `STKPWHR`: <empty -- third person plural form>

## Do, Should, Would, Could
```
🅂🅃🄿🄷 🅾 🄵🄿🄻🅃🄳
🅂🄺🅆🅁 🅾 🅁🄱🄶🅂🅉
　　　🅰🅾 🄴🅄
```

The keys `AO*` are used to determine which of the additional words are added.
The form that is added depends on the tense of the verb. `*` is used to provide
the negative version.

| `A O` | Word            | Negative forms           |
| ----- | --------------- | ------------------------ |
| `_ _` | do / does / did | don't / doesn't / didn't |
| `_ O` | shall / should  | shall not / shouldn't    |
| `A _` | can / could     | can't / couldn't         |
| `A O` | will / would    | won't / wouldn't         |

To get `did`, `should`, `could`, `would`, use a past tense verb (or past tense
placeholder `-D`).

## Really, Just, Even, Still

```
🅂🅃🄿🄷 🄾 🅵🄿🄻🅃🄳
🅂🄺🅆🅁 🄾 🅁🄱🄶🅂🅉
　　　🄰🄾 🅴🆄
```

`EUF` controls how the adverbs `really`, `just`, `even` and `still` combine
with `do`, `should`, `could`, `would`. `EU` select the word, while `F` will
swap the order. `F` by itself appends the word `even`

| `E U F` | Word          |
| ------- | ------------- |
| `_ _ _` | <empty>       |
| `_ _ F` | {} e**v**en   |
| `E _ _` | {} r**e**ally |
| `E _ F` | r**e**ally {} |
| `_ U _` | {} j**u**st   |
| `_ U F` | just {}       |
| `E U _` | {} st**i**ll  |
| `E U F` | st**i**ll {}  |

Examples:
* `A*E` produces: `can't really`
* `A*EF` produces: `really can't`

An exception is for `do` (and only the positive form), which is when
neither `A` nor `O` are pressed.

| `A O * E U F` | Result        |
| ------------- | ------------- |
| `_ _ _ _ _ _` | <empty>       |
| `_ _ _ _ _ F` | e**v**en      |
| `_ _ _ _ U _` | j**u**st      |
| `_ _ _ _ U F` | {}            |
| `_ _ _ E _ _` | r**e**ally    |
| `_ _ _ E _ F` | r**e**ally do |
| `_ _ _ E U _` | st**i**ll     |
| `_ _ _ E U F` | st**i**ll do  |

This allows typing phrases such as:
* `SWREUG`: `I still go`
* `KPWRFBSD`: `You even said`
* `SWRUFPBG`: `I do think`

## Verbs

All verbs have a present and past tense version. The past tense is formed by
adding `-D`, unless the verb includes `-S`, in which case `-Z` is used

| Stroke | Meaning (-T)        |
| ------ | ------------------- |
| ``     | <empty>             |
| `D`    | <empty, past tense> |
| `B`    | To be (the)         |
| `BL`   | To believe (that)   |
| `BG`   | To come (to)        |
| `PBLG` | To find (the)       |
| `RG`   | To forget (to)      |
| `GT`   | To get              |
| `GZ`   | To give             |
| `G`    | To go               |
| `T`    | To have (to)        |
| `PB`   | To know (that)      |
| `BLG`  | To like             |
| `LZ`   | To live             |
| `L`    | To look             |
| `LG`   | To love             |
| `LT`   | To let              |
| `RPBL` | To make             |
| `RPG`  | To need (to)        |
| `RLS`  | To realize (that)   |
| `RL`   | To recall           |
| `RLT`  | To relate           |
| `RPL`  | To remember (that)  |
| `R`    | To run              |
| `BS`   | To say              |
| `S`    | To see              |
| `PLS`  | To seem (to)        |
| `PBG`  | To think (that)     |
| `RT`   | To try              |
| `RPB`  | To understand (the) |
| `Z`    | To use              |
| `P`    | To want (to)        |
| `RBG`  | To work             |

Examples:
*  `SWREB`: I really am
*  `SWR*UTD`: I didn't just have

# Installation

1. In plover, first install plover-python-dictionary
2. Save jeff-phrasing.py from this repository
3. Drag and drop the file into plover.

You may also be interested in:
* [jeff-modifiers](https://github.com/jthlim/jeff-modifiers)
* [jeff-numbers](https://github.com/jthlim/jeff-numbers)
* [jeff-visual-stroke](https://github.com/jthlim/jeff-visual-stroke)
