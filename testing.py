from morse_dict import MORSE_2_ASCII


def decode_morse(morse):
    MORSE_2_ASCII[""] = " "
    result = ""
    turn_string_to_list = morse.split(" ")
    for letter in turn_string_to_list:
        result += MORSE_2_ASCII[letter]
    print(" ".join(result.split()))
    return " ".join(result.split())


decode_morse(".... . -.--   .--- ..- -.. .")
