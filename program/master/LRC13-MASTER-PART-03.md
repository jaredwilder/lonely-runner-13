Assume \(LRC(k-1)\). For any \(k\)-speed tuple \(V\),
\[
\boxed{\exists j:\operatorname{ML}(V\setminus\{v_j\})>1/k.}
\]
If all deletions were tight, the multiplicity function of the \(1/k\)-bad sets would be \(\ge2\) everywhere with mean exactly \(2\), contradicting the positive neighborhood of \(t=0\) where all \(k\) sets overlap.

For \(k=13\): every hypothetical counterexample contains a **primitive non-tight 12-speed deletion**.

## K7. Robust Private Deletion Interval — LIVE-ANALYTIC

For the strict deletion \(j\), there is an open interval \(I\) such that
\[
\boxed{\|u_jt\|<1/14,\qquad \|u_it\|>1/13\ (i\ne j)\qquad(t\in I).}
\]
With \(u_i\le C\), one may certify
\[
\boxed{|I|\ge1/(13C^2).}
\]

## K8. Arbitrary-Denominator Private Witness Theorem — LIVE-ANALYTIC

Let
\[
D_0=13C^2=1351875719774345695830656516373849784810797518893.
\]
There is one fixed index \(j\) such that for every integer \(d>D_0\) there exists \(a\in\mathbb Z\) with
\[
\boxed{\left\|\frac{au_j}{d}\right\|<1/14,\qquad
\left\|\frac{au_i}{d}\right\|>1/13\ (i\ne j).}
\]
Thus the private witness occurs on every sufficiently fine denominator grid, including all sufficiently large odd and prime denominators.

## K9. Quantitative singleton/private-witness mass — LIVE-ANALYTIC

