# Lonely Runner — 13 effective speeds

**Author:** Jared Wilder  
**Estate program date:** 2026-08-07  
**Current status:** this repository preserves an independent finite/structural LRC(13) program and a closed large-prime residue-class theorem. A later external preprint now reports a full computer-assisted proof of the fourteen-runner case; that external package has **not yet been independently replayed in this repository**.

This repository is the canonical public home for the estate's 13-effective-speed program. It consolidates the late-round theorem bank, terminal normal form, supplements, exact finite evidence, and the earlier compact record that had outgrown a cross-subject archive.

## External status update — 2026-09-14

On **2026-09-02**, Jaan Allikvere submitted [`arXiv:2609.02604`, *Fourteen lonely runners*](https://arxiv.org/abs/2609.02604). The paper explicitly claims a proof of `LRC(13)`—the fourteen-runner case after one runner is made stationary—by closing **111 prime gates** in the finite-checking framework of Sungkawichai and Trakulthongchai.

The abstract reports

```text
sum_p log p > 681.5292
```

against the required

```text
log B_13 < 670.3498,
```

and describes per-gate certificates plus a separate audit of all 111 closed gates. The arXiv record links a verification package, certificates, and source code at DOI [`10.5281/zenodo.22066772`](https://doi.org/10.5281/zenodo.22066772).

**Authority boundary:** this is a very recent external computer-assisted proof claim. This repository's August statements that the full case was open are therefore historically stale as statements about the literature. We have **not yet replayed the external 111-gate package here**, so this repository does not independently certify that full proof yet.

Our own August results below remain independently meaningful subresults regardless of that later claim.

## Strongest estate closed subproblem

Read [`LARGE-PRIME-CANONICAL-CLOSURE.md`](LARGE-PRIME-CANONICAL-CLOSURE.md).

For every prime

```text
p > 2366,
```

if a primitive positive integer 13-speed tuple satisfies

```text
u_i ≡ i (mod p),   1 ≤ i ≤ 13,
```

then there exists a real time `t` with

```text
||t u_i|| ≥ 1/14   for every i.
```

Thus **no primitive LRC(13) counterexample lies in this canonical large-prime residue class**.

The proof architecture is:

```text
12-deletion / short-relation structure
    ↓
repaired F_13 scalarization
    ↓
CRT scalar-canonical class modulo 13p
    ↓
8190 exact parity certificates
    ↓
2-adic scalar-canonical descent.
```

This is an estate theorem about a residue class, not a claim to priority for the later full fourteen-runner result.

## Fresh independent parity verification — 2026-09-14

The historical source named a verifier/CSV pair for the load-bearing parity lemma, but those exact executable bytes were not present in this focused repository. Rather than relying on the historical PASS receipt, [`verification/verify_parity_lemma.py`](verification/verify_parity_lemma.py) reconstructs the finite court independently from the theorem statement.

For every mask `e in {0,1}^13`, it exhausts the advertised rational family

```text
x = n/(2d),   1 <= d <= 26,
```

using exact integer arithmetic and checks

```text
min_{1<=i<=13} ||i x + e_i/2|| >= 1/13.
```

GitHub Actions run `34856943727` passed. The fresh replay independently recovered exactly:

- **8190 / 8192** certified parity masks;
- uncertified mask `0`;
- uncertified mask `5461`, exactly the pattern `e_i = i (mod 2)`.

The script then hostile-replays every reconstructed certificate individually. No floating-point comparison and no historical certificate table is used.

This verifies the finite parity lemma. The analytic `F_13` reduction and 2-adic descent remain mathematical proof steps rather than outputs of this finite checker.

## Structural program

The deeper source program also preserves:

- the deleted-runner trap from the verified 12-speed result;
- the pair-overlap budget and mandatory divisor witnesses;
- a degree-two Riesz obstruction forcing every actual 13-speed counterexample to carry a short coefficient-2 additive relation;
- the relation-entry dichotomy between early additive structure and multiplicative clustering;
- the repaired mod-13 scalar reduction;
- the exact 8190-of-8192 parity-certificate lemma;
- the scalar-canonical 2-adic descent.

The source also preserves a major integrity correction: changing the stationary reference was once treated as preserving counterexample status; that implication is false, and target-level branches depending on it are retracted. Standalone lemmas survive only where independently justified.

## Scope

The repository separates exact finite statements and normal forms from global status claims. Bounded computation remains bounded; conditional reductions remain conditional. Historical novelty / priority of the estate's closed residue-class theorem is not asserted without a dedicated literature court.

## Source layout

Exact public source bytes are migrated under:

- `program/` — the focused `unpublished-math-papers/lonely-runner-13/` package;
- `program/master/` — the split 1,288-line master extraction;
- `compact-record/` — the earlier `combinatorial-records/lonely-runner/` material;
- `verification/` — fresh independent finite replays added during publication audit.

The archive copies remain public for provenance, but this repository is the preferred reading surface for the estate's 13-speed work.
