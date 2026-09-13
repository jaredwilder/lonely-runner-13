# LRC(13) / FOURTEEN-RUNNER WALL — MASTER SESSION ASSET EXTRACTION

**Campaign date:** 2026-08-07  
**Scope:** complete theorem/gold extraction for the entire multi-round campaign, including audits, retractions, negative gold, late-game breakthroughs, computational certificates, and final Court state.

## Read this first

This document is intentionally conservative about status. It preserves the campaign's strongest mathematics **and** its failed/retracted branches.

The full 14-total-runner / 13-effective-speed Lonely Runner case was **not** proved in the session.

The strongest late closed subproblem is the large-prime canonical \(k=13\) residue class for \(p>2366\), via repaired mod-13 polynomial reduction plus exact 2-adic descent.

---

# Fourteen-Runner Wall — Complete Session Asset Extraction

**Campaign:** 19 mathematical attack rounds + terminal extraction  
**Date:** 2026-08-07  
**Target:** 14 total runners / 13 normalized speeds at threshold \(1/14\)

## Status vocabulary

- **LIVE** — reference-safe argument retained in the final Court.
- **KNOWN INPUT** — external theorem or standard/known-style ingredient used as authority.
- **ABSTRACT GOLD** — mathematically useful standalone finite/combinatorial lemma, but its original application to the target was invalidated.
- **RETRACTED** — target-level claim depended on the false all-reference implication found in Round 14.
- **NEGATIVE GOLD** — route killed by an exact logical failure, counterexample, or insufficient implication.
- **OPEN OBLIGATION** — explicit statement still requiring proof.

---

# A. External authority actually used

## A1. Verified \(k\le12\) frontier — KNOWN INPUT

Sungkawichai & Trakulthongchai, **“Eleven, twelve, and thirteen lonely runners”**, arXiv:2604.23906 (2026-04-26).

Used as:
\[
\forall\text{ tuples of at most 12 distinct effective speeds},
\quad
\exists t:\|u_it\|\ge1/(k+1).
\]

For 12 speeds this gives \(1/13\).

## A2. Mixed-threshold / exact pair correlation — KNOWN INPUT / comparison

Alathea Jensen, **“Mixed thresholds in the Lonely Runner Conjecture”**, arXiv:2605.27941 (2026-05-27).

Relevant because it develops:
- mixed distance thresholds;
- Fourier series for threshold indicators;
- arithmetic-progression summation;
- exact two-function unequal-threshold integrals.

The session did **not** import a nonexistent higher-product theorem from it.

## A3. Tao 2017 — KNOWN BACKGROUND

Terence Tao, **“Some remarks on the lonely runner conjecture”**, arXiv:1701.02048.

Relevant background for finite verification and modular/divisibility methods. The elementary divisor witness used in this session was also reproved directly.

---

# B. Final LIVE theorem bank

## B1. Covering formulation

For
\[
B_i=\{t:\|u_it\|<1/14\},
\]
a counterexample is exactly
\[
\mathbb T=\bigcup_{i=1}^{13}B_i.
\]

Each \(\mu(B_i)=1/7\).

---

## B2. Deleted-Runner Trap (Round 1)

For
\[
W_j=\{t:\|u_it\|\ge1/13\ \forall i\ne j\},
\]
the verified \(k=12\) theorem gives \(W_j\ne\varnothing\).

A counterexample forces
\[
\boxed{W_j\subseteq\{t:\|u_jt\|<1/14\}.}
\]

### One-deletion closure criterion
If for one \(j\) there exists \(t\in W_j\) with
\[
\|u_jt\|\ge1/14,
\]
the 13-speed tuple is closed.

---

## B3. Pair-overlap budget (Round 1)

If
\[
N(t)=\sum_i\mathbf1_{B_i}(t),
\]
counterexample status gives \(N\ge1\), while
\[
\int N=13/7.
\]

Since \(\binom N2\ge N-1\),
\[
\boxed{
\sum_{i<j}\mu(B_i\cap B_j)\ge6/7.
}
\]

**Status:** LIVE but strategically demoted; generic pair overlap was not the strongest route.

---

## B4. Mandatory divisor witness (Rounds 2/14)

