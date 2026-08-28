# The Model · FinWise

> Module 6 · Pricing & Monetization. A pricing recommendation for FinWise leadership.

**To:** FinWise leadership · **From:** Product · **Re:** Is pricing the lever to pull?

---

## Recommendation in one line

**No — pricing is not the lever, and raising it now would make things worse.** FinWise is in **Stage 1, Value Creation**. The one pricing change worth making is structural rather than numerical: **re-time the reverse trial to start at activation instead of at sign-up**, and repackage around a value metric the customer already understands.

---

## Step 1 · Assess the monetization stage

**FinWise is in Stage 1 · Value Creation.** This is the uncomfortable answer, and the funnel supports it on two counts.

**Data point 1 — 2% of trial users convert to paid.** FinWise runs a *reverse* trial: users already have full functionality. When people who have been given everything still don't buy, the constraint cannot be access, packaging or price. It is that value never landed. [M4](../04-signals/data-signals.md) shows why: 72% of trials never import their own data, so the product never gets the chance to prove anything. A Stage 2 company has value landing and is working out how to capture more of it. FinWise isn't there yet.

**Data point 2 — 40% one-year retention on paid customers.** 60% of the people who *did* pay leave within a year. That's the same failure showing up after the sale: value isn't becoming habitual. M4 splits it cleanly — customers who ran three or more modelling outputs in month one retain at 62%, those who didn't at 24%. Retention is decided by usage depth, not by the price paid.

**Why this matters for the recommendation.** Stage 2 moves — price increases, expansion tiers, aggressive upsell — assume the value engine works and needs better capture. Applying them here would extract more from the 2% who already convert while doing nothing about the 98% who never saw the product work. It would raise ARPU on a shrinking base and read as growth for about two quarters.

---

## Step 2 · Select the model

**Keep the reverse trial. Change when it starts.**

The reverse trial is the right model for FinWise — the product's value is only legible once it runs on real data, so gating features would guarantee nobody ever sees it. The defect isn't the model, it's the clock.

> **Today the premium window starts at sign-up and expires on the calendar. Most trials therefore expire having never imported anything — FinWise spends its entire premium window on users who haven't started.**

**The change: the premium window begins at the first modelling output.** Sign up whenever you like; the 14 days of full access start the moment FinWise models your business. Users who never import never consume the window, and the downgrade moment lands when there's a forecast on screen worth keeping instead of an empty workspace worth abandoning.

### Why not the alternatives

- **Raise prices.** Stage 2 move on a Stage 1 problem. Extracts more from 2% and ignores 98%.
- **Discount to lift conversion.** Users who never saw the product work aren't declining on price. Discounting damages ARPU permanently and leaves the cause untouched.
- **Classic freemium.** Would require gating the import or the modelling output — the exact behaviours the whole strategy depends on. Fastest way to kill the growth loop.
- **Usage-based on transaction volume.** Punishes the customers with the most data, who are the ones the model most needs, and makes the bill unpredictable for a cash-anxious buyer.
- **Sales-assisted trials.** Would work, but converts a product problem into a permanent cost line and doesn't compound.

### Packaging

**Value metric: companies modelled + forecast horizon + collaborators.** It scales with value received, an SMB owner grasps it without explanation, and it grows naturally as the business does.

| | **Starter** — $49/mo | **Growth** — $149/mo | **Advisor** — $399/mo |
|---|---|---|---|
| Companies modelled | 1 | 1 | up to 10 |
| Forecast horizon | 13 weeks | 12 months + scenarios | 12 months + scenarios |
| Refresh | monthly | unlimited | unlimited |
| Users | 1 | 3 | unlimited |
| **Accountant seat** | **free** | **free** | — |
| Scenario modelling | — | ✓ | ✓ |
| Branded client reports | — | — | ✓ |

**The free accountant seat is strategy, not generosity.** Accountants and bookkeepers are FinWise's highest-leverage distribution channel — step 3→4 of the [M1 growth loop](../01-bet/growth-bet.md). One accountant carries the product to an entire client book at zero CAC, which is exactly the compounding motion that paid acquisition has failed to buy. Charging for that seat would monetise the loop and stop it.

**The Advisor tier exists because of them.** Once an accountant is inside multiple client accounts, multi-company access is a genuine need with obvious willingness to pay — and it's expansion revenue that arrives *because* the loop worked, not instead of it.

---

## Step 3 · The single most important pricing bet to validate next

> **That re-timing the reverse trial to start at first modelling output — rather than at sign-up — increases trial → paid conversion.**

**Why this one, ahead of every price-point question.** It's the only pricing change that acts directly on the 2%. Every other candidate (price level, tier boundaries, annual discount) optimises the conversion of users who already reached value; this one changes how many users reach the paywall having seen the product work at all. Price-point tests are worth running — after the funnel stops leaking 72% of its users.

**How I'd test it:** cohort-based, new trials only, 50/50, with trial→paid at 30 days as the primary metric and a minimum 60-day observation window. Existing users are grandfathered — changing terms on people who signed up under different ones is a trust cost that outlasts any pricing gain. Sequence it *after* [FW-IMP-001](../05-validation/experiment-brief.md); running an onboarding test and a trial-mechanics test at once makes both unreadable.

**The risk I'd want watched.** Activation-triggered windows can be gamed — a user could import, stall, and stretch a premium window indefinitely. Cap the window at 45 days from sign-up regardless, so the mechanism can't be farmed.

---

## Model signal — what success looks like in the data

**The signal we want: conversions cluster tightly at the end of the activation-triggered window.**

If conversions spike as the premium window closes for users who imported — and are sparse everywhere else — the paywall is sitting on a real value moment. If they're spread evenly across the lifecycle, the paywall isn't at a value moment; it's an obstacle people eventually give in to, and the packaging needs rethinking rather than re-testing.

| Metric | Target | Read at |
|---|---|---|
| Trial → paid conversion | 2% → **6–8%** | 90 days |
| Share of converters converting within 7 days of window close | > 60% | 90 days |
| One-year paid retention | 40% → **55%** | 12 months |
| Free accountant seats activated per paying customer | > 0.4 | 90 days |
| Share of new trials from share/invite | 8% → 20% | 180 days |
| **Guardrail:** import rate within 48h | **no decline** vs pre-launch | Continuous |

The last row matters most. If introducing any pricing change depresses the import rate, the paywall has leaked upstream into the activation gate, and it gets rolled back regardless of what the revenue line says.

---

## The honest risk

The whole recommendation rests on M4's correlational finding that reaching a first modelling output causes conversion, rather than merely coinciding with the kind of user who converts anyway. If [FW-IMP-001](../05-validation/experiment-brief.md) comes back flat, this memo's premise weakens considerably — and the right response would be to re-open whether FinWise's problem is activation at all, rather than to reach for the price list.
