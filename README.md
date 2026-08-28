# FinWise, A Product-Led Growth Strategy

> **FinWise doesn't have a conversion problem — it has an import problem that presents as one. 72% of trials never let the product touch their books, so it never gets the chance to prove anything.**

**Leena Mohsen Almoradi** · Product Analytics & Experimentation Certification, 2026 cohort · August 2026

My final project: a complete growth and experimentation strategy for **FinWise Co.**, a B2B SaaS company selling financial-management software to small businesses. One folder per module; this README is **The Story** that ties them together.

---

## The seven required deliverables

| # | Required | Where it lives |
|---|---|---|
| 1 | **Growth Hypothesis & Bet** | [`01-bet/growth-bet.md`](01-bet/growth-bet.md) |
| 2 | **Metrics & Signal Diagnosis** | [`04-signals/data-signals.md`](04-signals/data-signals.md) |
| 3 | **Experimentation Plan** | [`05-validation/experiment-brief.md`](05-validation/experiment-brief.md) + [readout](05-validation/results-analysis.md) |
| 4 | **Onboarding Prototype** | [`02-solution/activation-solution.md`](02-solution/activation-solution.md) |
| 5 | **Gamification Mechanism** | [`03-mechanic/engagement-mechanic.md`](03-mechanic/engagement-mechanic.md) |
| 6 | **Pricing Recommendation** | [`06-model/pricing-model.md`](06-model/pricing-model.md) |
| 7 | **Individual Insights** | [The Story](#the-story), below |

### By module

| # | Module | Deliverable | Folder |
|---|---|---|---|
| 1 | **The Bet** (Ignite a PLG Motion) | growth hypothesis & bet + growth-loop viz | [`01-bet/`](01-bet/growth-bet.md) |
| 2 | **The Solution** (Acquisition & Activation) | 5-screen onboarding prototype + Aha definition | [`02-solution/`](02-solution/activation-solution.md) |
| 3 | **The Mechanic** (Retention & Engagement) | gamification mechanic + rationale & wireframe | [`03-mechanic/`](03-mechanic/engagement-mechanic.md) |
| 4 | **The Signals** (Data & Analytics) | Aim · Move · Prove + the data pattern | [`04-signals/`](04-signals/data-signals.md) |
| 5 | **The Validation** (Experimentation Methods) | experiment brief + reading another team's result | [`05-validation/`](05-validation/experiment-brief.md) |
| 6 | **The Model** (Pricing & Monetization) | pricing & packaging memo | [`06-model/`](06-model/pricing-model.md) |

---

## The scenario

FinWise Co. is a B2B SaaS company providing financial-management software to small businesses. It has reached PMF, runs a product-led motion with a reverse trial, and wants to grow hard over the next year.

| ARR | Trial → paid | 1-year paid retention | Growth engine |
|---|---|---|---|
| $10M | **2%** | **40%** (60% churn) | Paid acquisition — no longer driving meaningful growth |

## The strategy in one pass

**The finding (M4).** 2% conversion looks like a pricing or sales problem. It's neither. **72% of trials never import their own financial data**, so FinWise spends its entire premium window on users who never let it model anything. Of the trials that do reach a first modelling output, **8.3% convert against 0.2%** — a 40× gap on one behaviour. The same behaviour explains the retention problem: customers who ran three or more modelling outputs in month one retain at **62%** versus **24%**. And **71% of trials that ever import do so in the first session** — after day 3, only 5% ever do. The outcome is settled in minutes.

**The bet (M1).** So we bet on the import, not on acquisition — and explicitly stop buying more trials into a funnel that leaks 5,760 of 12,000 users at a single step. The growth loop compounds twice over: every import sharpens the model that produces the next user's first output, and every forecast shared with an accountant carries FinWise into a whole client book at zero CAC. That's the motion paid spend cannot buy, which is exactly why paid spend has plateaued.

**The solution (M2).** The trial's first session is rebuilt around the import: frame the user's own decision, make the import the headline ask, answer the trust objection where it's felt, pay out value mid-sync, and end on a 13-week cash view with one flagged risk. Sample data is demoted to last and honestly labelled — offering it early is the most tempting way to fake activation and destroy conversion.

**The mechanic (M3).** **Forecast Confidence** — a score that decays as data goes stale and recovers in one tap. Not a points streak, because losing points costs an SMB owner nothing; losing the reliability of a forecast they've started quoting costs them something real. The Monday trigger, the 20-second refresh, the variable "what changed" card, and a one-tap categorisation that improves the shared model.

**The validation (M5).** Nothing ships on a correlation. FW-IMP-001 is a 14-day user-level A/B test — import within 48h, 28% → 35%, ~690 per arm, five guardrails, sealed read date, decision rules written first. Part two: a result from **another team** landed at n=20 with 6.8% power. The call was *iterate* — a non-significant result there is evidence about the test, not the product.

**The model (M6).** FinWise is in **Stage 1, Value Creation**, not Stage 2 — the 2% conversion and 40% retention both say value isn't landing, and raising prices would extract more from the 2% while ignoring the 98%. The pricing bet worth making is structural: **re-time the reverse trial to start at the first modelling output rather than at sign-up**, so the premium window is spent on users who've actually started. Plus a free accountant seat, because the distribution channel should never be the thing you monetise.

---

## The Story

**Growth thesis:** FinWise grows when trial users import their own books — the import creates the modelling output, the output creates a weekly habit, and the habit is what converts and retains.

**One friction.** Reading the M5 result without flinching. It came back negative — B converted worse than A — and every instinct offered a way out. I could kill the idea, or I could go hunting for the segment where B won, which was right there: Organic showed a clean +25pp. Sitting with the fact that four users per cell makes that number noise, and that a −10pp difference resting on one person is equally noise, was harder than any of the design work. The pre-registered decision rules are what made it survivable. Writing them down beforehand isn't bureaucracy — it's the only thing standing between you and a story you'd prefer to tell.

**One Aha.** Halfway through M6 I realised I'd been about to recommend a price increase. FinWise has PMF, $10M ARR and a monetisation model already in place, so Stage 2 felt like the obvious read. Then I went back to the trial funnel and saw that a *reverse* trial converting at 2% can't be a capture problem — those users already had everything, for free, and still walked. The company looks like Stage 2 from the ARR line and is unmistakably Stage 1 from the funnel. That's when the modules stopped being six assignments and became one system: the pricing answer was sitting in the M4 data, and I'd nearly missed it by reading the balance sheet instead.

**Takeaways.**
- A headline metric usually names a *symptom*. "2% conversion" became actionable only once it was split by whether the user had ever imported anything.
- Correlation earns you a hypothesis, not a decision. The 40× gap justified running FW-IMP-001; it never justified shipping.
- Guardrails are where the real thinking shows. Naming a success metric is easy; naming the specific way your change could win its metric and still be a bad idea is the harder discipline.
- **Absence of evidence is not evidence of absence.** A non-significant result at n=20 says nothing about the product and everything about the test. Power analysis belongs before you run, not as an excuse afterwards.
- Effect size outranks p-value in a small sample. Session duration at p = 0.25 with d = 0.54 is worth another test; engagement at p = 0.83 with d = 0.10 is not.
- Strategy coheres or it doesn't. The most dangerous ideas in this project weren't the bad ones — they were the locally sensible ones that contradicted another module at the seam.

---

## Repo structure

```
ProductSchool-Analystic/
├── README.md                              ← this dashboard + The Story
├── 01-bet/growth-bet.md                   ← M1: hypothesis, bet, growth loop
│   └── assets/growth-loop.svg
├── 02-solution/activation-solution.md     ← M2: onboarding prototype + Aha
│   └── assets/onboarding-flow.svg
├── 03-mechanic/engagement-mechanic.md     ← M3: Forecast Confidence + wireframe
│   └── assets/forecast-confidence-wireframe.svg
├── 04-signals/data-signals.md             ← M4: Aim·Move·Prove + data pattern
│   └── assets/activation-funnel.svg
├── 05-validation/
│   ├── experiment-brief.md                ← M5 pt1: my experiment design
│   ├── results-analysis.md                ← M5 pt2: reading another team's result
│   ├── analysis.py                        ← reproduces every figure
│   ├── data/ab_test_experiment_data.csv    ← the A/B dataset
│   └── assets/experiment-results.svg
└── 06-model/pricing-model.md              ← M6: pricing & packaging memo
```

**Note on figures.** The scenario supplies FinWise's headline numbers (2% trial→paid, 40% retention, $10M ARR). The funnel breakdowns in M4 are illustrative figures constructed to be arithmetically consistent with those, and are labelled as such in the file.

---

_Certification submission — Product Analytics & Experimentation Certification, 2026 cohort._
