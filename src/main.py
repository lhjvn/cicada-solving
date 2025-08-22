from LiberPrimus import get_section, runeToLatin
from InstarCrypto import find_best_substitution

koan2 = get_section(6)
print(koan2)

# koan2 is encrypted using vignere cipher with key 'ᚠᛁᚱᚠᚢᛗᚠᛖᚱᛖᚾᚠᛖ' len 13

# Try to find the best substitution for koan2
key_length = 13  # Known from the comment
best_key, s , pt = find_best_substitution(koan2)

print(f"Best key found: {best_key}")


# Convert the known key from runes to Latin for comparison
known_key_runes = 'ᚠᛁᚱᚠᚢᛗᚠᛖᚱᛖᚾᚠᛖ'
known_key_latin = runeToLatin(known_key_runes)
print(f"Known key: {known_key_latin}")

# Compare the found key with the known key
if best_key == known_key_latin:
    print("The found key matches the known key!")
else:
    print("The keys don't match.")