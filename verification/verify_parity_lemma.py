#!/usr/bin/env python3
"""Independent exact replay of the LRC(13) parity-certificate lemma.

For each parity mask e in {0,1}^13, search the advertised rational family
    x = n/(2d), 1 <= d <= 26, 0 <= n < 2d,
and test exactly whether
    min_{1<=i<=13} || i*x + e_i/2 || >= 1/13.

All comparisons are integer comparisons.  This script is independent of the
historical certificate CSV/verifier; it reconstructs certificates directly.
It certifies the finite lemma only, not the full analytic reduction and not
full LRC(13).
"""

from __future__ import annotations


def safe(i: int, bit: int, n: int, d: int) -> bool:
    den = 2 * d
    r = (i * n + bit * d) % den
    dist_num = min(r, den - r)
    return 13 * dist_num >= den


def masks_certified_by(n: int, d: int) -> list[int]:
    masks = [0]
    for i in range(1, 14):
        allowed = [bit for bit in (0, 1) if safe(i, bit, n, d)]
        if not allowed:
            return []
        nxt: list[int] = []
        for mask in masks:
            for bit in allowed:
                nxt.append(mask | (bit << (i - 1)))
        masks = nxt
    return masks


def main() -> None:
    cert: dict[int, tuple[int, int]] = {}
    candidate_points = 0

    for d in range(1, 27):
        for n in range(2 * d):
            masks = masks_certified_by(n, d)
            if not masks:
                continue
            candidate_points += 1
            for mask in masks:
                cert.setdefault(mask, (n, d))

    universe = set(range(1 << 13))
    missing = universe - set(cert)
    expected_missing = {0, 5461}

    assert len(cert) == 8190, len(cert)
    assert missing == expected_missing, sorted(missing)
    assert all(((5461 >> (i - 1)) & 1) == (i & 1) for i in range(1, 14))

    # Hostile replay of every stored certificate, one mask at a time.
    for mask, (n, d) in cert.items():
        for i in range(1, 14):
            bit = (mask >> (i - 1)) & 1
            assert safe(i, bit, n, d), (mask, n, d, i, bit)

    print(f"candidate rational points checked: {candidate_points}")
    print(f"certified masks: {len(cert)}/8192")
    print(f"uncertified masks: {sorted(missing)}")
    print("mask 5461 bits are e_i = i (mod 2)")
    print("PASS: exact parity-certificate lemma independently reconstructed")


if __name__ == "__main__":
    main()