For every
\[
q=2,\dots,14,
\]
some normalized speed satisfies
\[
\boxed{q\mid u_i.}
\]

Direct proof uses \(t=1/q\).

---

## B5. Conditional maximum-anchor resonant probe theorem (Rounds 2–3)

Let maximum speed be
\[
M=qa
\]
and suppose \(M\) is the unique multiple of \(q\), \(3\le q\le14\).

Use probes
\[
t_{m,\sigma}=\frac mq+\frac{\sigma}{14M}.
\]

The anchor satisfies
\[
\|Mt_{m,\sigma}\|=1/14.
\]

For \(v<M,\ q\nmid v\), a bad probe requires
\[
mv\equiv\pm1\pmod q,
\]
and hence at most two probes can be killed by \(v\).

Moreover positive capacity requires
\[
\boxed{
v>\frac{14-q}{q}M
}
\]
and \((v,q)=1\).

### Consequences
- For \(q=13\), zero-slack saturation forces all 12 other residues mod 13 to be distinct if the unique-maximum branch existed.
- For \(q=14\), a unique maximal multiple of 14 is impossible.
- For \(q=3,\dots,7\), a unique maximal \(q\)-multiple is impossible because the required size threshold exceeds \(M\).

**Status:** LIVE as a conditional theorem at the one legitimate normalized reference.

---

## B6. Prime divisibility multiplicity bound (Rounds 14–16)

Let \(h_p\) be the number of speeds divisible by prime \(p\le13\).

Compress the \(p\)-multiples and use the verified small-\(k\) theorem to make them safe on a \(p\)-probe grid.

Every nonmultiple has grid capacity at most
\[
\lceil p/7\rceil.
\]

Therefore
\[
\boxed{
p\le(13-h_p)\lceil p/7\rceil.
}
\]

Consequences:
\[
\boxed{
h_2\le11,\;
h_3\le10,\;
h_5\le8,\;
h_7\le6,\;
h_{11}\le7,\;
h_{13}\le6.
}
\]

Combined with the mandatory divisor witness:
\[
\boxed{1\le h_{13}\le6.}
\]

---

## B7. Exact prime-probe law (Round 15)

For prime \(7<p\le13\), a nonmultiple \(v\) on the lifted \(p\)-grid has exact capacity
\[
\boxed{
N_{p,v}(\tau)
=
2-
\mathbf1_{\{\|v\tau\|\le(14-p)/14\}}.
}
\]

Special cases:

### \(p=13\)
One slot iff
\[
\|v\tau\|\le1/14,
\]
otherwise two.

### \(p=11\)
One slot iff
\[
\|v\tau\|\le3/14,
\]
otherwise two.

---

## B8. Eleven-resonance saturation (Round 15)

If
\[
h_{11}=7,
\]
the seven compressed multiples can be made \(1/8\)-safe, while the six outsiders must cover 11 probes.

Therefore at least five of the six outsiders satisfy
\[
\boxed{\|v\tau\|>3/14.}
\]

---

## B9. GCD-sensitive composite capacity (Round 15)

For modulus \(q\), outsider \(v\), put
\[
d=(v,q),\qquad Q=q/d.
\]

Then
\[
\boxed{
N_{q,v}(\tau)
\le
d\left\lceil Q/7\right\rceil
=
(v,q)\left\lceil\frac{q}{7(v,q)}\right\rceil.
}
\]

Hence any counterexample must satisfy the quantitative capacity requirement
\[
\boxed{
q
\le
\sum_{q\nmid v}
(v,q)
\left\lceil\frac{q}{7(v,q)}\right\rceil.
}
\]

This converts composite divisibility from a binary label into a gcd-sensitive capacity constraint.

---

## B10. Exact 13-slot law (Rounds 6, 14–19)

For outsider \(v\), phase \(\tau\), write
\[
v\tau=n+\beta,\quad0\le\beta<1,\qquad r=v\bmod13\ne0.
\]

At probes
\[
t_m=(m+\tau)/13,
\]
only
\[
rm+n\equiv0,-1\pmod{13}
\]
can be bad.

Thus
\[
\boxed{
|S_v(\tau)|
