# Lonely Runner — 13 effective speeds — late-round theorem bank

**Campaign:** 2026-08-07  
**Target:** for 13 distinct nonzero integer speeds, find `t` with all distances at least `1/14`  
**Court:** **NOT CLOSED**

This file releases the theorem-level mathematics from Rounds 21–23 and the final doctrine close state. It supersedes the earlier session bank where later statements strengthen older constants or convert qualitative restrictions into exact finite normal forms. The retracted all-reference/change-of-stationary-runner branch is not used.

External inputs used by these deductions include the proved Lonely Runner cases through 12 effective speeds and finite/gcd-volume results cited in the campaign. Historical novelty of the session deductions has not been independently certified.

## 1. Uniform finite slack below `1/14`

For a hypothetical primitive 13-speed counterexample, write

`0<u1<...<u13`, `gcd(u1,...,u13)=1`,

and

`lambda = max_t min_i ||u_i t|| < 1/14`.

The campaign first used the Giri–Kravitz quantitative finite-volume bound to obtain a finite speed bound and hence rational slack. Later, the Malikiosis–Santos–Schymura gcd-volume bound sharpened the finite envelope to

`C = 91^12 = 322475487413604782665681`,

so every speed of a counterexample satisfies `u_i <= C`. Since a maximizing point below `1/2` occurs at an intersection of two active linear pieces, `lambda=a/q` with `q<=2C`; therefore

`1/14 - lambda >= 1/(28C)`.

## 2. Seventh adjacent-gap theorem

Round 21 crossed the singular seven-dominant-runner wall. Combining a variable-threshold dominant-block transfer with the finite slack gives a universal adjacent-gap restriction. In the final `C=91^12` normalization, every counterexample satisfies

`u7/u6 < 12 C`.

Together with the previously banked dominant-block ladder, every counterexample has seven consecutive upper-gap restrictions:

- `u7/u6 < 12C`;
- `u8/u7 <= 48`;
- `u9/u8 <= 27`;
- `u10/u9 <= 20`;
- `u11/u10 <= 33/2`;
- `u12/u11 <= 72/5`;
- `u13/u12 < 13`.

Round 23 sharpens the seventh gap **in the additively independent bottom-six branch**: if the six smallest speeds are 2-dissociated, then

`u7/u6 < 9C`.

## 3. All-prime multiplicity theorem

For every prime `p`, let

`h_p = #{i : p | u_i}`.

Every counterexample satisfies

`p <= (13-h_p) ceil(p/7)`.

Equivalently,

`h_p <= 13 - ceil(p / ceil(p/7))`.

Consequences:

- no prime divides 12 or 13 speeds;
- if `h_p>=11`, then `p=2`;
- if `h_p>=10` or `h_p>=9`, then `p in {2,3}`;
- if `h_p>=8`, then `p in {2,3,5}`;
- if `h_p>=7`, then `p in {2,3,5,11,17,23,29}`;
- every prime `p>=31` divides at most six speeds.

## 4. Majority-gcd hierarchy

The prime multiplicity theorem implies immediately:

- every 12-speed deletion is primitive;
- the radical of the gcd of any 11 speeds divides `2`;
- the radical of the gcd of any 10 or 9 speeds divides `6`;
- the radical of the gcd of any 8 speeds divides `30`;
- the radical of the gcd of any 7 speeds divides `2*3*5*11*17*23*29`.

Round 22 strengthens this to prime powers:

- gcd of any 12 speeds is `1`;
- gcd of any 11 speeds divides `2`;
- gcd of any 10 speeds divides `24`;
- gcd of any 9 speeds divides `2^a 3^2` for some `a>=0`;
- gcd of any 8 speeds divides `2^a 3^b 5`;
- gcd of any 7 speeds divides `2^a 3^b 5^2*11*17*23*29`.

## 5. Strict Deletion Theorem

For a 13-speed tuple let

`lambda_j = ML(V \ {u_j})`.

The proved 12-speed case gives `lambda_j >= 1/13` for all `j`. The campaign proves that they cannot all be tight:

`exists j : lambda_j > 1/13`.

