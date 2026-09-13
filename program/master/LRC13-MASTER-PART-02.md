The following cannot be used as target theorems from this session:

- Universal residue multiplicity for **every original runner** and every \(q\le14\).
- Global “original 14-speed set is 3-AP-free” theorem.
- Unique-13-farthest elimination obtained by changing reference.
- Global 14-point simultaneous congruence-partner skeleton.
- Mod-13 \((7,7)\) two-fiber reduction on the original 14 runners.
- Bilateral internal witness based on choosing bases in both fibers.
- Bilateral Hall matching as a target reduction.
- Seven near-opposite pairs as a target reduction.
- 57-state / 2793-state bilateral packet program.
- 49-base invariant lattice and centroid conservation as target constraints.
- Robust-or-critical bilateral witness-set theorem.
- Simultaneous compression of every mod-13 fiber using independently changed bases.

These may contain standalone algebraic/combinatorial facts, but their claimed implication from a one-runner counterexample was invalid.

---

# D. ABSTRACT GOLD SALVAGED FROM THE RETRACTED BRANCH

These are worth keeping as reusable mathematics, but **not as established LRC(13) reductions**.

## D1. Saturated-cover combinatorics

If seven subsets of a 13-set each have size at most two and cover all 13 elements:

- total incidence 13 forces exactly six pairs + one singleton and no overlaps;
- total incidence 14 forces seven pairs and exactly one doubled element.

This abstract lemma is later used validly in the reference-safe \(h_{13}=6\) branch.

## D2. Hall lemma for two near-partitions

For two 7-block covers of a 13-set where every block has size at most two and every \(k\)-block subfamily has union size at least \(2k-1\), the block-intersection bipartite graph satisfies Hall and has a perfect matching.

Mathematically useful; target application from Rounds 7–9 was retracted.

## D3. Cycle tilings for equal chord step

If all capacity-two blocks are edges of one \(C_{13}\), saturation forces alternating matching/near-perfect edge patterns.

Useful finite combinatorics; not by itself a target theorem.

## D4. Packet diameter observation

If fixed nonzero integer frequencies \(d_i\) satisfy
\[
\|d_i\tau\|<1/7
\]
throughout one open interval \(J\), then
\[
|J|\le2/(7\max|d_i|).
\]

Standalone true analytic fact.

---

# E. NEGATIVE GOLD — ROUTES KILLED

## E1. Generic pair-overlap alone is too diffuse
Round 1's
\[
\sum_{i<j}\mu(B_i\cap B_j)\ge6/7
\]
is true but did not yield the needed fixed-\(k\) rigidity.

## E2. Bare CRT/divisor coverage does not kill the mod-13 saturation branch
Residue transversals and mandatory divisors have ample Chinese-remainder freedom.

## E3. Static congruence-partner skeleton is insufficient
A concrete primitive 14-integer witness was produced in Round 6 satisfying the proposed static residue conditions while remaining 3-AP-free. It was never claimed to be an LRC counterexample; it killed the static-skeleton implication.

## E4. \(1/13\)-separation from a base does not prevent pair distance \(<1/7\)
Numerical gap:
\[
1/7-1/13=6/91.
\]

## E5. Signed Hall cancellation is false combinatorially
Odd-cycle incidence alone does not force mixed matching-error signs.

## E6. “57 packets = complete arithmetic state” was too aggressive
Even inside the later-retracted bilateral setup, marked bases had been quotiented away. Round 11 corrected this to at most 2793 marked packets.

## E7. 49-base coherence with unrelated witnesses is too weak
The witness phases can vary independently.

## E8. One Beatty/floor packet is not plausibly impossible
For irrational phases, quotient freedom gives substantial floor-residue flexibility. Single-packet impossibility was demoted.

## E9. First moments do not kill the \(h_{13}=6\) branch
Seven outsider singleton-condition sets of measure \(1/7\) can in principle avoid pair collisions on a positive-measure \(W\).

## E10. No universal favorable harmonic sign
Both the mixed \(1/13\)-\(1/14\) and equal \(1/14\)-\(1/14\) correlation corrections admit positive and negative arithmetic orientations.

