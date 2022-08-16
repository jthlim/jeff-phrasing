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
* `SWRAFGTD` produces `I could have gone to`
* `KWHRO*UFGTD` produces `He just shouldn't go to`
* `KWHRO*EGTD` produces `He shouldn't be going to`
* `SWRAOEUFGTD` produces `I would never go to`
* `SWREFGT` produces `I've been going to`
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

The phrase is constructed in 6 parts:

1. A starter (`I`, `you`, `he`, `she`, `it`, `we`, `they`)
2. An optional `do`/`can`/`shall`/`will` or their negative or past tense forms
3. A optional modifier word `just`/`still`/`never`/`even`/`have`/`be`
4. A verb e.g. `go`, `say`, `understand`, etc.
5. An optional suffix word 
6. A tense

For example: `SWRO*FGTD`: `I shouldn't have gone to` 

1. `SWR` is the starter: 'I'
2. `O*` is 'shouldn't'
3. `F` is 'have'
4. `G` is 'go'
5. `T` is 'to'
6. `D` is for past tense

The phrase will generally be constructed in a manner that seems grammatically correct:

Example 1:
  * `SWR-G` produces `I go`
  * `SWR-GD` produces `I went`
  * `SWRAGD` produces `I could go` -- the addition of 'can' in past tense becomes 'could' and 'went' changes to 'go'.
  * `SWREG` produces `I am going`
  * `SWREGD`: produces `I was going`
  * `SWRAOEGD`: produces `I would be going`
  * `SWRFG`: produces `I've gone`
  * `SWRFGD`: produces `I'd gone`
  * `SWREFG`: produces `I've been going`
  * `SWREFGD`: produces `I'd been going`

Example 2:
  *  `SWREUFB`: produces `I never am`
  *  `SWREUFBD`: produces `I never was`
  *  `SWROEUFBD`: produces `I should never be`

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
* `STKPWHR`: `` (empty -- third person singular form)
* `STWR`: `` (empty -- third person plural form)

Example usage of of `STWR` and `STKPWHR`:
* `SWR-RPGT/STWR-RPBT` produces 'I need to understand the'
* `KWHR-PL/STWR-FPBT` produces 'he may have known that'
* `SKWRAEUPB/STKPWHR-EUFGT` produces 'Jane never goes to'

 # Do, Can, Shall, Will
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

`EUF` controls how the words `just`, `still`, `never`, `even`, `be` and `have`.

* `E` is used for verb forms of `to be`.

* `F` is used for verb forms of `to have`.
  
* `EF` is used for verb forms of `have been`.

* `U` is used to suffix `just`, `UF` is used to prefix `just`.

The way these work is sometimes dependent upon whether a negative form ('*')
is used.

* `EU` gives the word `still` and is used as a suffix in positive form,
  but as a prefix for negative form

  * `...AEU...`: `... can still ...`
  * `...A*EU...`: `... still can't ...`

* `-EUF` appends the word `never` for positive forms, and `even` for negative
  forms.

  * `...AEUF...`: `... can never ...`
  * `...A*EUF...`: `... can't even ...`

Full table:

| `* E U F` | Modifier                           |
| --------- | ---------------------------------- |
| `? _ _ _` | <empty>                            |
| `? _ U _` | {} j**u**st                        |
| `? _ U F` | j**u**st {}                        |
| `_ E U _` | {} st**i**ll                       |
| `* E U _` | st**i**ll {}                       |
| `_ E U F` | {} n**ev**er                       |
| `* E U F` | {} **ev**en                        |
| `? E _ _` | 'be' + -ing verb form              |
| `? _ _ F` | 'have' + past participle verb form |
| `? E _ F` | 'have been' + -ing verb form       |

Examples:
* `SWRUPB` produces: `I just know`
* `SWREGT` produces:  `I'm going to`
* `SWRFGT` produces:  `I've gone to`
* `SWREFGT` produces: `I've been going to`
* `SWROEGTD` produces:  `I should be going to`
* `KWHRGT` produces: `he goes to`
* `KWHREGT` produces: `he's going to`
* `KWHRFGT` produces: `he's gone to`
* `KWHREFGT` produces: `he's been going to`

An exception is for `do`:

| `A O * E U F` | Result                         |
| ------------- | ------------------------------ |
| `_ _ _ _ _ _` | <empty>                        |
| `_ _ _ _ _ F` | have been + past verb form     |
| `_ _ * _ _ F` | have not been + past verb form |
| `_ _ _ _ U _` | j**u**st                       |
| `_ _ _ _ U F` | {}                             |
| `_ _ _ E _ _` | be + -ing verb form            |
| `_ _ * E _ _` | not be + -ing verb form        |
| `_ _ _ E _ F` | have been + -ing verb form     |
| `_ _ * E _ F` | have not been + -ing verb form |
| `_ _ _ E U _` | st**i**ll                      |
| `_ _ _ E U F` | n**ev**er                      |

This allows typing phrases such as:

* `SWREUG`: `I still go`
* `KPWREUFBSZ`: `you never said`
* `SWREGT`: `I'm going to`
* `SWRFGT`: `I've gone to`
* `SWREFGT`: `I've been going to`

Finally, the special prefix `STWRU` will give the infinitive form of the verb.
* `STWRUGT`: `to go to`
* `STWRULTS`: `to feel like`

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
| `LS`   | To feel (like)      |
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
| `RL`   | To recall           |
| `RPL`  | To remember (that)  |
| `R`    | To run              |
| `BS`   | To say (that)       |
| `S`    | To see              |
| `PLS`  | To seem (to)        |
| `RBT`  | To take             |
| `RLT`  | To tell             |
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
