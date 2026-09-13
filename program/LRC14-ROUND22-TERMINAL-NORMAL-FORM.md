# LRC(13) — Round 22 Terminal Normal Form
## Strict Deletion + Power-GCD + Additive-Relation Breakthrough

**Date:** 2026-08-07  
**Target:** 13 normalized positive integer speeds `u_1,...,u_13`, loneliness threshold `1/14`.

## Court status

**Full LRC(13) close: NOT YET EARNED.**

This public extraction records the reference-safe mathematical restrictions obtained for every hypothetical counterexample. The false all-reference branch is excluded; retracted material is separately listed in `LRC14-THEOREM-BANK.json`.

The campaign used the published `k<=12` frontier as an external input and then derived the statements below.

## 1. Strict deletion theorem

For each `j`, define the maximum loneliness of the 12-speed deletion

`lambda_j = max_t min_{i != j} ||u_i t||`.

The known 12-speed result gives `lambda_j >= 1/13`. Not all deletions can be tight:

> **There exists j with `lambda_j > 1/13`.**

Proof: if every `lambda_j=1/13`, set `C_i={t: ||u_i t||<=1/13}` and `N(t)=sum_i 1_{C_i}(t)`. Tightness forces `N(t)>=2` everywhere. But every `C_i` has measure `2/13`, hence `int N=2`, so `N=2` almost everywhere. Near `t=0`, however, all 13 speeds lie in their `C_i`, so `N=13` on a set of positive measure. Contradiction.

Thus any hypothetical counterexample contains a deletion with an open interval `I` on which

`||u_i t||>1/13` for every `i != j`,

while counterexample status forces

`||u_j t||<1/14` throughout `I`.

So the deleted runner has a robust private interval, not merely an isolated private witness.

## 2. Primitive deletions and divisor restrictions

The campaign's all-prime probe inequality is

`p <= (13-h_p) ceil(p/7)`,

where `h_p` is the number of speeds divisible by prime `p`.

No prime can satisfy this with `h_p>=12`, so every 12-speed deletion is primitive:

`gcd(u_1,...,u_hat_j,...,u_13)=1` for all `j`.

Combining with strict deletion: every counterexample contains a **primitive non-tight 12-speed deletion**.

The same probe law gives

`h_2<=11, h_3<=10, h_5<=8, h_7<=6, h_11<=7, h_13<=6`,

and the mandatory-divisor argument gives `h_13>=1`; hence

`1 <= h_13 <= 6`.

## 3. Exact finite budget and divisor-support identity

The imported finite-checking criterion gives

`G(u) = sum_{S subseteq [13]} gcd(u_i : i in S) <= 91^12`,

with the empty-set term zero. Numerically,

`91^12 = 322475487413604782665681`.

In particular every speed is at most this constant.

Let `h_d=#{i:d|u_i}`. Using `m=sum_{d|m} phi(d)` and reversing the sums gives the exact identity

`G(u) = sum_{d>=1} phi(d) (2^{h_d}-1)`.

Thus every hypothetical counterexample obeys

`sum_{d>=1} phi(d) (2^{h_d}-1) <= 91^12`.

The terminal supplement records the resulting majority-gcd ceiling sequence

`1, 1, 2, 4, 9, 36, 288`

for subsets of sizes `13,12,11,10,9,8,7` respectively.

## 4. GCD-sensitive probe capacity

For modulus `q` and outsider speed `v`, put `d=gcd(v,q)`, `Q=q/d`. The exact capacity bound is

`N_{q,v}(tau) <= d ceil(Q/7) = gcd(v,q) ceil(q/(7 gcd(v,q)))`.

This replaces a binary divisibility label by a quantitative capacity inequality.

## 5. The h_7=6 transition-cover theorem

Suppose exactly six speeds are divisible by 7, written `7a_1,...,7a_6`, with seven outsiders `v` not divisible by 7. Define

`W={tau: ||a_i tau||>=1/14 for i=1,...,6}`.

At each lifted seven-probe phase the six divisible speeds are safe; every outsider can kill at most one probe, so a counterexample forces each outsider to kill exactly one. The transition points for an outsider `v` are

`T_v={(2k+1)/(2v):0<=k<v}`.

Those points must lie outside `W`, so the six internal bad sets cover all `v` transition points. If `d_i=gcd(a_i,v)`, then

`v <= sum_{i=1}^6 d_i ceil((v/d_i)/7)`.

Consequently

`sum_i gcd(a_i,v) >= v/7`,

so some `i` has

`gcd(a_i,v) >= v/42`,

and therefore

`v <= 6(7a_i)`.

Hence every outsider is quantitatively anchored to an internal 7-multiple.

## 6. Exact degree-two Riesz obstruction

Call `V` 2-dissociated if

`sum_v epsilon_v v=0`, with every `epsilon_v in {-2,-1,0,1,2}`,

forces all coefficients to vanish. Let

`P(x)=(2/3)(1-cos(2 pi x))^2`.

`P` is nonnegative, has mean 1, and Fourier support in `{-2,-1,0,1,2}`. For a 2-dissociated `n`-set, the Riesz product `R(t)=prod_{v in V} P(vt)` has integral 1. Testing the bad-set cover against `R(t)dt` gives

`1 <= n (2/3)(1-cos(2 pi delta))^2`,

where `delta=ML(V)`. Therefore

`ML(V) >= (1/(2 pi)) arccos(1-sqrt(3/(2n)))`.

For `n=13`, the lower bound is approximately `0.135210985878358 > 1/14`.

Therefore every hypothetical 13-speed counterexample must fail 2-dissociation: there is a nonzero coefficient vector

`epsilon_i in {-2,-1,0,1,2}`

with

`sum_i epsilon_i u_i = 0`.

## 7. Terminal normal form

Every hypothetical counterexample is simultaneously:

1. primitive after every one-coordinate deletion;
2. non-tight after at least one deletion, with a robust private interval;
3. bounded by `G(u)<=91^12`;
4. constrained by the power-sensitive majority-gcd hierarchy;
5. constrained by the campaign's dominant-gap restrictions;
6. constrained by all-prime multiplicity laws;
7. additively dependent through coefficients in `[-2,2]`;
8. in the extremal `h_7=6` branch, constrained by the transition-cover gcd inequality above.

The clean remaining throat is the **Primitive Non-Tight Extension Lemma**: prove that the forced primitive non-tight 12-speed deletion cannot be extended by one distinct speed to a `1/14` counterexample under these arithmetic restrictions.

That lemma was **not proved**. The full conjecture remains open in this release.