# Strategy — Seventeen Syllables of Debugging

## The game

Judge-scored text, pairwise: a judge model compares two haiku at a time
on (1) 5-7-5 form, (2) a concrete central picture, (3) a turn in the
last line, (4) every word earning its place, (5) clean spoken rhythm.
Short + concrete wins; the playbook rule for judge-scored text is one
concrete image with a turn, not a paragraph.

## The entry (v1)

```
Cursor blinks at three
logs insist they saw nothing
the bug wore my name
```

72 characters, 3 lines, 5-7-5 syllables (verified in tests/).

## Why this recipe

- **Concrete centre (criterion 2):** a cursor blinking at 3am and a log
  line are the two most concrete debugging images in the brief itself —
  no vague statement about code anywhere.
- **Turn (criterion 3):** lines 1–2 set up an innocent machine (the logs
  saw nothing); line 3 reframes it — the bug is not in the machine, it
  wears *my* name. The fault moves from the system to the debugger.
- **Every word earns its place (criterion 4):** 13 words, no filler added
  to reach the count. "insist" does double work (logs as witnesses who
  lie by omission); "wore" turns the bug into something with a face.
- **Rhythm (criterion 5):** reads as plain speech, one breath, no
  syllable-exercise stiffness.
- **Originality:** our own image, not a copy of any entry already in —
  the field is judged pairwise, so a distinct voice matters more than
  matching a house style.

## Tried and dropped

- Longer, more "poetic" drafts (adjectives, metaphors about the night):
  they added words that earned nothing and diluted the picture.
- A joke punchline ("it was a missing semicolon"): concrete but a cliché
  every debugger has heard — loses on freshness (criterion 2).

## Expected outcome

A valid gate (1–200 chars, UTF-8) and a competitive dev rate against the
house anchors. Blind rounds mean no live score until round 1 closes
(12:15 WIB); iterate from the round-1 board, keeping whatever the judge
rewards and fixing only what it penalises.
