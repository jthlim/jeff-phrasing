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
* `KWHRGT` produces `he goes to`
* `KWHRUGT` produces `does he go to`
* `SWRGTD` produces `I went to`
* `KWHRGTD` produces `he went to`
* `SWRAFGTD` produces `I could have gone to`
* `KWHRO*UFGTD` produces `he just shouldn't go to`
* `KWHRO*EGTD` produces `he shouldn't be going to`
* `SWRAOEUFGTD` produces `I would never go to`
* `SWREFGT` produces `I have been going to`
* `SWR-RPBT` produces `I understand the`
* `SWRA*EURPBT` produces `I still can't understand the`
* `SWR*UFBGTSDZ/TWRAOEPBLGTD` produces `I just didn't expect that we would be finding that`

Many decisions on the word choices were taken from statistical data and
Google Books N-gram Viewer.

This dictionary also supports full reverse lookup, so you can see how to
stroke phrases in Plover's suggestions window.

# Warning
This is currently a work in progress. Expect changes in future versions.

# System

The phrase is constructed in multiple parts:

1. A starter (`I`, `you`, `he`, `she`, `it`, `we`, `they`)
2. An optional `do`/`can`/`shall`/`will`
3. An optional `not`
4. A optional modifier `just`/`still`/`never`/`even`/`have`/`be`
5. A verb e.g. `go`, `say`, `understand`, etc.
6. An optional suffix word
7. A tense

The phrase will generally be constructed in a manner that feels grammatically
correct.

Example 1: For the stroke `SWRO*FGTD`:

1. `SWR` is the starter: `I`
2. `O` is `shall`
3. `*` is `not`
4. `F` is `have`
5. `G` is `go`
6. `T` is `to`
7. `D` is for past tense

Once the verb forms, tenses and short forms are matched up, this results in:
`I shouldn't have gone to`

Example 1:
  * `SWR-G` produces `I go`
  * `SWRUG` produces `do I go`
  * `SWR-GD` produces `I went`
  * `SWRAGD` produces `I could go`
  * `SWRAUGD` produces `could I go`
  * `SWREG` produces `I am going`
  * `SWREGD` produces `I was going`
  * `SWRAOEGD` produces `I would be going`
  * `SWRFG` produces `I have gone`
  * `SWRFGD` produces `I had gone`
  * `SWREFG` produces `I have been going`
  * `SWREFGD` produces `I had been going`

Example 2: See how the verb 'be' changes:
  * `SWREUFB` produces `I never am`
  * `SWREUFBD` produces `I never was`
  * `SWROEUFB` produces `I shall never be`
  * `SWROEUFBD` produces `I should never be`

## Starters

Starters are formed using keys on the left hand side of the board:
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

`EUF` controls word ordering and how the words `just`, `still`, `never`,
`even`, `be` and `have` combine into the sentence.

* `E` is used for verb forms of `to be`.

* `F` is used for verb forms of `to have`.

* `EF` is used for verb forms of `have been`.

* `U` is used to swap the order of starter and middle words:
  * `SWROGTD`: `I should go to`
  * `SWROUGT`: `should I go to`

* `EU` gives the word `still` and is used as a suffix in positive form,
  but as a prefix for negative form

  * `...AEU...`: `... can still ...`
  * `...A*EU...`: `... still can't ...`

* `UF` gives the word `just` and is used as a suffix in positive form,
  but as a prefix for negative form

  * `...AUF...`: `... can just ...`
  * `...A*UF...`: `... just can't ...`

* `-EUF` appends the word `never` for positive forms, and `even` for negative
  forms.

  * `...AEUF...`: `... can never ...`
  * `...A*EUF...`: `... can't even ...`

Full table:

| `* E U F` | Modifier                             | `SWRAGD`                  |
| --------- | ------------------------------------ | ------------------------- |
| `? _ _ _` | <empty>                              | `I could go`              |
| `? E _ _` | 'be' + -ing verb form                | `I could be going`        |
| `? _ _ F` | 'have' + past participle verb form   | `I could have gone`       |
| `? E _ F` | 'have been' + -ing verb form         | `I could have been going` |
| `? _ U _` | <swap starter and do/can/shall/will> | `could I go`              |
| `_ _ U F` | `{}` j**u**st                        | `I could just go`         |
| `* _ U F` | j**u**st `{}`                        | `I just couldn't go`      |
| `_ E U _` | `{}` st**i**ll                       | `I could still go`        |
| `* E U _` | st**i**ll `{}`                       | `I still couldn't go`     |
| `_ E U F` | `{}` n**ev**er                       | `I could never go`        |
| `* E U F` | `{}` **ev**en                        | `I couldn't even go`      |

Note: The `{}` in the table represents `do`/`can`/`shall`/`will`

An exception is for `do`:

| `A O * E U F` | Result                         | `SWR-G`:               |
| ------------- | ------------------------------ | ---------------------- |
| `_ _ _ _ _ _` | <empty>                        | `I go`                 |
| `_ _ _ _ U _` | <swap word order>              | `do I go`              |
| `_ _ _ _ U F` | `{}`                           | `I do go`              |
| `_ _ _ _ _ F` | have + past verb form          | `I have gone`          |
| `_ _ * _ _ F` | have not  + past verb form     | `I haven't gone`       |
| `_ _ _ E _ _` | be + -ing verb form            | `I am going`           |
| `_ _ * E _ _` | not be + -ing verb form        | `I am not going`       |
| `_ _ _ E _ F` | have been + -ing verb form     | `I have been going`    |
| `_ _ * E _ F` | have not been + -ing verb form | `I haven't been going` |
| `_ _ _ E U _` | st**i**ll                      | `I still go`           |
| `_ _ _ E U F` | n**ev**er                      | `I never go`           |

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
| `BLG`  | To call             |
| `BG`   | To come (to)        |
| `RP`   | To do (it)          |
| `BGS`  | To expect (that)    |
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
| `PBL`  | To mean             |
| `PLZ`  | To move             |
| `RPG`  | To need (to)        |
| `RLS`  | To realize (that)   |
| `RL`   | To recall           |
| `RPL`  | To remember (that)  |
| `R`    | To run              |
| `BS`   | To say (that)       |
| `S`    | To see              |
| `PLS`  | To seem (to)        |
| `RBZ`  | To show             |
| `RBT`  | To take             |
| `RLT`  | To tell             |
| `PBG`  | To think (that)     |
| `RT`   | To try (to)         |
| `RPB`  | To understand (the) |
| `Z`    | To use              |
| `P`    | To want (to)        |
| `RBG`  | To work             |

Examples:
*  `SWRB` produces `I am`
*  `KPWRB` produces `you are`
*  `SWRAB` produces `I can be`

Memorization hint: `live`, `give` and `move` use `LZ`, `GZ` and `MZ`.

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