## E11. No proved global handoff winding
Local forced handoffs are valid; a nonzero global displacement/winding invariant was not established.

## E12. Essentiality does not imply disjointness
The six internal bad sets are all essential, but that does not force union-bound equality.

---

# F. AUDIT CORRECTIONS BEYOND ROUND 14

## F1. Round 7 close-pair uniqueness
The claim that Pair Mode produced the only compressed pair with distance \(<1/7\) was too strong. What was unique was the doubled probe / designated overlapping pair. Round 8 corrected this.

## F2. Round 17 “seven essential chords”
Retain the valid statement:
- every outsider has a deleted-runner private physical probe in a saturated phase.

Do **not** infer without additional proof that every outsider must occur in two-slot mode on that phase or that every chord direction is globally realized as a transition.

---

# G. FINAL CONDITIONAL CLOSE

For \(1\le h\le6\), define the terminal saturation statement `TS(h)`:

There are no integers
\[
a_1,\dots,a_h,\quad
v_1,\dots,v_{13-h},
\]
with \(13\nmid v_j\), satisfying the inherited distinctness/primitivity constraints, such that for every
\[
\tau\in
W_h=\{\|a_i\tau\|\ge1/14\ \forall i\},
\]
the exact outsider slot sets
\[
S_{v_j}(\tau)
\]
cover all 13 residue probes.

Then:

\[
\boxed{
TS(1)\land TS(2)\land\cdots\land TS(6)
\Longrightarrow
LRC(13).
}
\]

Reason:
- mandatory divisor witness gives \(h_{13}\ge1\);
- multiplicity theorem gives \(h_{13}\le6\);
- a counterexample with that \(h\) would violate `TS(h)`.

The session has **not** proved all six `TS(h)`.

The sharpest accumulated branch is `TS(6)`:
- \(\mu(W_6)>1/7\);
- every phase of \(W_6\) is a saturated 13-cover state;
- generic transitions obey forced handoff;
- all six internal frequencies are essential;
- every outsider has a private physical probe at some deleted-runner witness;
- exact harmonic and gcd-sensitive probe formulas are available.

---

# H. MACHINE-TESTABLE ASSETS DELIVERED

Companion file:

`lrc14_terminal_checks.py`

It verifies:

1. exact 13-slot formula for all nonzero residues modulo 13 and representative phase regions;
2. inverse-residue chord displacement;
3. saturated incidence classification;
4. prime capacity/multiplicity arithmetic;
5. mixed \(13\times14\) harmonic sign table;
6. Bernoulli-formula consistency at the finite residue level.

Companion structured bank:

`LRC14-THEOREM-BANK.json`

contains machine-ingestible theorem statuses and dependencies.

---

# I. Best next machine attack

The strongest honest machine target is not “prove the whole open conjecture from prose.”

It is:

## Target TS6
Refute existence of an \(h_{13}=6\) tuple satisfying the universal saturated-cover condition on
\[
W=\{\tau:\|a_i\tau\|\ge1/14\ \forall i\}.
\]

A useful proof engine should combine:

- cell decomposition by all events
  \[
  a_i\tau\in\mathbb Z\pm1/14,\qquad
  v_j\tau\in\mathbb Z,\mathbb Z\pm1/14;
  \]
- exact 13-slot state constraints;
- forced generic handoffs;
- strict witness-measure lower bound;
- gcd-sensitive \(q=8,9,10,11,12,14\) capacities;
- exact equal-threshold pair correlations.

A certified impossibility proof for TS6 would be genuine new progress:
\[
h_{13}\le5.
\]

It would **not by itself** close LRC(13); TS5–TS1 would remain.

---

# J. Final campaign verdict

**Full LRC(13) closure:** not earned.  
**Reference-safe theorem estate:** substantial.  
**Largest invalid branch:** identified and retracted.  
**Strongest structural reduction:** \(1\le h_{13}\le6\) plus universal 13-probe saturation constraints indexed by \(h\).  
**Sharpest equality wall:** \(h_{13}=6\), with saturation on a set of measure strictly greater than \(1/7\).