Proof core: if all deletions were tight, the threshold bad-set multiplicity

`N(t)=sum_i 1_{||u_i t||<=1/13}`

would have to satisfy `N(t)>=2` everywhere, while its integral is exactly `2`. Hence `N=2` almost everywhere, impossible because near `t=0` all 13 bad sets overlap on a positive-measure interval.

Thus every counterexample contains a **primitive non-tight 12-speed deletion**.

## 6. Robust private deletion interval

For the index `j` from the Strict Deletion Theorem there is a nonempty open interval `I` such that throughout `I`

- `||u_i t|| > 1/13` for every `i != j`;
- `||u_j t|| < 1/14`.

Using the finite bound `u_i<=C`, the strict deletion maximum satisfies

`lambda_j >= 1/13 + 1/(26C)`,

and one may take a certified interval with

`|I| >= 1/(13 C^2)`.

## 7. General Strict Deletion Principle

Round 23 proves the preceding argument for all `k>=3`:

> If `LRC(k-1)` is true, then every `k`-speed tuple has a deletion whose maximum loneliness is **strictly greater than** `1/k`.

Since LRC is known through effective size 12 in the campaign's authority state, every 13-speed tuple contains a nested flag

`V13 ⊃ V12 ⊃ ... ⊃ V2`, `|Vm|=m`,

with

`ML(Vm) > 1/(m+1)`

for every `2<=m<=12`.

For a counterexample under the same finite envelope, each strict member obeys the quantitative separation

`ML(Vm) >= 1/(m+1) + 1/(2C(m+1))`.

## 8. Exact gcd budget and divisor-support identity

Every primitive counterexample satisfies the finite gcd-volume budget

`G(u) = sum_{S subset [13]} gcd(u_i : i in S) <= 91^12`,

with the empty-set term zero.

Writing

`h_d = #{i : d | u_i}`,

the campaign derives the exact divisor-support identity

`G(u) = sum_{d>=1} phi(d) (2^{h_d}-1)`.

Hence

`sum_{d>=1} phi(d)(2^{h_d}-1) <= 91^12`.

## 9. Prime-power probe inequality

If `p^e` divides at least `s` speeds and `H_p` is the number divisible by `p`, every counterexample satisfies

`p^e <= (H_p-s) p^{e-1} ceil(p/7) + (13-H_p) ceil(p^e/7)`.

This is the engine behind the prime-power gcd restrictions above.

## 10. The `h_7=6` transition-cover theorem

Suppose exactly six speeds are divisible by 7, written `7a_1,...,7a_6`, and let `v` be any of the seven outsiders. The exact seven-probe transition argument gives

`v <= sum_{i=1}^6 gcd(a_i,v) ceil((v/gcd(a_i,v))/7)`.

Consequently

`sum_i gcd(a_i,v) >= v/7`,

so some `i` satisfies

`gcd(a_i,v) >= v/42`.

Since `7` does not divide `v`, this implies

`v <= 6*(7a_i)`

for some divisible speed. In particular the largest outsider is at most six times the largest 7-divisible speed.

## 11. Exact degree-two Riesz obstruction

Call a set `V` 2-dissociated if

`sum_{v in V} epsilon_v v = 0`, `epsilon_v in {-2,-1,0,1,2}`

forces all coefficients zero.

Using

`P(x) = (2/3)(1-cos(2pi x))^2`,

whose Fourier support lies in `{-2,-1,0,1,2}`, the campaign proves that every 2-dissociated `n`-set satisfies

`ML(V) >= (1/(2pi)) arccos(1 - sqrt(3/(2n)))`.

For `n=13`, the right side is approximately

`0.135210985878358 > 1/14`.

Therefore every hypothetical 13-speed counterexample has a nonzero additive relation

`sum epsilon_i u_i = 0`, `epsilon_i in {-2,-1,0,1,2}`.

## 12. Additive-or-cluster transfer

For `r=1,...,6`, if the bottom `13-r` speeds are 2-dissociated, the dominant-block transfer with the Riesz threshold gives

`u_{14-r}/u_{13-r} <= D_r`,

where

`D_r = 3r / [7(7-r)(beta_{13-r}-1/14)]`

