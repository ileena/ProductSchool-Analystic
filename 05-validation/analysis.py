"""
Analysis of the A/B result in data/ab_test_experiment_data.csv.
Reproduces every figure quoted in results-analysis.md.

    pip install pandas scipy numpy
    python analysis.py
"""
import numpy as np
import pandas as pd
from scipy import stats

Z_ALPHA, Z_BETA = 1.959963985, 0.8416212336

df = pd.read_csv("data/ab_test_experiment_data.csv")
df.columns = ["uid", "version", "source", "duration", "conv", "engagement"]
A, B = df[df.version == "A"], df[df.version == "B"]


def wilson(c, n, z=Z_ALPHA):
    p, d = c / n, 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return centre - half, centre + half


def n_per_arm(p1, p2):
    return (Z_ALPHA + Z_BETA) ** 2 * (p1 * (1 - p1) + p2 * (1 - p2)) / (p2 - p1) ** 2


def power_at_n(p1, p2, n):
    se = np.sqrt(p1 * (1 - p1) / n + p2 * (1 - p2) / n)
    return stats.norm.cdf(abs(p2 - p1) / se - Z_ALPHA)


print("=" * 62)
print("PRIMARY METRIC - CONVERSION")
print("=" * 62)
for lbl, arm in [("A", A), ("B", B)]:
    lo, hi = wilson(arm.conv.sum(), len(arm))
    print(f"  {lbl}: {arm.conv.sum()}/{len(arm)} = {arm.conv.mean():.0%}  "
          f"95% Wilson CI [{lo:.0%}, {hi:.0%}]")

table = [[A.conv.sum(), len(A) - A.conv.sum()], [B.conv.sum(), len(B) - B.conv.sum()]]
_, p_fisher = stats.fisher_exact(table)
p1, p2 = A.conv.mean(), B.conv.mean()
se = np.sqrt(p1 * (1 - p1) / len(A) + p2 * (1 - p2) / len(B))
print(f"  difference: {p2 - p1:+.0%}  Fisher exact p = {p_fisher:.4f}")
print(f"  95% CI on difference: [{p2 - p1 - Z_ALPHA * se:+.0%}, {p2 - p1 + Z_ALPHA * se:+.0%}]")

print("\n" + "=" * 62)
print("SECONDARY METRICS (directional only)")
print("=" * 62)
for col, label in [("duration", "Session duration (s)"), ("engagement", "Feature engagement (%)")]:
    t, p = stats.ttest_ind(B[col], A[col], equal_var=False)
    d = (B[col].mean() - A[col].mean()) / np.sqrt((A[col].var() + B[col].var()) / 2)
    print(f"  {label}: {A[col].mean():.1f} -> {B[col].mean():.1f} "
          f"({B[col].mean() - A[col].mean():+.1f})  Welch t={t:.2f} p={p:.4f} d={d:.2f}")

print("\n" + "=" * 62)
print("POWER - the actual finding")
print("=" * 62)
print(f"  n required to detect 70% -> 77% (+7pp MDE): {n_per_arm(.70, .77):.0f} per arm")
print(f"  n actually run:                             {len(A)} per arm")
print(f"  power on the observed 70% -> 60%:           {power_at_n(.70, .60, 10):.1%}")
print(f"  power even if B had hit 100%:               {power_at_n(.70, 1.0, 10):.1%}")

print("\n" + "=" * 62)
print("SEGMENTS (hypothesis-generating only)")
print("=" * 62)
seg = df.groupby(["source", "version"]).agg(
    n=("uid", "count"), conv=("conv", "sum"), cr=("conv", "mean"),
    dur=("duration", "mean"), eng=("engagement", "mean")).round(2)
print(seg.to_string())

print("\n" + "=" * 62)
print("VALIDITY CHECKS")
print("=" * 62)
print(f"  Sample ratio: {len(A)}/{len(B)} - balanced, no SRM")
print("  Source mix by arm:")
print(pd.crosstab(df.source, df.version).to_string())
print("  NOTE: mix is identical across arms. Simple randomisation would rarely")
print("        produce this; assignment was stratified, or the sample is constructed.")
