# Lonely Runner with 13 effective speeds — closed large-prime canonical residue class

**Status:** **CLOSED SUBPROBLEM**.  
**Full LRC(13) / fourteen-runner problem:** **OPEN in this estate**.  
**Campaign date:** 2026-08-07.  
**Novelty / priority:** not asserted here; this page publishes the estate theorem and its authority boundary before a dedicated literature court.

## Theorem

Let `p>2366` be prime and let

\[
0<u_1<\cdots<u_{13}
\]

be a primitive integer speed tuple satisfying

\[
\gcd(u_1,\ldots,u_{13})=1
\]

and the canonical large-prime residue condition

\[
\boxed{u_i\equiv i\pmod p\qquad(1\le i\le13).}
\]

Then there exists a real time `t` such that

\[
\boxed{\|t u_i\|\ge\frac1{14}\qquad(1\le i\le13).}
\]

Therefore **no primitive LRC(13) counterexample belongs to this canonical residue class for any prime `p>2366`.**

The campaign identifies this as its strongest closed subproblem.

---

# Proof architecture

The proof has two genuinely different layers:

1. a repaired mod-13 / CRT reduction that forces any surviving canonical-class counterexample into a scalar-canonical congruence modulo `M=13p`;
2. an exact parity-certificate lemma plus infinite 2-adic descent that kills every sufficiently large scalar-canonical congruence.

The computational ingredient is finite and explicit; the descent after that is analytic/arithmetic.

---

# I. Repaired mod-13 reduction

Write

\[
v_i=u_i\pmod{13}\quad(1\le i\le12),
\qquad
c=u_{13}\pmod{13}.
\]

Use times

\[
t=\frac{s}{13}+\frac{R}{p}.
\]

Because `u_i≡i (mod p)`, the first twelve coordinates become

\[
\left\{\frac{s v_i}{13}+\frac{Ri}{p}\right\},
\]

while coordinate 13 is

\[
\left\{\frac{s c}{13}+\frac{13R}{p}\right\}.
\]

The source uses the published twelve-coordinate field proposition over `F_13` and its affine corollary to place non-scalar residue patterns in safe bins.

## The `c!=0` cases

If all `v_i` are nonzero, a coarse mod-13 point already gives all thirteen coordinates distance at least `1/13`.

For mixed or zero first-twelve patterns, perturb from a safe mod-13 point to a nearby `p`-grid point. The thirteenth coordinate loses less than

\[
\frac{13}{p}.
\]

Since

\[
\frac1{13}-\frac1{14}=\frac1{182},
\]

the inequality

\[
p>2366=13\cdot182
\]

preserves the required `1/14` margin. Hence `c!=0` cannot survive.

## The `c=0` cases

If all `v_i=0`, primitivity fails.

If the first twelve residues are mixed, or all nonzero but not proportional to `(1,...,12)`, the field/affine proposition again produces a safe coarse cell. Moving right by an amount

\[
\frac1{182}\le\varepsilon<\frac1{156}
\]

makes coordinate 13 safe while leaving the first twelve inside their safe cell. The available interval has width

\[
\frac1{156}-\frac1{182}=\frac1{1092},
\]

so the large-prime grid is fine enough.

Thus the only possible surviving pattern is

\[
\boxed{u_i\equiv\alpha i\pmod{13}\qquad(1\le i\le13)}
\]

for some nonzero `alpha in F_13`.

By CRT with the original congruence modulo `p`, there is a unit `b mod M`,

\[
M=13p,
\]

such that

\[
\boxed{u_i\equiv b i\pmod M\qquad(1\le i\le13).}
\]

This is the **scalar-canonical exceptional class**.

---

# II. Exact parity-certificate lemma

For a parity pattern

\[
e=(e_1,\ldots,e_{13})\in\{0,1\}^{13},
\]

define

\[
F_e(x)=\min_{1\le i\le13}
\left\|ix+\frac{e_i}{2}\right\|.
\]

The campaign's exact certificate suite exhausts all `2^13=8192` parity patterns.

For **8190 of the 8192 patterns**, it supplies an exact rational test point of the form

\[
x=\frac{n}{2d},\qquad1\le d\le26,
\]

for which

\[
\boxed{F_e(x)\ge\frac1{13}.}
\]

Exactly two patterns remain:

1. `e=(0,...,0)`;
2. `e_i ≡ i (mod 2)`, mask `5461`.

