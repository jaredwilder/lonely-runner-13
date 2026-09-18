# Lonely Runner with 13 effective speeds

This repository studies a structured 13-speed case of the Lonely Runner Conjecture. Its main completed result excludes an infinite large-prime residue class of potential counterexamples, with an exact finite parity calculation that can be replayed independently.

## Large-prime residue-class theorem

Let `p>2366` be prime, and let

\[
(u_1,\ldots,u_{13})
\]

be a primitive positive integer speed vector satisfying

\[
u_i\equiv i\pmod p\qquad(1\le i\le13).
\]

Then there exists a real time `t` such that

\[
\boxed{\|t u_i\|\ge \frac1{14}\quad\text{for every }i.}
\]

So no primitive 13-speed counterexample can lie in this canonical large-prime residue class.

The proof combines a short-relation reduction, a scalarization modulo `13p`, an exact parity classification, and a 2-adic descent. The complete writeup is [`LARGE-PRIME-CANONICAL-CLOSURE.md`](LARGE-PRIME-CANONICAL-CLOSURE.md).

## Exact parity classification

The finite step can be checked directly from its statement. For each mask

\[
e\in\{0,1\}^{13},
\]

the verifier searches rational points

\[
x=\frac{n}{2d},\qquad 1\le d\le26,
\]

and checks whether

\[
\min_{1\le i\le13}\left\|ix+\frac{e_i}{2}\right\|\ge\frac1{13}.
\]

The exhaustive result is:

- **8190 of 8192 masks certified**;
- the all-zero mask is exceptional;
- the alternating-parity mask `5461`, with `e_i\equiv i\pmod2`, is exceptional.

Run

```bash
python verification/verify_parity_lemma.py
```

The script reconstructs the certificates from the theorem statement, checks them using exact integer arithmetic, and then verifies every recovered certificate individually. No floating-point comparison is used.

## Structural ingredients

The surrounding argument develops several reusable pieces:

- the deleted-runner constraint inherited from the 12-speed theorem;
- pair-overlap bounds and divisor witnesses;
- a degree-two Riesz obstruction that forces short additive relations;
- a dichotomy between additive structure and multiplicative clustering;
- reduction to a scalar canonical class modulo 13;
- the final 2-adic descent.

A stationary-reference implication used in an earlier route was found to be false and removed; the theorem above does not depend on it.

## Related work

Jaan Allikvere's 2026 preprint *Fourteen lonely runners* gives a computer-assisted proof of the full fourteen-runner case using a different finite-checking framework. This repository preserves the independent large-prime theorem and its exact certificates as a separate structural result.

## Repository map

- `program/` — the full 13-speed mathematical development;
- `program/master/` — consolidated source extraction;
- `compact-record/` — earlier compact statements;
- `verification/` — independent finite replay.

Author: Jared Wilder.