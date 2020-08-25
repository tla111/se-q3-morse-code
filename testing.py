from morse_dict import MORSE_2_ASCII

# Referenced https://www.geeksforgeeks.org/largest-substring-with-same-characters/


def decode_bits(bits):
    bits_morsecode = ""
    highest, frequency = 1, 1
    for occur in range(1, len(bits)):
        if bits[occur] == bits[occur - 1]:
            frequency += 1
        else:
            highest = max(highest, frequency)
            frequency = 1
    highest = max(highest, frequency)
    freq = highest // 7

    for x in range(len(bits)):
        if bits[x:x + (3 * freq)] == "111" * freq:
            bits_morsecode += "-"
        elif bits[x] == "1":
            bits_morsecode += "."
        elif bits[x] == "0":
            bits_morsecode += " "

    print(bits_morsecode)


decode_bits("1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011")


# def decode_morse(morse):
#     MORSE_2_ASCII[""] = " "
#     result = ""
#     turn_string_to_list = morse.split(" ")
#     for letter in turn_string_to_list:
#         result += MORSE_2_ASCII[letter]
#     print(" ".join(result.split()))
#     return " ".join(result.split())


# decode_morse(".... . -.--   .--- ..- -.. .")
