---
title: Permissive (Non-Reciprocal) Licensing
aliases: [non-copyleft, non-reciprocal-license, permissive-license, mit-style-license, bsd-style-license]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-licensing]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Permissive (Non-Reciprocal) Licensing

A **permissive** (also *non-reciprocal* or *non-copyleft*) license "grants the freedoms under
discussion here but … does not have a clause requiring that they apply to distributed
derivative works as well"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=173), p. 160).
It is the opposite of [[copyleft]]: where copyleft makes freedom contagious, a permissive
license lets the code flow anywhere — including into closed-source products.

## The defining property: proprietary-compatible

The practical signature of a permissive license is that "the covered code [can] be used in
proprietary programs." Doing so "does not affect the licensing terms of the proprietary
program: it is still as proprietary as ever, it just happens to contain some code from a
non-proprietary source." The Apache, X Consortium, BSD-style, and MIT-style licenses are all
proprietary-compatible
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=174), p. 161).

Permissive licenses commonly still carry **attribution requirements** — a notice giving credit
to the authors must accompany use of the code — but this does not make the derivative itself
free; it "merely [requires] that credit be given for its free parts"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=174), p. 161).

## When to choose permissive

The decision criterion is the single licensing question from [[open-source-licensing]]: *are
you willing to let your code be used in proprietary programs?* If yes — or if you actively
want maximum adoption, including inside proprietary software (for example to displace a
proprietary competitor) — choose a permissive license.

The two early, well-known examples are **BSD** and **MIT**; the more recent **Apache License
2.0** is "also very popular — increasingly so — and somewhat better adapted to the legal
landscape of modern open source software development"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=173), p. 160).

## MIT as the default permissive choice

Fogel's recommended default non-copyleft license is **MIT**, for three reasons
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=176), p. 163):

- It is "extremely short," and "both widely used and widely recognized" — lowering the
  barrier to entry, since people need not re-read unfamiliar legalese (see
  [[open-source-licensing]] §*Choosing a license*).
- It is "fully compatible with all versions of the GNU General Public License," so MIT-licensed
  code can be mixed into a GPL work under any GPL version (see [[license-compatibility]]).

The **Apache License 2.0** is "nearly as compelling": it adds "explicit defenses against
misuse of software patents" (a *patent snapback* clause) that may matter to some organizations.
But its GPL-compatibility "is more complicated — by some interpretations, it is compatible with
GPL version 3 only." To spare downstream redistributors that complexity, Fogel still recommends
MIT "for anyone who doesn't have a reason to choose otherwise"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=176), p. 163).

## Negative Space

- **MIT-vs-BSD micro-differences** (`too-granular`): the two "differ only in uninteresting ways
  and are basically interchangeable"; the page does not enumerate the clause-level differences.
- **Full license texts** (`too-granular`): wording of MIT/BSD/Apache is not transcribed; the
  page captures what the *category* guarantees and when to pick it.
- **Patent-snapback clause mechanics** (`foreshadowing`): named here as Apache 2.0's
  distinguishing feature; the patent-defense machinery is treated with patents in Ch. 9b
  (batch 17) and summarised on [[open-source-licensing]] §*What licenses vary on*.

## See also

- [[copyleft]] — the reciprocal opposite; together these are the primary license-type split a
  project chooses between.
- [[open-source-licensing]] — the anchor: the one-question choice, terminology, and the full
  recommended-license list.
- [[license-compatibility]] — why MIT's full GPL-compatibility is an advantage and Apache's is
  qualified.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 9 "Legal Matters" —
  "Aspects of Licenses" (non-reciprocal/permissive definition, proprietary-compatibility,
  attribution requirements) and "Choosing a License" (MIT as the default non-copyleft license,
  the MIT-vs-Apache reasoning) (printed pp. 160–163).
