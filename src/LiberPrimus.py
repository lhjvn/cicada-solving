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

# known_solved = get_section(18) + get_section(3)  +get_section(7) + get_section(5) 
# rune_freq = Counter(r for r in known_solved if r in RUNE_TO_LATIN)
# total = sum(rune_freq.values())
# normalized_freq = {rune: count / total for rune, count in rune_freq.items()}

normalized_freq = {'ᛈ': 0.016423357664233577, 'ᚪ': 0.060218978102189784, 'ᚱ': 0.06934306569343066, 'ᛒ': 0.02281021897810219, 'ᛚ': 0.03923357664233577, 'ᛖ': 0.1259124087591241, 'ᛁ': 0.055656934306569344, 'ᚳ': 0.03923357664233577, 'ᚦ': 0.03832116788321168, 'ᚾ': 0.0666058394160584, 'ᛋ': 0.0666058394160584, 'ᛏ': 0.058394160583941604, 'ᚢ': 0.05474452554744526, 'ᛝ': 0.014598540145985401, 'ᚩ': 0.08759124087591241, 'ᚠ': 0.016423357664233577, 'ᚹ': 0.040145985401459854, 'ᛗ': 0.02645985401459854, 'ᚻ': 0.02281021897810219, 'ᛞ': 0.03193430656934307, 'ᚣ': 0.012773722627737226, 'ᚷ': 0.013686131386861315, 'ᛡ': 0.010948905109489052, 'ᚫ': 0.0018248175182481751, 'ᛠ': 0.0072992700729927005}

if __name__ == "__main__":
    print()