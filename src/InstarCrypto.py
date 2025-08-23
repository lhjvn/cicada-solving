from GematriaPrimus import RUNE_TO_IDX, IDX_TO_RUNE
from PrimusFrequencies import NORMALIZED_FREQ_PLAINTEXT

from collections import Counter

def applyShift(text: str, shift: int) -> str:
    """
    Apply a shift to the given text by shifting each rune by the specified amount.
    """
    shifted = ""
    for char in text:
        if char in RUNE_TO_IDX:
            idx = (RUNE_TO_IDX[char] + shift) % len(IDX_TO_RUNE)
            shifted += IDX_TO_RUNE[idx]
        else:
            shifted += char
    return shifted

def applyMultiShift(text: str, shifts:any) -> str:
    """
    Apply multiple shifts to the given text by shifting each rune by the specified amounts in sequence.
    """
    key = []
    # Parse key
    if type(shifts) == str:
        print("[?] Key is given in runes, parsing used GP IDX")
        key = [RUNE_TO_IDX[s] for s in shifts if s in RUNE_TO_IDX]
        print(f'[?] {shifts} <- {key}')
    elif type(shifts) == list:
        key = shifts
    try:
        sum(key)
    except TypeError:
        raise TypeError(f"Unsupported key type: Input does not contain valid shifts values")

    shifted = ""
    shift_len = len(key)
    key_idx = 0
    for i in range(len(text)):
        char = text[i]
        if char in RUNE_TO_IDX:
            idx = (RUNE_TO_IDX[char] + key[key_idx % shift_len]) % len(IDX_TO_RUNE)
            shifted += IDX_TO_RUNE[idx]
            key_idx += 1 # only increment key_idx when we shift a valid rune
        else:
            shifted += char
    return shifted


def scoreMonoSubstitution(text: str, reference_freq=NORMALIZED_FREQ_PLAINTEXT) -> float:
    """
    Score a text to detect if it's a mono-alphabetic substitution based on frequency analysis.
    Higher score indicates closer match to the expected frequency distribution.

    Args:
        text: The text to analyze
        reference_freq: The reference frequency distribution (default: normalized_freq)

    Returns:
        float: A score representing how well the frequencies match
    """
    # Count the runes in the input text
    text_freq = Counter(r for r in text if r in RUNE_TO_IDX)
    text_total = sum(text_freq.values())

    if text_total == 0:
        return 0.0

    # Normalize frequencies in the text
    text_normalized_freq = {rune: count / text_total for rune, count in text_freq.items()}

    # Calculate the score using frequency correlation
    # Lower sum of absolute differences means better match
    score = 0.0
    for rune in set(reference_freq.keys()) | set(text_normalized_freq.keys()):
        ref_val = reference_freq.get(rune, 0)
        text_val = text_normalized_freq.get(rune, 0)
        score -= abs(ref_val - text_val)  # Negative to make higher score better

    return score

# This function can also test for atbash by first encrypting `str` atbash. Then the function returns key=0.
def findBestSubstitution(ciphertext: str, key_space=None, reference_freq=NORMALIZED_FREQ_PLAINTEXT) -> tuple:
    """
    Find the best substitution key for a mono-alphabetic cipher.
    
    Args:
        ciphertext: The encrypted text
        key_space: Optional list of possible keys to try (default: tries shifts 0-29)
        reference_freq: The reference frequency distribution
        
    Returns:
        tuple: (best_key, best_score, decrypted_text)
    """
    if key_space is None:
        # Default to trying all shifts in the rune alphabet
        key_space = list(range(29))
    
    best_score = float('-inf')
    best_key = None
    best_text = None
    
    for key in key_space:
        # Apply the substitution by shifting each rune by 'key' positions
        decrypted = ""
        for char in ciphertext:
            if char in RUNE_TO_IDX:
                idx = (RUNE_TO_IDX[char] + key) % len(IDX_TO_RUNE)
                decrypted += IDX_TO_RUNE[idx]
            else:
                decrypted += char
        
        # Score the decrypted text
        score = scoreMonoSubstitution(decrypted, reference_freq)
        
        if score > best_score:
            best_score = score
            best_key = key
            best_text = decrypted
    return best_key, best_score, best_text

def atbash(text: str) -> str:
    """
    Apply the Atbash cipher to the given text using the rune alphabet.
    
    The Atbash cipher replaces each rune with its mirror position in the alphabet.
    For example, the first rune becomes the last, the second becomes the second-to-last, etc.
    
    Args:
        text: The text to encrypt/decrypt with Atbash
        
    Returns:
        str: The text after applying the Atbash transformation
    """
    result = ""
    
    for char in text:
        if char in RUNE_TO_IDX:
            # Find the position in the rune alphabet
            idx = RUNE_TO_IDX[char]
            # Calculate the mirror position
            mirror_idx = (28 - idx) % 29
            # Replace with the rune at the mirror position
            result += IDX_TO_RUNE[mirror_idx]
        else:
            # Keep non-rune characters unchanged
            result += char
    
    return result


__all__ = ["applyShift", "atbash", "findBestSubstitution", "scoreMonoSubstitution"]
