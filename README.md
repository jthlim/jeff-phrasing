# Jeff's phrasing dictionary for Plover

# Background

In many systems, there are strokes possible where the phrases formed are
typically unusable. For example, the verb endings or tense could mismatch, such
as: `I really doesn't wanted`.

This phrasing dictionary automatically matches tenses and verb forms,
which makes it easier to learn because there's less to remember. With the
key-space freed up, extra flexibility has been added to enable more expressive
phrases.

Some examples:
* `SWRGT` produces `I go to`
* `KWHRGT` produces `He goes to`
* `SWRGTD` produces `I went to`
* `KWHRGTD` produces `He went to`
* `SWRAEFGTD` produces `I could have gone to`
* `KWHRO*EUFGTD` produces `He really shouldn't go to`
* `KWHRO*EGTD` produces `He shouldn't be going to`
* `SWRAOFGTD` produces `I would never go to`
* `SWR-RPBT` produces `I understand the`
* `SWRA*EURPBT` produces `I still can't understand the`
* `SWR*UFPBTD/TWRAOEPBLGD` produces `I just didn't know that we would be finding`

Many decisions on the word choices were taken from statistical data and
Google Books N-gram Viewer.

This dictionary also supports full reverse lookup, so you can see how to
stroke phrases in Plover's suggestions window.

# Warning
This is currently a work in progress. Expect changes in future versions.

# System

The phrase is constructed in 5 parts:

1. A starter (`I`, `you`, `he`, `she`, `it`, `we`, `they`)
2. An optional `do`/`can`/`shall`/`will` or their negative or past tense forms
3. A optional modifier word `really`/`just`/`still`/`never`/`even`/`have`/`be`
4. A verb e.g. `go`, `say`, `understand`, etc.
5. An optional suffix word 

For example: `SWRO*EGTD`: `I shouldn't be going to` 

1. `SWR` is the starter: 'I'
2. `O*` is 'shouldn't'
3. `E` is 'be'
4. `G` is 'go'
5. `T` is 'to'

The phrase will generally be constructed in a manner that seems grammatically correct:

Example 1:
  * `SWRG` produces `I go`
  * `SWRGD` produces `I went` (`-D` for past tense)
  * `SWRAGD` produces `I could go` -- the addition of 'can' in past tense becomes 'could' and 'went' changes to 'go'.
  * `SWREG` produces `I am going`
  * `SWREGD`: produces `I was going`
  * `SWRAOEGD`: produces `I would be going`
 
Example 2:
  *  `SWREUFB`: produces `I really am`
  *  `SWREUFBD`: produces `I really was`
  *  `SWROEUFBD`: produces `I really should be`
 
## Starters

Starters are all formed on the left hand side of the board:
```
🆂🆃🅿🅷 🄾 🄵🄿🄻🅃🄳
🆂🅺🆆🆁 🄾 🅁🄱🄶🅂🅉
　　　🄰🄾 🄴🅄
```

* `SWR`: `I`
* `KPWR`: `you`
* `KWHR`: `he`
* `SKWHR`: `she`
* `KPWH`: `it`
* `TWH`: `they`
* `STKPWHR`: <empty -- third person singular form>
* `STWR`: <empty -- root form>

Example usage of of `STWR` and `STKPWHR`:
* `SWR-RPGT/STWRURPBT` produces 'I need to just understand the'
* `KWHR-PL/STWR-FPBT` produces 'he may have known that'
* `SWREUFPLD/STWR-RPGT/STWR-GT` produces 'I really might need to go to'
* `SKWRAEUPB/STKPWHR-FGT` produces 'Jane never goes to'

## Do, Can, Shall, Will
```
🅂🅃🄿🄷 🅾 🄵🄿🄻🅃🄳
🅂🄺🅆🅁 🅾 🅁🄱🄶🅂🅉
　　　🅰🅾 🄴🅄
```

The keys `AO*` are used to determine which of the additional words are added.
The form that is added depends on the tense of the verb. `*` is added to
get the negative version.

| `A O` | Word            | Negative forms           |
| ----- | --------------- | ------------------------ |
| `_ _` | do / does / did | don't / doesn't / didn't |
| `_ O` | shall / should  | shall not / shouldn't    |
| `A _` | can / could     | can't / couldn't         |
| `A O` | will / would    | won't / wouldn't         |

To get `did`, `should`, `could`, `would`, use a past tense verb (or past tense
placeholder `-D`).

## Modifiers

```
🅂🅃🄿🄷 🄾 🅵🄿🄻🅃🄳
🅂🄺🅆🅁 🄾 🅁🄱🄶🅂🅉
　　　🄰🄾 🅴🆄
```

