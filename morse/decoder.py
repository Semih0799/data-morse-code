"""
This module provides functions to decode Morse code into text.
Functions:
- decode(morse_code): Decodes Morse code back into text.
"""
from morse.mapping import MORSE

def decode_word(morse_word):
    """
    Decodes a single Morse code word into text.
    Letters are separated by a space.
    """
    reverse_morse = {v: k for k, v in MORSE.items()}
    letters = morse_word.split()
    return "".join(reverse_morse.get(letter, "") for letter in letters)

def decode(morse_code):
    """
    Decodes Morse code back into text.
    Words separated by | and letters by space.
    """
    words = morse_code.split("|")
    return " ".join(decode_word(word) for word in words)
    
    
if __name__ == "__main__":
    from morse.encoder import encode
    
    # Example usage for one word
    EXAMPLE_TEXT = "abc"
    ENCODED = encode(EXAMPLE_TEXT)
    DECODED = decode(ENCODED)
    print(f"'{EXAMPLE_TEXT}' -> '{ENCODED}' -> '{DECODED}'")
    
    # Example usage for one sentence
    EXAMPLE_TEXT = "Hi Guys"
    ENCODED = encode(EXAMPLE_TEXT)
    DECODED = decode(ENCODED)
    print(f"'{EXAMPLE_TEXT}' -> '{ENCODED}' -> '{DECODED}'")