This is the complete extraction without laundering conjectures or retracted implications into the theorem bank.


# K. LATE-GAME ADDENDUM — ROUNDS 20–CHAMPIONSHIP

This section extends the earlier extraction through the final championship round. Status tags:

- **LIVE-ANALYTIC** — proof argument retained in Court; not Lean-formalized unless separately stated.
- **LIVE-CERTIFIED** — finite/computational statement independently checked by a supplied verifier.
- **CONDITIONAL** — exact implication with an explicitly unproved hypothesis.
- **ABSTRACT GOLD** — true standalone lemma whose earlier target application may have been retracted.
- **OPEN** — explicit remaining frontier obligation.
- **NEGATIVE GOLD** — exact failure or killed route.

---

## K1. Periodic bad-set discrepancy lemma — LIVE-ANALYTIC

For \(B_s=\{t:\|st\|<1/14\}\) and every interval \(I\) of length \(L\),
\[
\boxed{|B_s\cap I|\le \frac L7+\frac{6}{49s}.}
\]
More generally, at threshold \(\lambda<1/2\), the bad-set density is \(2\lambda\) and the interval discrepancy is at most
\[
\boxed{\frac{2\lambda(1-2\lambda)}s.}
\]

## K2. Dominant Block Transfer Theorem — LIVE-ANALYTIC

For a target with \(k\) effective speeds at threshold \(1/(k+1)\), assume LRC is already known for the lower \(k-r\) speeds. Let the lower block be bounded by \(V\), the top \(r\) speeds be at least \(U\), and assume \(1\le r<(k+1)/2\). Then
\[
\boxed{\frac UV>\frac{(k-1)(k-r+1)}{k+1-2r}\Longrightarrow LRC(k).}
\]
For \(k=13\), every counterexample obeys the six-gap ladder
\[
\boxed{\frac{u_{13}}{u_{12}}<13,\quad
\frac{u_{12}}{u_{11}}\le\frac{72}{5},\quad
\frac{u_{11}}{u_{10}}\le\frac{33}{2},\quad
\frac{u_{10}}{u_9}\le20,\quad
\frac{u_9}{u_8}\le27,\quad
\frac{u_8}{u_7}\le48.}
\]
The \(r=1\) endpoint has a direct perturbative proof.  
**Machine receipt:** `lrc14_gap_constants_check.py`.

## K3. Finite-volume slack and seventh gap — LIVE-ANALYTIC

The later finite checking/gcd-volume bound gives
\[
\boxed{C=91^{12}=322475487413604782665681}
\]
for every coordinate of a primitive counterexample. Rationality of an extremal loneliness value yields
\[
\boxed{\frac1{14}-\lambda\ge\frac1{28C}.}
\]
This crosses the singular \(r=7\) wall and gives
\[
\boxed{\frac{u_7}{u_6}<12C=3869705848963257391988172.}
\]
In the 2-dissociated lower-six branch, the Riesz threshold \(\beta_6=1/6\) improves this to
\[
\boxed{\frac{u_7}{u_6}<9C=2902279386722443043991129.}
\]

## K4. All-prime multiplicity theorem — LIVE-ANALYTIC

For every prime \(p\), with \(h_p=\#\{i:p\mid u_i\}\),
\[
\boxed{p\le(13-h_p)\left\lceil\frac p7\right\rceil.}
\]
Hence:
- \(h_p\ge12\): impossible;
- \(h_p\ge11\): only \(p=2\);
- \(h_p\ge10\) or \(9\): only \(p\in\{2,3\}\);
- \(h_p\ge8\): only \(p\in\{2,3,5\}\);
- \(h_p\ge7\): only \(p\in\{2,3,5,11,17,23,29\}\);
- every prime \(p\ge31\) divides at most six speeds.

**Machine receipt:** `lrc14_round21_checks.py`.

## K5. Every 12-deletion is primitive — LIVE-ANALYTIC

No prime can divide any twelve speeds, so
\[
\boxed{\gcd(u_1,\dots,\widehat{u_j},\dots,u_{13})=1\qquad\forall j.}
\]

## K6. Strict Deletion Principle — LIVE-ANALYTIC
