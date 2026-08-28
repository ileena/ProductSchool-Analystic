# The Validation · FinWise

> Module 5, part 1 · Experimentation Methods. A structured experiment brief for FinWise, with the method justified against the trade-offs.

**Experiment ID:** FW-IMP-001 · **Owner:** Product · **Status:** designed, ready to launch

*(Part 2 of this module — reading a result from another team and making a call — is in [`results-analysis.md`](results-analysis.md).)*

## What we're testing and why now

M4 established a correlation: trials that reach a first modelling output convert at 8.3% against 0.2% for those that don't. M2 proposed a redesigned first session built entirely around getting there. Neither establishes that the redesign *causes* the improvement — motivated users may simply do both. This experiment is what converts a correlational finding into a decision we're allowed to act on.

## Step 1 · Choose the method

**Two-arm, user-level randomised A/B test.** 50/50 allocation at trial start, fixed horizon, one pre-registered read.

| Arm | Experience |
|---|---|
| **A · Control** | Current trial onboarding: sign-up → feature tour → workspace, import available in settings |
| **B · Treatment** | Decision-first flow (M2): frame the decision → import as the headline ask → partial value during sync → first modelling output → share |

### Justification against the trade-offs

A standard A/B test is sufficient here, so it's what we run — no need to overcomplicate a question this clean.

- **User-level randomisation** works because each trial's onboarding is independent. There's no marketplace, no shared inventory, no interference between users, so the core assumption holds without contortion.
- **Not a switchback.** Switchbacks exist to handle time-varying interference. Nothing here is shared across users, so a switchback would cost complexity and buy nothing.
- **Not a geo holdout.** We can randomise the individual directly. Geo splits trade away statistical power for robustness against interference we don't have.
- **Not before/after.** Trial mix shifts week to week with campaign activity, so any observed change would be uninterpretable — we'd be measuring the marketing calendar.
- **Not a multi-armed bandit.** Bandits optimise allocation when you want to exploit a winner during the test. We want an unbiased causal estimate for a permanent build decision, and the traffic is cheap enough not to need adaptive allocation.
- **Fixed horizon, not sequential.** The metric reads within 48 hours of assignment and the required sample is modest, so a pre-registered read date is the simplest defence against peeking. The cost is losing the option to stop early on a win — acceptable over 14 days.

## Step 2 · Hypothesis and primary metric

> **If** we rebuild the trial's first session around the data import — framing it with the user's own decision, ranking the paths by speed, answering the trust objection in place, and paying out value before the sync completes —
> **then** the share of new trials that **import financial data within 48 hours** will rise from **28% to 35%**,
> **because** the import currently competes with a feature tour for attention and is framed as configuration rather than as the point of the trial.

**Primary metric:** % of new trials that import financial data within 48h of trial start.

One primary metric, chosen deliberately. It is the M1 bet stated numerically, it's the strongest known predictor of both conversion and retention (M4), and it reads within two days — early enough to act on, causally close enough to the change to be attributable.

### Metrics as instrumented

| Brief | Event / field | Type |
|---|---|---|
| Import within 48h | `data_import_succeeded` where `seconds_since_trial_start ≤ 172800` | Primary |
| Reached first modelling output | `modeling_output_viewed` where `is_sample_data = false` | Secondary |
| Speed to value | median `seconds_since_trial_start` on first output | Secondary |
| Habit formed | `forecast_refreshed` in trial week 1 | Secondary |
| Commercial outcome | trial → paid | Guardrail + follow-on |

## Step 3 · Sizing

| Parameter | Value |
|---|---|
| Baseline (p₁) | 28% |
| Target (p₂) | 35% |
| MDE | +7pp absolute (+25% relative) |
| Significance (α) | 0.05, two-sided |
| Power (1−β) | 80% |

```
n per arm = (Z(α/2) + Z(β))² × [p₁(1−p₁) + p₂(1−p₂)] / δ²
          = (1.96 + 0.84)² × [0.2016 + 0.2275] / 0.07²
          = 7.84 × 0.4291 / 0.0049
          ≈ 687 per arm  →  ~1,380 total
```

At ~400 trials/day, 1,380 users accrue in roughly 3.5 days. **The test still runs 14 days** — two complete weekly cycles, because B2B trial starts skew heavily to weekdays and a short window would weight one part of the week far more than another. It also lets the 48-hour metric close cleanly for every enrolled user and gives the secondary metrics a usable read.

## Step 4 · Guardrails

The change concentrates the trial on a single high-commitment ask, so the plausible harm is that users who would have pottered around and converted later now bounce at the import screen. Each guardrail catches a specific way this could be a bad idea that still looks like a good result.

| Guardrail | Threshold | The risk it catches |
|---|---|---|
| Trial abandonment within first session | must not rise more than **+3pp** vs control | We front-loaded the hardest ask and lost people at the door |
| Trial → paid conversion | must not fall **below control** at any point | We won the input metric and lost the outcome |
| Import failure rate (`data_import_failed` / started) | must not rise more than **+2pp** | We pushed volume into a connector that can't take it |
| Support tickets tagged `import` per 100 trials | must not rise more than **15%** | Throughput bought with confusion |
| Share of outputs on sample data | must not rise | We inflated the North Star with forecasts of nobody's business |

**Breach handling:** guardrails are monitored daily from day 3 under a pre-declared alerting rule. A confirmed breach stops the test immediately. That is the *only* permitted early look, it covers guardrails exclusively, and the primary metric stays sealed. Monitoring for harm is not peeking; monitoring for a win is.

## Step 5 · Read date

| Milestone | Date |
|---|---|
| Ramp to 50/50 | **Mon 7 September 2026** |
| Guardrail monitoring begins | Wed 9 September 2026 |
| **Read date — primary metric unsealed** | **Mon 21 September 2026** |
| Decision documented and circulated | Tue 22 September 2026 |

**No peeking.** The primary metric is not viewed before 21 September, and the test does not stop early for a positive result. Checking repeatedly until something crosses significance inflates the false-positive rate well above the nominal 5%; a fixed read date is what keeps α meaning what it claims to mean.

## Decision rules — written before the data exists

| Outcome | Decision |
|---|---|
| Primary significant positive, no guardrail breach | **Ship** to 100%, then proceed to the M6 pricing bet |
| Primary positive but not significant | **Iterate.** Do not ship. Sharpen the weakest screen (likely screen 2's trust copy) and re-run |
| Primary flat or negative | **Kill this execution.** The import thesis survives; the redesign didn't. Re-examine whether the barrier is willingness or capability — `data_import_failed` rates will say which |
| Any guardrail breached | **Roll back**, regardless of the primary result |

## Validity checks before reading anything

1. **Sample Ratio Mismatch** — assignment within 50% ± 1%. A meaningful deviation invalidates the test outright.
2. **Pre-period A/A** — three days of A/A before ramp, to confirm the pipeline shows no difference where none exists.
3. **Novelty effect** — minimal here since every user in the test is new to FinWise, but the day-by-day trend still gets checked for a decaying lift.
4. **Segment consistency** — the effect should hold in direction across traffic sources and across accounting-tool users versus CSV users. A reversal in a segment is a finding, not noise to average away.

## What this experiment cannot tell us

It measures a 48-hour import event over 14 days. It does **not** prove that the conversion and retention gaps from M4 are causal — that needs the treatment cohort held for a full trial-to-renewal cycle, which is a follow-on test (FW-IMP-002). Shipping on this result is a bet that the well-established link between activation and conversion holds for FinWise. It's a reasonable bet, and it is still a bet.