`EUF` controls how the words `really`, `just`, `still`, `never`, `even`, 
`be` and `have`.

The way these work is sometimes dependent upon whether '*' is used.

* `still` is used as a prefix for negative forms, and as a suffix
for positive form:

  * `...AEU...`: `... can still ...`
  * `...A*EU..`: `... still can't ...`

* `-F` appends the word `never` for positive forms, and `even` for negative
  forms.

  * `...AF...`: `... can never ...`
  * `...A*F...`: `... can't even ...`

Full table:

| `* E U F` | Modifier                |
| --------- | ----------------------- |
| `? _ _ _` | <empty>                 |
| `_ _ _ F` | {} ne**v**er            |
| `* _ _ F` | {} e**v**en             |
| `? _ U _` | {} j**u**st             |
| `? _ U F` | j**u**st {}             |
| `_ E U _` | {} st**i**ll            |
| `* E U _` | st**i**ll {}            |
| `? E U F` | really {}               |
| `? E _ _` | 'be' + -ing verb form   |
| `? E _ F` | 'have' + past verb form |

Examples:
* `SWRUPB` produces: `I just know`
* `SWREGTD` produces:  `I am going to`
* `SWROEGTD` produces:  `I should be going to`

An exception is for `do`:

| `A O * E U F` | Result                    |
| ------------- | ------------------------- |
| `_ _ _ _ _ _` | <empty>                   |
| `_ _ _ _ _ F` | ne**v**er                 |
| `_ _ _ _ U _` | j**u**st                  |
| `_ _ _ _ U F` | {}                        |
| `_ _ _ E _ _` | be + -ing verb form       |
| `_ _ * E _ _` | not be + -ing verb form   |
| `_ _ _ E _ F` | have + past verb form     |
| `_ _ * E _ F` | have not + past verb form |
| `_ _ _ E U _` | st**i**ll                 |
| `_ _ _ E U F` | really                    |

This allows typing phrases such as:

* `SWREUG`: `I still go`
* `KPWRFBSD`: `you never said`
* `SWREGT`: `I am going to`
* `SWREFGT`: `I have gone to`

## Verbs and suffix words

All verbs have a present and past tense version. The past tense is formed by
adding `-D`, unless the verb includes `-S`, in which case `-Z` is used instead.

Suffix words are indicated in parentheses, and are added by using `-T`. If the
stroke includes `-T`, then `-S` is used instead.

For past tense with suffix words that cause a diagonal to be formed
(`-TZ` or `-SD`), then `-TSDZ` is used instead.

| Stroke | Meaning (-T)        |
| ------ | ------------------- |
| ``     | <empty>             |
| `D`    | <empty, past tense> |
| `B`    | To be (the)         |
| `BL`   | To believe (that)   |
| `BG`   | To come (to)        |
| `RP`   | To do (it)          |
| `PBLG` | To find (that)      |
| `RG`   | To forget (to)      |
| `GS`   | To get (to)         |
| `GZ`   | To give             |
| `G`    | To go (to)          |
| `T`    | To have (to)        |
| `PB`   | To know (that)      |
| `BLG`  | To like (to)        |
| `LZ`   | To live             |
| `L`    | To look             |
| `LG`   | To love             |
| `LT`   | To let              |
| `RPBL` | To make (the)       |
| `PL`   | may/might (have)    |
| `PLZ`  | To move             |
| `RPG`  | To need (to)        |
| `RLS`  | To realize (that)   |
| `RL`   | To recall (that)    |
| `RPL`  | To remember (that)  |
| `R`    | To run              |
| `BS`   | To say (to)         |
| `S`    | To see              |
| `PLS`  | To seem (to)        |
| `RBT`  | To take             |
| `PBG`  | To think (that)     |
| `RT`   | To try (to)         |
| `RPB`  | To understand (the) |
| `Z`    | To use              |
| `P`    | To want (to)        |
| `RBG`  | To work             |

Examples:
*  `SWRB`: `I am`
*  `KPWRB`:  `you are`
*  `SWRAB`: `I can be`

# Installation

1. In plover, first install plover-python-dictionary
2. Save jeff-phrasing.py from this repository
3. Drag and drop the file into plover.

You may also be interested in:
* [jeff-modifiers](https://github.com/jthlim/jeff-modifiers)
* [jeff-numbers](https://github.com/jthlim/jeff-numbers)
* [jeff-visual-stroke](https://github.com/jthlim/jeff-visual-stroke)

# Credits
This dictionary takes inspiration from both Jade and Aerick's phrasing systems.