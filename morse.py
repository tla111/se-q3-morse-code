#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
from morse_dict import MORSE_2_ASCII
__author__ = """ Timothy La (tla111)
Received help from John W
For decode_bits(), worked with Howard,
Jasmyine, & Bethsheba in Study Hall
"""


def decode_bits(bits):
    bits = bits.strip("0")
    freq = min([len(bit) for bit in bits.split("1") + bits.split("0") if bit])

    bits_morsecode = bits.replace(
        "111" * freq, "-").replace(
            "1" * freq, ".").replace(
                "0000000" * freq, "   ").replace(
                    "000" * freq, " ").replace(
                        "0" * freq, "")

    return bits_morsecode.strip()


def decode_morse(morse):
    MORSE_2_ASCII[""] = " "
    result = ""
    turn_string_to_list = morse.split(" ")
    for letter in turn_string_to_list:
        result += MORSE_2_ASCII[letter]
    print(" ".join(result.split()))
    return " ".join(result.split())


decode_morse(".... . -.--   .--- ..- -.. .")
if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
