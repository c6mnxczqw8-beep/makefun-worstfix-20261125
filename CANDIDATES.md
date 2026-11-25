# Commit message candidates (draft pass)

One line each, at most 100 characters, scored on: really a
commit message about a fix that backfired, funniness, and how
sharply it captures the irony of a repair that broke more than
it mended.

1. Memory cure: "fix: cured the memory leak by deleting the
   memory itself" -- the cure is the catastrophe, stated flatly.
   Could gain a deadpan consequence clause if length allows.
2. Login: "fix: users can no longer log in, which has reduced
   login complaints to zero" -- strong irony, slightly long.
3. Typo: "fix: corrected the error message; the error is now the
   message" -- elegant loop, less catastrophic.
4. Speed: "perf: made the page load instantly by removing the
   page" -- classic shape, well worn.
5. Test suite: "fix: all tests pass now that there are no tests"
   -- beloved classic; too famous to feel fresh.

## Verdict

Winner: candidate 1, after a refinement pass. The flat draft
("deleting the memory itself") gained a deadpan consequence
clause -- "uptime is now measured in seconds" -- reported in
the same unbothered release-notes voice, which sharpens the
irony: the author noticed the catastrophe and logged it as a
metric. 86 characters, inside the 100 limit.
