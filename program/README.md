# Lonely Runner — 13 effective speeds

**Author:** Jared Wilder  
**Research date:** 2026-08-07  
**Public extraction:** 2026-09-11

This directory contains a sustained research program on the 13-effective-speed Lonely Runner case. It had no root README when recovered, which made a substantial theorem bank discoverable only if a reader already knew the internal filenames. This page fixes that publication defect while the program awaits a dedicated repository.

## Research target

For 13 distinct nonzero integer speeds, the target is to find a time `t` at which every runner is at distance at least `1/14` from the origin modulo one.

The parent 13-speed case is not asserted solved here. The value of this program is the structural reduction it places on any hypothetical counterexample.

## Main public artifacts

- [`LRC13-LATE-ROUNDS-21-23-FINAL-THEOREM-BANK.md`](LRC13-LATE-ROUNDS-21-23-FINAL-THEOREM-BANK.md) — 14KB theorem-level record from the late rounds;
- [`LRC14-ROUND22-TERMINAL-NORMAL-FORM.md`](LRC14-ROUND22-TERMINAL-NORMAL-FORM.md) — terminal normal-form reduction;
- [`LRC14-THEOREM-BANK.json`](LRC14-THEOREM-BANK.json) — structured theorem bank;
- [`LRC14-FINAL-THEOREM-SUPPLEMENT.json`](LRC14-FINAL-THEOREM-SUPPLEMENT.json) — final structured supplement;
- `master/` — deeper provenance/research material.

Later statements supersede weaker constants from earlier passes when explicitly stated.

## Strong late-round structure

For a primitive hypothetical counterexample

`0 < u1 < ... < u13`, `gcd(u1,...,u13)=1`,

with maximum loneliness `lambda < 1/14`, the late theorem bank records a finite speed envelope

`C = 91^12 = 322475487413604782665681`

and consequently a rational slack

`1/14 - lambda >= 1/(28C)`.

### Seven adjacent-gap restrictions

The final bank constrains every adjacent ratio in the upper half:

- `u7/u6 < 12C`;
- `u8/u7 <= 48`;
- `u9/u8 <= 27`;
- `u10/u9 <= 20`;
- `u11/u10 <= 33/2`;
- `u12/u11 <= 72/5`;
- `u13/u12 < 13`.

In the additively independent bottom-six branch, the first bound sharpens to `u7/u6 < 9C`.

### Prime multiplicity and gcd hierarchy

For every prime `p`, if `h_p` is the number of speeds divisible by `p`, the bank proves

`p <= (13-h_p) ceil(p/7)`.

Among the consequences:

- no prime divides 12 or 13 speeds;
- multiplicity at least 11 forces `p=2`;
- multiplicity at least 10 or 9 forces `p in {2,3}`;
- multiplicity at least 8 forces `p in {2,3,5}`;
- every prime `p>=31` divides at most six speeds.

This feeds a corresponding majority-gcd hierarchy for large deletions/subsets of the speed tuple.

### Strict deletion theorem

If `lambda_j` denotes the maximum loneliness after deleting `u_j`, the known 12-speed result gives `lambda_j>=1/13` for every deletion. The campaign proves that equality cannot hold for all thirteen deletions:

> **There exists `j` with `lambda_j > 1/13`.**

The proof uses the threshold bad-set multiplicity: if every deletion were tight, the multiplicity function would have to equal two almost everywhere, contradicting the positive-measure interval near `t=0` on which all thirteen bad sets overlap.

The resulting deletion can be made quantitative using the finite speed bound and produces a robust interval on which the other twelve speeds are simultaneously beyond `1/13` while the deleted speed remains below `1/14`.

## Evidence and dependency discipline

The theorem bank explicitly separates internal deductions from external inputs, including the previously proved Lonely Runner cases through 12 effective speeds and finite/gcd-volume results used by the campaign.

Historical novelty is not inferred from the campaign. The retracted all-reference/change-of-stationary-runner branch is excluded from the late theorem layer.

## Repository promotion

This program has multiple theorem banks, structured data, a terminal normal form, explicit external dependencies, and a live frontier. It is therefore on the standalone-repository promotion queue rather than being treated as an ordinary archive folder.