and

`beta_m=(1/(2pi)) arccos(1-sqrt(3/(2m)))`.

The campaign records the numerical bounds

- `r=1`: `D≈1.070915862955858`;
- `r=2`: `D≈2.450725892330589`;
- `r=3`: `D≈4.366476981200525`;
- `r=4`: `D≈7.345810490509302`;
- `r=5`: `D≈12.967231482019137`;
- `r=6`: `D≈29.110552146587931`.

Thus every counterexample must either acquire a short coefficient-2 relation in a lower prefix or become sharply multiplicatively clustered before that relation appears.

## 13. Relation-entry normal form

Because 2-dissociation is hereditary, let `m0` be the least prefix size at which a coefficient-2 relation appears. Round 22 guarantees `m0<=13`. Every smaller prefix is 2-dissociated, so every upper adjacent gap encountered before the first relation obeys the corresponding Riesz cluster bound.

This is the campaign's **relation-entry normal form**: a counterexample cannot remain simultaneously low-coefficient-additively independent and strongly lacunary.

## 14. Quantitative private-witness mass

For the threshold `1/13` bad sets, let

`N(t)=sum_i 1_{||u_i t||<=1/13}`.

In a `1/14` counterexample, `N(t)>=1` everywhere and `∫N=2`. On the interval `||t||<1/(13u13)`, all thirteen indicators equal one. Balancing the positive and negative parts of `N-2` gives

`mu{t : N(t)=1} >= 22/(13 u13)`.

At a singleton time, the unique threshold-bad runner must actually satisfy `<1/14`. Therefore some index `j` has private-witness set of measure at least

`22/(169 u13)`.

## 15. Arbitrary-denominator private-witness theorem

With the same strict deletion index `j`, the certified private interval has length at least `1/(13C^2)`. Therefore for **every** integer

`d > 13 C^2`

there is an integer `a` such that

`||a u_j/d|| < 1/14`

while

`||a u_i/d|| > 1/13` for every `i != j`.

Thus one fixed deleted runner has a private witness on every sufficiently fine denominator grid, not just on a selected prime family.

## 16. All-modulus probe-capacity theorem

Let `q>1` divide `h<=12` selected speeds. For an outsider speed `v`, put

`d=gcd(v,q)`, `Q=q/d`.

On the `q` lifted probes, that outsider can hit at most

`N_{q,v} <= d ceil(Q/7) = gcd(v,q) ceil(q/(7 gcd(v,q)))`.

Hence every counterexample satisfies the exact necessary condition

`q <= sum_{q not| v} gcd(v,q) ceil(q/(7 gcd(v,q)))`

for **every integer modulus `q`**, not merely primes.

## 17. GCD support amplification

Let a subset of `h>=7` speeds have gcd `q`, and let the `13-h` outsider gcds be `d_j=gcd(q,v_j)`. The all-modulus capacity law yields

`sum_j d_j >= ((h-6)/6) q`.

Thus some outsider satisfies

`d_j >= ((h-6)/(6(13-h))) q`.

A large gcd supported on a strict majority of the speeds must therefore propagate substantially toward at least one additional speed.

## 18. Certified recursive majority-gcd collapse

Combining support amplification with exact finite enumeration of allowable divisor multisets gives the campaign's strongest majority ladder:

| subset size | gcd of every such subset is at most |
|---:|---:|
| 13 | 1 |
| 12 | 1 |
| 11 | 2 |
| 10 | 4 |
| 9 | 9 |
| 8 | 36 |
| 7 | 288 |

The finite relaxation attains its envelope with divisor-multiset witnesses such as `q=288` and outsider gcds `(1,1,1,1,8,36)` at `h=7`. These witness sharpness of the **necessary-condition relaxation**, not existence of Lonely Runner counterexamples.

Combining the exact gcd budget with divisor support extends the finite ladder to smaller subsets, but the new structural collapse is the majority sequence

`1, 2, 4, 9, 36, 288`.

## 19. Exact 13-probe law

If `h` speeds are multiples of 13 and the rest are outsiders, use lifted probes

