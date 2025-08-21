"""
Contains all known mappings for the liber primus alphabet
"""

GEMATRIAPRIMUS = (
            (u"ᚠ", "f", 2, 0),
            (u"ᚢ", "v", 3, 1),
            (u"ᚢ", "u", 3, 1),
            (u"ᚦ", "T", 5, 2),  # th
            (u"ᚩ", "o", 7, 3),
            (u"ᚱ", "r", 11, 4),
            (u"ᚳ", "k", 13, 5),
            (u"ᚳ", "c", 13, 5),
            (u"ᚷ", "g", 17, 6),
            (u"ᚹ", "w", 19, 7),
            (u"ᚻ", "h", 23, 8),
            (u"ᚾ", "n", 29, 9),
            (u"ᛁ", "i", 31, 10),
            (u"ᛄ", "j", 37, 11),
            (u"ᛇ", "E", 41, 12),  # eo
            (u"ᛈ", "p", 43, 13),
            (u"ᛉ", "x", 47, 14),
            (u"ᛋ", "z", 53, 15),
            (u"ᛋ", "s", 53, 15),
            (u"ᛏ", "t", 59, 16),
            (u"ᛒ", "b", 61, 17),
            (u"ᛖ", "e", 67, 18),
            (u"ᛗ", "m", 71, 19),
            (u"ᛚ", "l", 73, 20),
            (u"ᛝ", "G", 79, 21),  # ing
            (u"ᛝ", "G", 79, 21),  # ng
            (u"ᛟ", "O", 83, 22),  # oe
            (u"ᛞ", "d", 89, 23),
            (u"ᚪ", "a", 97, 24),
            (u"ᚫ", "A", 101, 25),  # ae
            (u"ᚣ", "y", 103, 26),
            (u"ᛡ", "I", 107, 27),  # ia
            (u"ᛡ", "I", 107, 27),  # io
            (u"ᛠ", "X", 109, 28),  # ea
)
LATSIMPLE = (
            ("T", "th"),
            ("E", "eo"),
            ("G", "ing"),
            ("G", "ng"),
            ("O", "oe"),
            ("A", "ae"),
            ("I", "io"),
            ("I", "ia"),
            ("X", "ea"),
        )

# We do NOT operate on latin thats why we DONT want any mappings using latin as key

RUNE_TO_PRIME = {rune: prime for rune, _, prime, _ in GEMATRIAPRIMUS}
RUNE_TO_IDX = {rune: idx for rune, _, _, idx in GEMATRIAPRIMUS}

PRIME_TO_IDX = {prime: idx for _, _, prime, idx in GEMATRIAPRIMUS}
IDX_TO_PRIME = {idx: prime for _, _, prime, idx in GEMATRIAPRIMUS}

PRIME_TO_LATIN = {prime: latin for _, latin, prime, _ in GEMATRIAPRIMUS}
IDX_TO_LATIN = {idx: latin for _, latin, _, idx in GEMATRIAPRIMUS}
IDX_TO_RUNE = {idx: rune for rune, _, _, idx in GEMATRIAPRIMUS}
RUNE_TO_LATIN = {rune: latin for rune, latin, _, _ in GEMATRIAPRIMUS}

# Export all dictionaries and tuples
__all__ = [
    'GEMATRIAPRIMUS',
    'LATSIMPLE',
    'RUNE_TO_PRIME',
    'RUNE_TO_IDX',
    'PRIME_TO_IDX',
    'IDX_TO_PRIME',
    'PRIME_TO_LATIN',
    'IDX_TO_LATIN',
    'RUNE_TO_LATIN',
    'IDX_TO_RUNE'
]