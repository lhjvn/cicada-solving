from GematriaPrimus import *
"""
This module contains the most prominent functions for working with the Liber Primus transcription.
"""

# Delimiters used in the transciption
"""
Delimiters
Word     : -
Clause   : .
Paragraph: &
Segment  : $
Chapter  : §
Line     : /
Page     : %
"""

def get_section(n:int):
    with open("../liber-primus.txt", "r", encoding="utf-8") as f:
        lines = f.read()
        return lines.split("$")[n-1]

def runeToLatin(section:str) -> str:
    pt = ''
    for rune in section:
        pt += RUNE_TO_LATIN.get(rune, rune)
    return pt