Those two patterns are exactly the two ways a scalar-canonical congruence modulo `M` can remain scalar-canonical modulo `2M`.

## Machine authority

The recovered final verification manifest records:

`verify_lrc14_parity_certificates.py — PASS`

and states that all **8190/8190** nonexceptional certificates were checked using integer arithmetic.

The complete companion CSV and verifier bytes remain a public-source mirroring target if they are not yet present under `program/master/`; the final manifest and theorem-bank authority are already recovered.

---

# III. Scalar-canonical 2-adic descent

The descent theorem is slightly more general than the large-prime result.

## Scalar-Canonical Descent Theorem

Let

\[
M\ge1183,
\qquad
\gcd(b,M)=1,
\qquad
u_i\equiv bi\pmod M,
\]

and suppose the full 13-tuple is primitive.

Then the tuple is **not** an LRC(13) counterexample.

### Proof

Write

\[
u_i=bi+Mn_i,
\qquad
e_i=n_i\pmod2.
\]

At an odd-numerator time

\[
t=\frac{a}{2M},
\]

we have

\[
\left\|u_it\right\|
=
\left\|i\frac{ba}{2M}+\frac{e_i}{2}\right\|.
\]

Multiplication by the odd unit `b` permutes the odd residue classes modulo `2M`, so accessible `ba/(2M)` values form a grid of spacing `1/M`.

If the parity pattern is one of the 8190 noncanonical patterns, choose a certified point `x_*` with all distances at least `1/13`, then an accessible odd-grid point `x` satisfying

\[
|x-x_*|\le\frac1{2M}.
\]

Every coordinate changes by at most

\[
13|x-x_*|\le\frac{13}{2M}.
\]

For

\[
M\ge1183=13\cdot91,
\]

\[
\frac{13}{2M}\le\frac1{182}
=
\frac1{13}-\frac1{14}.
\]

So all thirteen runners remain `1/14`-safe, contradiction.

Therefore any counterexample must have one of the two canonical parity patterns. These imply respectively

\[
u_i\equiv bi\pmod{2M}
\]

or

\[
u_i\equiv(b+M)i\pmod{2M}.
\]

Primitivity selects a unit scalar in the first odd-modulus lift; after the modulus becomes even the surviving scalar lifts are odd units. Hence

\[
\boxed{
\text{counterexample scalar-canonical mod }M
\Longrightarrow
\text{counterexample scalar-canonical mod }2M.
}
\]

Iterating,

\[
u_i\equiv b_r i\pmod{2^rM}
\]

for every `r>=0`. Consequently, for every pair `i,j`,

\[
2^rM\mid(ju_i-iu_j)
\]

for every `r`, forcing

\[
ju_i=iu_j.
\]

Thus

\[
\boxed{u_i=i u_1.}
\]

Finally take

\[
t=\frac1{14u_1}.
\]

Then

\[
\|u_it\|=\left\|\frac{i}{14}\right\|\ge\frac1{14}
\]

for every `1<=i<=13`, contradiction.

So no scalar-canonical tuple with `M>=1183` is a counterexample.

---

# IV. Finish of the large-prime theorem

Part I reduces any hypothetical canonical-class counterexample for prime `p>2366` to scalar-canonical form modulo

\[
M=13p>1183.
\]

Part III rules out that form.

Therefore the canonical large-prime residue class is closed.

---

# Boundary: what remains open

This theorem does **not** prove the full 13-effective-speed Lonely Runner Conjecture.

The remaining load-bearing obligation in the source program is the full `k=13` modular sieve: show that every candidate modular class is either eliminated directly or driven into a class already closed analytically.

The historical campaign explicitly rejects several shortcuts:

- experimental `raw_log_13` artifacts were not a proof;
- a generic `p=199` brute-force initial sieve did not finish;
- directly transplanting the prime-field polynomial argument to `Z_14` was invalid;
- the repaired route uses `F_13` on twelve coordinates plus a separate thirteenth-coordinate argument.

So the correct public status is:

> **large-prime canonical residue class: CLOSED for every prime `p>2366`; full LRC(13): OPEN.**

## Recovered authority sources

- `LRC13-CANONICAL-CLASS-CLOSURE.md`;
- `LRC13-FULL-SESSION-MASTER-ASSET-EXTRACTION.md`;
- `LRC13-FINAL-MASTER-THEOREM-BANK.json`;
- `LRC13-FINAL-VERIFICATION-MANIFEST.md`;
- exact parity certificate suite / verifier named above.
