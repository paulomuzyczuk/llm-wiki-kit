---
title: The Automation Ratio
aliases: [automation-ratio, automate-common-tasks, dont-make-humans-do-machine-work]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [project-infrastructure, continuous-integration]
roles: [tech-lead, code-craftsperson]
source_tier: 1
project: null
source_count: 1
status: active
---

# The Automation Ratio

The automation ratio is Fogel's rule of thumb for when a project should stop doing a task by
hand: "Try not to let humans do what machines could do instead. As a rule of thumb, automating
a common task is worth at least ten times the effort a developer would spend doing that task
manually one time. For very frequent or very complex tasks, that ratio could easily go up to
twenty or even higher"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=154), p. 141).

It is the operating principle behind the minimum toolset in [[project-infrastructure]] — and
the reason "beware over-automation" is a *limit* on a strong default, not an argument against
it.

## Why the math is invisible — and why that's the trap

The cost of *not* automating hides because "each individual performance of the task does not
feel like a huge burden, [so] no one ever gets annoyed enough to do anything about it." What
makes automation compelling is the multiplication: "the small burden is multiplied by the
number of times each developer incurs it, and then that number is multiplied by the number of
developers." Seeing this requires stepping back — "Thinking of yourself as a 'project manager',
rather than just another developer, may be a useful attitude here," because individual
developers are "too wrapped up in low-level work to see the big picture"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=154), p. 141).

Fogel uses "automation" broadly — "not only repeated actions… but any sort of technical
infrastructure that assists humans" (e.g. a docs site that recompiles XML to displayable form
on every commit). Beyond reclaimed time, automation "eliminates… the griping and frustration
that ensue when humans make missteps… in trying to perform complicated procedures manually":
"Multi-step, deterministic operations are exactly what computers were invented for; save your
humans for more interesting things"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=154), p. 141).

## Automated testing: the highest-value automation

Automated tests pay off "for any software project, but especially so for open source
projects, because automated testing (especially regression testing) allows developers to feel
comfortable changing code in areas they are unfamiliar with, and thus encourages exploratory
development." Since detecting breakage by hand means guessing where you might have broken
something, automated detection "saves the project a lot of time" and "makes people much more
relaxed about refactoring large swaths of code," improving long-term maintainability
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=154), p. 141).
The mechanics of running these tests on every change are covered under [[continuous-integration]].

### Regression vs. unit testing

Fogel pairs two test types by their temporal stance:

- **Regression testing** — "testing that working software stays working." Its purpose is to
  reduce the chance that changes "break the software, particularly in ways the software has
  been broken before." It is *retrospective*: "What has broken in the past?"
- **Unit testing** — "testing the software's module boundaries using their documented APIs,"
  both to guard against breakage and "to prove that the intended functionality exists as
  claimed." It is *prospective*: "What needs to continue working in the future?"

As a project grows, "the chances of unexpected side effects increase steadily"; good design
slows but cannot eliminate this, which is why many projects "encourage, and sometimes even
require, contributors to accompany new functionality with corresponding new… tests"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=155), p. 142).

## Automation must not become a barrier

Automated testing "is not a panacea." It "works best for programs with batch-style
interfaces"; GUI-driven software "is much harder to test programmatically." And test suites
"can often be quite complex, with a learning curve and maintenance burden all their own."
Hence the load-bearing caveat: "The easier it is to add new tests to the suite, the more
developers will do so, and the fewer bugs will survive to release"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=155), p. 142).

A mandatory-test policy can backfire: if a ten-minute fix needs two hours of test-writing,
"most developers will not bother with the test" — and if tests are *required*, "the developer
may not bother to fix the bug in the first place." The general rule applies to every process,
not just testing: "If the test system ever becomes a significant impediment to development,
something must be done, and quickly. The same would be true for any routine process that turns
into a barrier or a bottleneck for contributors"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=155), p. 142).

## Negative Space

- **Subversion's Contribulyzer / "Beautiful Teams" chapter** (`case-study-specifics`): a
  cited example of automating away a team bottleneck, not a generalizable concept.
- **"Don't break the build" social custom** (`subsumed-by` [[continuous-integration]]): the
  rule and its public-test-run corollary are captured in the CI enrichment, not duplicated.

## See also

- [[continuous-integration]] — running the automated tests on every change as part of the
  development cycle.
- [[project-infrastructure]] — the minimum standard automation the ratio justifies.
- [[code-review]] — the human-judgment work freed up when machines take the mechanical load.
- [[version-control]] — the commit stream automation (docs builds, test runs) reacts to.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 8 "Managing Participants" —
  §The Automation Ratio, §Automated testing, §Regression Testing and Unit Testing (printed
  pp. 141–142).
