# Lonely Runner — 13 Effective Speeds

**Jared Wilder**

Structural and exact finite work on the 13-speed Lonely Runner case, including a closed large-prime residue-class theorem and an independently replayed parity certificate.

## Large-prime residue-class theorem

For every prime

```text
p > 2366,
```

if a primitive positive integer 13-speed tuple satisfies

```text
u_i ≡ i (mod p),   1 ≤ i ≤ 13,
```

then there exists a real time `t` such that

```text
||t u_i|| ≥ 1/14   for every i.
```

Equivalently, no primitive 13-speed counterexample can lie in this canonical large-prime residue class.

The proof architecture is

```text
12-deletion / short-relation structure
    ↓
F_13 scalarization
    ↓
CRT scalar-canonical class modulo 13p
    ↓
8190 exact parity certificates
    ↓
2-adic scalar-canonical descent
```

See [`LARGE-PRIME-CANONICAL-CLOSURE.md`](LARGE-PRIME-CANONICAL-CLOSURE.md).

## Exact parity verification

[`verification/verify_parity_lemma.py`](verification/verify_parity_lemma.py) independently reconstructs the finite parity court from the theorem statement.

For every mask `e in {0,1}^13`, it exhausts

```text
x = n/(2d),   1 <= d <= 26,
```

with exact integer arithmetic and checks

```text
min_{1<=i<=13} ||i x + e_i/2|| >= 1/13.
```

The replay recovers exactly:

- **8190 / 8192** certified parity masks;
- uncertified mask `0`;
- uncertified mask `5461`, the pattern `e_i = i (mod 2)`.

GitHub Actions run `34856943727` passed. The script rechecks every reconstructed certificate individually and uses no floating-point comparisons.

## Structural program

The repository also develops:

- the deleted-runner trap from the 12-speed result;
- pair-overlap budgets and divisor witnesses;
- a degree-two Riesz obstruction forcing short coefficient-2 additive structure;
- a relation-entry dichotomy between additive structure and multiplicative clustering;
- the mod-13 scalar reduction;
- the scalar-canonical 2-adic descent.

A previously used stationary-reference implication was found to be false; arguments depending on it were removed while independently valid lemmas were retained.

## External literature

Jaan Allikvere’s September 2026 preprint *Fourteen lonely runners* (arXiv:2609.02604) reports a computer-assisted proof of the full 14-runner case using 111 prime gates. This repository preserves Wilder’s independent August program and its closed residue-class theorem.

## Repository map

- `program/` — focused 13-speed research package
- `program/master/` — master extraction
- `compact-record/` — earlier compact development
- `verification/` — independent finite replays