Let \(N(t)=\#\{i:\|u_it\|\le1/13\}\). For a counterexample, \(N\ge1\) and \(\int N=2\). Near \(0\), \(N=13\) on a set of measure \(2/(13u_{13})\). Balancing positive and negative parts of \(N-2\) yields
\[
\boxed{\mu\{t:N(t)=1\}\ge\frac{22}{13u_{13}}.}
\]
At a singleton time the unique \(1/13\)-bad runner must be \(1/14\)-bad. Hence some fixed \(j\) has private mass
\[
\boxed{\ge\frac{22}{169u_{13}}.}
\]

## K10. Strict Loneliness Flag — LIVE-ANALYTIC

Every 13-speed tuple admits a nested chain
\[
V_{13}\supset V_{12}\supset\cdots\supset V_2
\]
with
\[
\boxed{|V_m|=m,\qquad \operatorname{ML}(V_m)>1/(m+1)\quad(2\le m\le12).}
\]
Inside a bounded counterexample:
\[
\boxed{\operatorname{ML}(V_m)\ge1/(m+1)+1/(2C(m+1)).}
\]

## K11. Exact subset-gcd budget — LIVE-ANALYTIC / EXTERNAL INPUT

\[
\boxed{G(\mathbf u)=\sum_{S\subseteq[13]}\gcd(u_i:i\in S)\le91^{12}.}
\]
If \(h_d=\#\{i:d\mid u_i\}\), then
\[
\boxed{G(\mathbf u)=\sum_{d\ge1}\varphi(d)(2^{h_d}-1).}
\]
Consequently, if \(q\) divides at least \(h\) speeds,
\[
\boxed{(2^h-1)q\le91^{12}.}
\]

## K12. All-modulus probe capacity theorem — LIVE-ANALYTIC

For every integer modulus \(q>1\), if \(q\) divides some selected speeds and \(v\) is an outsider, put \(d=\gcd(v,q)\). Then
\[
\boxed{N_{q,v}\le d\left\lceil\frac{q}{7d}\right\rceil.}
\]
Therefore every counterexample satisfies
\[
\boxed{q\le\sum_{q\nmid v}\gcd(v,q)\left\lceil\frac{q}{7\gcd(v,q)}\right\rceil.}
\]

## K13. GCD support amplification — LIVE-ANALYTIC

If an \(h\)-subset, \(h\ge7\), has gcd \(q\), and outsiders have \(d_j=\gcd(q,v_j)\), then
\[
\boxed{\sum_jd_j\ge\frac{h-6}{6}q.}
\]
Thus some outsider has
\[
\boxed{d_j\ge\frac{h-6}{6(13-h)}q.}
\]

## K14. Certified recursive majority-GCD collapse — LIVE-CERTIFIED

The finite divisor-multiset verifier certifies
\[
\boxed{\begin{array}{c|cccccc}
|S|&12&11&10&9&8&7\\\hline
\gcd(S)\le&1&2&4&9&36&288
\end{array}}
\]
for every hypothetical counterexample.

Top relaxation witness multisets:
\[
\begin{array}{c|c}
11&2;(1,1)\\
10&4;(1,1,2)\\
9&9;(1,1,1,3)\\
8&36;(1,1,4,4,9)\\
7&288;(1,1,1,1,8,36).
\end{array}
\]
These certify sharpness of the relaxation only.  
**Machine receipt:** `lrc14_final_doctrine_checks.py`.

Complete ladder:
\[
\begin{array}{c|c}
13&1\\12&1\\11&2\\10&4\\9&9\\8&36\\7&288\\
6&5118658530374679089931\\
5&10402435077858218795667\\
4&21498365827573652177712\\
3&46067926773372111809383\\
2&107491829137868260888560\\
1&322475487413604782665681.
\end{array}
\]

## K15. Maximal \(h_7=6\) transition-cover theorem — LIVE-ANALYTIC

If exactly six speeds are divisible by \(7\), write them \(7a_i\). For every outsider \(v\), transition-grid coverage yields
\[
\boxed{v\le\sum_{i=1}^6\gcd(a_i,v)\left\lceil\frac{v/\gcd(a_i,v)}7\right\rceil.}
\]
Hence
\[
\boxed{\sum_i\gcd(a_i,v)\ge v/7,\qquad \max_i\gcd(a_i,v)\ge v/42.}
\]
Therefore for some anchor
\[
\boxed{v\le6(7a_i),}
\]
and globally
\[
\boxed{\max(\text{outsiders})\le6\max(\text{7-divisible speeds}).}
\]

## K16. Degree-two Riesz obstruction — LIVE-ANALYTIC

For a 2-dissociated \(n\)-set,
\[
\boxed{\operatorname{ML}(V)\ge\frac1{2\pi}\arccos\left(1-\sqrt{\frac3{2n}}\right).}
\]
At \(n=13\), the lower bound is
\[
0.135210985878358\ldots>1/14.
\]
Hence every counterexample has a nonzero short relation
\[
\boxed{\sum_{i=1}^{13}\varepsilon_i u_i=0,\qquad \varepsilon_i\in\{-2,-1,0,1,2\}.}
\]

## K17. Additive-or-Cluster Transfer — LIVE-ANALYTIC / CERTIFIED CONSTANTS

Let
\[
\beta_m=\frac1{2\pi}\arccos\left(1-\sqrt{\frac3{2m}}\right).
\]
If the bottom \(13-r\) speeds are 2-dissociated, then either a short relation already exists or the next gap obeys
\[
\frac{u_{14-r}}{u_{13-r}}\le
D_r:=\frac{3r}{7(7-r)(\beta_{13-r}-1/14)}.
\]
For \(r=1,\dots,6\),
\[
\boxed{D_r\approx
1.070915862956,
2.450725892331,
4.366476981201,
7.345810490509,
12.967231482019,
29.110552146588.}
\]
**Machine receipt:** `lrc14_round23_checks.py`.

## K18. Relation-entry normal form — LIVE-ANALYTIC

There is a least prefix where a coefficient-2 relation appears. Every earlier prefix is 2-dissociated, so before the first relation the speeds are forced into the Riesz clustering regime:
\[
\boxed{\text{short additive relation early, or sharp multiplicative clustering first.}}
\]

## K19. Repaired mod-13 polynomial reduction — LIVE-ANALYTIC

For a large-prime canonical class
\[
u_i\equiv i\pmod p,
\]
the published 12-coordinate field proposition over \(\mathbb F_{13}\) eliminates all mod-13 patterns except
\[
\boxed{u_i\equiv\alpha i\pmod{13}.}
\]
CRT gives a scalar-canonical exceptional congruence
\[
\boxed{u_i\equiv bi\pmod{M},\qquad M=13p.}
\]

## K20. Affine \(\mathbb F_{13}\) corollary — LIVE-ANALYTIC

If \(v\in(\mathbb F_{13}^{\times})^{12}\) is not proportional to \((1,\dots,12)\), then there exist \(s\ne0\), \(m\) with
\[
\boxed{sv+m(1,\dots,12)\in\{1,\dots,11\}^{12}.}
\]

## K21. Exact parity certificate lemma — LIVE-CERTIFIED

For
\[
F_e(x)=\min_{1\le i\le13}\left\|ix+\frac{e_i}{2}\right\|,
\qquad e\in\{0,1\}^{13},
\]
exact rational certificates prove \(F_e(x)\ge1/13\) for **8190 of 8192** parity patterns.

Only:
1. \(e=(0,\dots,0)\);
2. \(e_i\equiv i\pmod2\), mask \(5461\),
remain. They are exactly the two scalar-canonical lifts mod \(2M\).

**Machine receipt:** `verify_lrc14_parity_certificates.py` passes all 8190 certificates using integer arithmetic.

## K22. Scalar-Canonical 2-Adic Descent Theorem — LIVE-ANALYTIC + CERTIFIED FINITE LEMMA

If
\[
M\ge1183,\quad \gcd(b,M)=1,\quad u_i\equiv bi\pmod M,
\]
then the tuple cannot be an LRC(13) counterexample.

A noncanonical parity lift is killed by K21 plus the perturbation loss
\[
13/(2M)\le1/182=1/13-1/14.
\]
Thus a counterexample would remain scalar-canonical mod \(2M,4M,8M,\dots\). Hence
\[
2^rM\mid(ju_i-iu_j)\quad\forall r,
\]
forcing \(ju_i=iu_j\). Therefore \(u_i=i u_1\), and \(t=1/(14u_1)\) closes the tuple.

## K23. Large-Prime Canonical Class Closure — CLOSED SUBPROBLEM

For prime \(p>2366\), if
\[
\gcd(u_1,\dots,u_{13})=1,
\qquad
u_i\equiv i\pmod p,
\]
then
\[
\boxed{\exists t:\|tu_i\|\ge1/14\quad\forall i.}
\]

This closes the large-prime canonical residue class at effective \(k=13\), despite composite \(k+1=14\), using:
1. repaired mod-13 polynomial reduction;
2. scalar-canonical CRT exceptional class;
3. exact 8190-pattern parity certificate;
4. infinite 2-adic descent.

**Boundary:** it does not prove arbitrary LRC(13). The remaining bottleneck is the full initial/evolving \(k=13\) modular sieve.

---

# L. LATE NEGATIVE GOLD / FAILED CLOSES

## L1. “Secret raw_log_13 already closes k=13” — KILLED
Experimental repository artifacts did not constitute a published/certified \(k=13\) proof.

## L2. Generic \(p=199\) initial-sieve brute force — INCOMPLETE
Exact search was computationally expensive and did not complete as a full \(k=13\) certificate in-session. This confirmed the initial sieve as a genuine bottleneck.

## L3. Direct polynomial method over \(\mathbb Z_{14}\) — BLOCKED
The published field proof requires prime \(k+1\); directly replacing it by the composite ring was unjustified. The successful repair uses \(\mathbb F_{13}\) on twelve coordinates plus a separate thirteenth-coordinate argument.

## L4. Primitive Non-Tight Extension Lemma — OPEN
The campaign did not prove that every primitive non-tight 12-speed tuple satisfying the gcd collapse is unextendable.

## L5. Full k=13 modular sieve — OPEN
The canonical class is closed, but a complete theorem showing every candidate modular class is eliminated or reaches a closed class was not obtained.

---

# M. FINAL COURT STATE

## Full conjecture
\[
\boxed{\text{LRC(13) / 14 total runners: NOT CLOSED IN THIS SESSION.}}
\]

## Strongest closed subproblem
\[
\boxed{\text{Large-prime canonical }k=13\text{ residue class: CLOSED for }p>2366.}
\]

## Universal survivor normal form
Any hypothetical counterexample must simultaneously satisfy:

1. covering by thirteen \(1/14\)-bad sets;
2. every 12-deletion primitive;
3. at least one deletion strictly non-tight;
4. one robust private interval of length at least \(1/(13C^2)\);
5. private witnesses on every sufficiently fine denominator grid;
6. quantitatively positive singleton/private-witness mass;
7. coordinate bound \(u_i\le C=91^{12}\);
8. all-modulus gcd-sensitive capacity inequalities;
9. majority gcd collapse \(1,2,4,9,36,288\);
10. all-prime multiplicity restrictions;
11. \(1\le h_{13}\le6\) and universal 13-resonance constraints;
12. seven dominant-gap restrictions;