`t_m=(m+tau)/13`, `m in F_13`.

For an outsider `v`, writing `r=v mod 13 !=0` and `v tau=n+beta`, its bad-probe set has exactly

`|S_v(tau)| = 2 - 1_{||v tau||<=1/14}`

(up to the strict-boundary convention), with the two possible residues explicitly

`{-r^{-1}n, -r^{-1}(n+1)} mod 13`.

This gives immediately

`1 <= h_13 <= 6`.

## 20. Universal 13-resonance saturation law

For the `h` compressed internal speeds define

`W_h={tau : ||a_i tau||>=1/14 for all i}`.

For every `tau in W_h`, the outsiders must cover all 13 lifted probes. If

`Z_h(tau)=#{j : ||v_j tau||<=1/14}`,

then

`Z_h(tau) <= 13-2h`.

For the extremal branch `h=6`, every point of `W_6` has only two possible cover states:

1. six two-slot outsiders plus one one-slot outsider partition the 13 probes exactly; or
2. all seven outsiders have two slots, with exactly one doubled probe and every other probe covered once.

No other saturation state is compatible with a counterexample.

## 21. Strict witness-measure refinement in the `h_13=6` branch

If `M=max_i |a_i|` for the six compressed multiples, then

`mu(W_6) >= 1/7 + 5/(7M) > 1/7`.

More generally

`mu(W_h) >= (7-h)/7 + (h-1)/(7M)`.

Thus the saturated finite-state cover must persist on a set **strictly larger** than the naive union-bound measure.

## 22. Generic handoff law

Inside the interior of `W_6`, away from simultaneous events, the outsider slot sets are locally constant except when one outsider crosses `||v_j tau||=1/14`. At a generic transition exactly one slot is created or destroyed. Saturation forces the disappearing slot to be the unique doubled probe immediately before a loss, and a newly created slot to become the unique doubled probe immediately after a gain. For residue `r_j=v_j mod13`, its two slots differ by `-r_j^{-1} mod13`.

This is a local finite-state transition law; no global winding invariant was proved.

## 23. Exact two-function harmonic identities

For `f_delta(x)=1_{||x||<delta}` the Fourier coefficients are

`fhat_delta(0)=2delta`, `fhat_delta(n)=sin(2pi n delta)/(pi n)`.

If `g=gcd(a,v)`, `A=a/g`, `V=v/g`, the campaign records exact Bernoulli-polynomial formulas for the intersections at thresholds `1/13,1/14` and at equal threshold `1/14`. The correction sign is determined by residue classes `A mod14` and `V mod13`; **both signs occur**, so no universal favorable harmonic sign was promoted.

## 24. Exact terminal conditional close

Define `TS(h)` to mean that no configuration with `h` compressed multiples of 13 and `13-h` outsiders can satisfy all original distinctness/primitivity constraints while having the exact outsider probe sets cover `F_13` for **every** `tau in W_h`.

Then

`TS(1) & TS(2) & ... & TS(6)`

would prove the 13-effective-speed Lonely Runner case. This implication has no hidden bridge: every counterexample has `1<=h_13<=6` and would furnish precisely one forbidden `TS(h)` configuration.

The packet does **not** prove those six saturation statements.

## 25. Final normal form / exact live throat

A genuine counterexample must simultaneously satisfy:

- every 12-deletion is primitive;
- at least one 12-deletion is strictly non-tight;
- one fixed deleted runner has private witnesses on every sufficiently fine denominator grid;
- private-witness mass is quantitatively positive;
- every modulus satisfies the exact gcd-sensitive probe-capacity law;
- gcd bounds `1,2,4,9,36,288` hold for subset sizes `12,11,10,9,8,7`;
- all seven dominant-gap restrictions hold;
- the 13 speeds satisfy a nonzero coefficient-2 additive relation;
- `1<=h_13<=6` and the corresponding exact lifted-probe saturation constraints hold.

The campaign's final missing implication is an extension obstruction: rule out extension of the forced primitive, non-tight 12-speed deletion by one integer speed under this arithmetic/probe/additive normal form.

**Full LRC(13) close: NO. Terminal structural reduction: YES.**
