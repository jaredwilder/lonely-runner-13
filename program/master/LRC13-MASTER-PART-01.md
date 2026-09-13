=
2-\mathbf1_{\{\|v\tau\|\le1/14\}}.
}
\]

When two slots occur:
\[
\boxed{
S_v(\tau)=
\{-r^{-1}n,-r^{-1}(n+1)\}\pmod{13}.
}
\]

Fixed chord displacement:
\[
\boxed{-v^{-1}\pmod{13}.}
\]

This is one of the central reusable lemmas of the session.

---

## B11. Deleted-runner multiplicity proof (Round 16)

Deleting any outsider and applying \(k=12\), then lifting its witness to the 13-grid, gives a particularly clean proof:
\[
\boxed{h_{13}\le6.}
\]

In the equality branch \(h_{13}=6\), the deleted outsider owns a probe at which it is the unique bad outsider.

---

## B12. Private-Probe Theorem (Round 16)

If
\[
h_{13}=6,
\]
then for every outsider \(v_j\) there exists a phase and 13-probe cover with a probe covered by \(v_j\) and by no other outsider.

**Important precision:** this does not imply that \(v_j\) is in one-slot mode at that phase.

---

## B13. Threshold-matched universal resonance law (Round 19 + terminal audit)

For general
\[
1\le h=h_{13}\le6,
\]
write the multiples as \(13a_i\) and define
\[
W_h=\{\tau:\|a_i\tau\|\ge1/14\ \forall i\}.
\]

Then
\[
\boxed{\mu(W_h)\ge(7-h)/7.}
\]

For every \(\tau\in W_h\), all \(h\) multiples are safe on all 13 lifted probes.

Let
\[
Z_h(\tau)=
\#\{v:\|v\tau\|\le1/14\}.
\]

Coverage forces
\[
\boxed{
Z_h(\tau)\le13-2h.
}
\]

This is the final global reference-safe resonance normal form.

---

## B14. Extremal universal saturation (Rounds 17–19)

For
\[
h_{13}=6,
\]
define
\[
W=\{\tau:\|a_i\tau\|\ge1/14,\ i=1,\dots,6\}.
\]

Then
\[
\boxed{\mu(W)\ge1/7}
\]
and for every \(\tau\in W\),
\[
\boxed{Z(\tau)\le1.}
\]

Therefore every phase in \(W\) has exactly one of two 13-cover states:

### Exact partition
\[
\boxed{2+2+2+2+2+2+1}
\]
with no overlap.

### One-overlap cover
\[
\boxed{2+2+2+2+2+2+2}
\]
with exactly one doubled probe.

---

## B15. Strict witness-measure theorem (terminal extraction; new)

Let
\[
M=\max_i|a_i|.
\]

All six internal bad sets contain
\[
\{\|\tau\|<1/(14M)\},
\]
a common interval of measure \(1/(7M)\).

Consequently
\[
\boxed{
\mu(W)
\ge
\frac17+\frac{5}{7M}
>
\frac17.
}
\]

General form for \(h\) multiples:
\[
\boxed{
\mu(W_h)
\ge
\frac{7-h}{7}+\frac{h-1}{7M}.
}
\]

This is stronger than the Round-19 union-bound estimate for every concrete finite tuple.

---

## B16. Forced handoff law (Round 17)

Inside \(\operatorname{int}(W)\), at a generic event where exactly one outsider changes between one-slot and two-slot mode:

- the disappearing slot must be the unique doubled probe immediately before a two-to-one transition;
- the appearing slot must become the unique doubled probe immediately after a one-to-two transition.

The slot displacement for runner \(v_j\) is
\[
-v_j^{-1}\pmod{13}.
\]

**Scope:** local/generic transitions only. No global winding theorem was proved.

---

## B17. Internal private witnesses (Round 19)

Delete one internal speed \(13a_j\).

The verified \(k=12\) theorem yields a physical time \(t_j\) at which all other 12 speeds are \(1/13\)-safe, while counterexample status forces \(13a_j\) to be \(<1/14\)-bad.

With
\[
\tau_j=13t_j\pmod1,
\]
\[
\boxed{\|a_j\tau_j\|<1/14,}
\]
while
\[
\boxed{\|a_i\tau_j\|\ge1/13\quad(i\ne j).}
\]

Thus every internal bad set is essential.

---

## B18. Exact partition polynomial (Round 15)

In an \(h_{13}=6\) phase with one singleton outsider, write for the six two-slot outsiders
\[
r_j=v_j\bmod13,\qquad
n_j=\lfloor v_j\tau\rfloor,
\]
and similarly the singleton data \((r_7,n_7,\delta)\).

Exact partition of all 13 residues implies
\[
\boxed{
\prod_{j=1}^{6}
(r_jX+n_j)(r_jX+n_j+1)
(r_7X+n_7+\delta)
=
C(X^{13}-X)
}
\]
in \(\mathbb F_{13}[X]\).

This is a true finite algebraic encoding of the slot partition.

**Strategic status:** LIVE but not a contradiction by itself; any valid residue partition produces such a factorization.

---

## B19. Exact unequal-threshold harmonic correction (Round 18)

With
\[
g=(a,v),\quad A=a/g,\quad V=v/g,
\]
\[
\mu(B_a(1/13)\cap B_v(1/14))
=
\frac{2}{91}
+
\kappa(A,V),
\]
where
\[
\boxed{
\kappa(A,V)=
\frac{
B_2(\{V/13-A/14\})
-
B_2(\{V/13+A/14\})
}{AV}.
}
\]

### Exact sign law
Let
\[
r=A\bmod14,\qquad s=V\bmod13,\ s\ne0.
\]

- \(r=0\) or \(7\): correction zero.
- \(r\in1,\dots,6\) and \(s\in1,\dots,6\): positive.
- \(r\in8,\dots,13\) and \(s\in7,\dots,12\): positive.
- opposite halves: negative.

The accompanying checker exhaustively verifies this finite sign table.

---

## B20. Equal-threshold harmonic correction (Round 19)

For both thresholds \(1/14\),
\[
\boxed{
\mu(B_a\cap B_v)
=
\frac1{49}
+
\frac{
B_2(\{(V-A)/14\})
-
B_2(\{(V+A)/14\})
}{AV}.
}
\]

For the \(6\times7=42\) internal–outsider pairs, the independent baseline is
\[
42/49=6/7,
\]
exactly matching
\[
\int X=6/7.
\]

If \(K_{14}\) is the sum of the 42 corrections:
\[
\boxed{
\int XZ=6/7+K_{14}.
}
\]

Counterexample saturation gives the bootstrap
\[
\boxed{
\mu(W)\ge1/7-K_{14}.
}
\]

Both signs occur, so no universal \(K_{14}<0\) theorem was obtained.

---

# C. RETRACTED TARGET-LEVEL ESTATE

## C1. The false edge discovered in Round 14

The campaign incorrectly used:

> If one chosen runner is a counterexample, then changing the stationary runner to any of the other 13 runners also gives a counterexample.

This implication is false.

Failure of loneliness for one runner does not imply failure for another runner.

Everything target-level depending on that edge was reopened/retracted.

---

## C2. Retracted claims / structures
