---
title: Topics Authority — software craft
type: authority
status: active
date: 2026-06-23
last_updated: 2026-06-24
---

<!-- batch 6 (2026-06-23): registered concepts bug-tracking, real-time-chat, wikis, translation-infrastructure -->
<!-- batch 7 (2026-06-23): registered subject open-source-economics; concepts open-source-economics, corporate-open-source-participation, government-and-open-source, open-source-contracting -->
<!-- batch 8 (2026-06-23): registered concepts funding-non-programming-activities, open-source-marketing -->
<!-- batch 9 (2026-06-24): registered concepts innersourcing, evaluating-open-source-projects, hiring-open-source-developers, crowdfunding-and-bounties -->

# Topics Authority — software craft

Controlled-vocabulary source of truth for this vault — a lightweight thesaurus
(a preferred term plus its use-for variants). `/vault-lint` Check 8 resolves
every `topics:` value against **Subjects** and validates `aliases:` against
**Concepts**. Report-only.

> Seeded 2026-06-23 from the vault's first content — *Producing Open Source
> Software* (2nd ed.) plus the two open-access papers queued for ingest. ≤10
> subjects / ≤30 aliases per the first-ingest seed rule; grows from here under
> resolve-before-minting.

## Subject categories

Governs `topics:`. A value must be a preferred term below (or a reserved tag).
List variant spellings/synonyms that should resolve to a preferred term in its
Use-for column.

| Preferred | Use-for (variants that resolve to it) |
|---|---|
| version-control | vcs, source-control, revision-control |
| code-review | peer-review, code-reviews |
| continuous-integration | ci, ci-cd, continuous-delivery |
| project-infrastructure | technical-infrastructure, tooling, dev-infrastructure |
| software-collaboration | collaboration, distributed-development |
| open-source-governance | governance, project-governance |
| open-source-participation | participation, contributors, contribution, community |
| open-source-culture | free-software, open-source-philosophy, hacker-ethic, foss-culture |
| bug-tracking | issue-tracking, bug-tracker, defect-tracking |
| release-engineering | releasing, packaging, release-management |
| code-quality | quality, software-quality |
| open-source-licensing | licensing, software-licenses, license-compatibility, copyleft |
| open-source-economics | funding, open-source-business, commercialization, corporate-open-source, organizations-and-money |

## Concept aliases

Governs `aliases:` / page identity — each topic page is a preferred concept and
its frontmatter `aliases:` are its use-for variants. No alias may belong to two
pages or shadow another page's canonical title/slug.

| Preferred (page) | Use-for (aliases) |
|---|---|
| version-control | vcs, source-control, revision-control |
| code-review | peer-review, conspicuous-code-review |
| continuous-integration | ci, ci-cd |
| open-source-participation | contributor-base, who-contributes |
| free-software-vs-open-source | open-source-definition, free-vs-open-source |
| open-source-governance | governance-model, benevolent-dictator, consensus-democracy |
| forkability | right-to-fork |
| launching-an-open-source-project | project-presentation, hacktivation-energy, scaled-presentation, getting-started |
| open-source-licensing | choosing-a-license, applying-a-license, software-license |
| setting-the-tone | project-culture, setting-precedents, codes-of-conduct, in-group-behaviors |
| developing-in-the-open | open-from-day-one, develop-in-the-open, opening-a-closed-project, transparency-by-default |
| project-infrastructure | technical-infrastructure, collaboration-tools, what-a-project-needs |
| project-hosting | canned-hosting, project-hosting-site, code-hosting |
| message-forums | mailing-lists, discussion-forums |
| bug-tracking | issue-tracking, issue-tracker, ticket-tracker, defect-tracker |
| real-time-chat | project-chat, chat-rooms, irc |
| wikis | project-wiki, wiki |
| translation-infrastructure | i18n, l10n, internationalization, localization, translation-platform |
| open-source-economics | economics-of-open-source, paid-developers, money-and-influence |
| corporate-open-source-participation | corporate-involvement, being-a-good-corporate-citizen, appear-as-many-not-one, money-cant-buy-love |
| government-and-open-source | government-open-source, public-sector-open-source, open-source-in-government |
| open-source-contracting | contracting, contractors, osqa, open-source-quality-assurance |
| funding-non-programming-activities | non-code-funding, funding-non-programming-work, professional-testing |
| open-source-marketing | oss-marketing, freedom-from-vendor-lock-in, cost-of-total-ownership |
| innersourcing | innersource, inner-source |
| evaluating-open-source-projects | project-evaluation, evaluating-projects, project-health-signals |
| hiring-open-source-developers | hiring-for-influence, open-source-resume, portable-resume-test |
| crowdfunding-and-bounties | crowdfunding, bounties, bounty-funding |

## Reserved non-subject tags

Tags legal in the topics field but not subject categories: `stub`.
