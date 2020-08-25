from morse_dict import MORSE_2_ASCII


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

    print(highest)
    return highest

    # for x in range(len(bits)):
    #     if bits[x:x+3] == "111":
    #         bits_morsecode += "-"
    #     elif bits[x] == "1":
    #         bits_morsecode += "."
    #     elif bits[x] == "0":
    #         bits_morsecode += " "

    # print(bits_morsecode)


decode_bits("11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011")


# def decode_morse(morse):
#     MORSE_2_ASCII[""] = " "
#     result = ""
#     turn_string_to_list = morse.split(" ")
#     for letter in turn_string_to_list:
#         result += MORSE_2_ASCII[letter]
#     print(" ".join(result.split()))
#     return " ".join(result.split())


# decode_morse(".... . -.--   .--- ..- -.. .")
