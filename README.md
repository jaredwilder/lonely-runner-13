# Lonely Runner — 13 effective speeds

**Author:** Jared Wilder  
**Status:** focused finite/structural theorem program; **full LRC(13) remains open**.

This repository is the canonical public home for the estate's 13-effective-speed program. It consolidates the late-round theorem bank, terminal normal form, supplements, exact finite evidence, and the earlier compact record that had outgrown a cross-subject archive.

## Strongest closed subproblem

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

This is a closed residue-class subproblem, not the fourteen-runner theorem.

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

The repository separates exact finite statements and normal forms from any general Lonely Runner claim. Bounded computation remains bounded; conditional reductions remain conditional. Historical novelty / priority of the closed residue-class theorem is not asserted without a dedicated literature court.

## Source layout

Exact public source bytes are migrated under:

- `program/` — the focused `unpublished-math-papers/lonely-runner-13/` package;
- `program/master/` — the split 1,288-line master extraction;
- `compact-record/` — the earlier `combinatorial-records/lonely-runner/` material.

The archive copies remain public for provenance, but this repository is the preferred reading surface for the 13-speed work.
