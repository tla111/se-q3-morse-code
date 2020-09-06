from morse_dict import MORSE_2_ASCII

# This function will transcode (covert encoded date) the binary
#   sequence into Morse code representation


def decode_bits(bits):
    # Take off any 0's in the front or back of string
    # In this case, no need to since both ends have 1s
    bits = bits.strip("0")
    # 1. If bit is true
    #       Run the for loop
    # 2. Get the length of each bit and store in list
    # 3. Output the value of the minimum number of occurrence
    freq = min([len(bit) for bit in bits.split("1")
                + bits.split("0") if bit])

    # Multiply the "string" by the freq (2) &
    #   replace it with a new value
    # Ex: "111" * 2(freq) = "111111" ->
    #   Replace "111111" to "-"
    # Ex: "1" * 2(freq) = "11" ->
    #   Replace "11" to "."
    bits_morsecode = bits.replace(
        "111" * freq, "-").replace(
            "1" * freq, ".").replace(
                "0000000" * freq, "   ").replace(
                    "000" * freq, " ").replace(
                        "0" * freq, "")

    # Return bits_morsecode
    #   Leading and trailing whitespaces are removed
    return bits_morsecode.strip()


hey_jude_bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"
print(decode_bits(hey_jude_bits))


# This function will decode the morse code (..-..) to words


def decode_morse(morse):
    # Create a "" as a key in MORSE_2_ASCII
    # & store " " as the value
    # Ex: {"": " "}
    MORSE_2_ASCII[""] = " "
    # Store an empty string in a variable (result)
    result = ""
    # The split() breaks up a string at the specified
    #   separator and return a list of strings
    # In the case of splitting an empty string,
    #   the first mode(no argument) will return an
    #   empty list because the whitespace is eaten
    #   and there are no values to put in the result list
    # https://stackoverflow.com/questions/16645083/
    # when-splitting-an-empty-string-in-python-why-
    # does-split-return-an-empty-list
    # Ex: ".... . -.--   .--- ..- -.. ."
    # ['....', '.', '-.--', '', '', '.---', '..-', '-..', '.']
    turn_string_to_list = morse.split(" ")
    # Loop over each item in the list
    for letter in turn_string_to_list:
        # The letter represents a value of a key in morse_dict.py
        # Store the key in result
        # Ex: ['....'] -> {"H": "...."} -> result = "H"
        # Ex: ['.'] -> {"E": "."} -> result = "HE"
        # Ex: ['-.--'] -> {"Y": "-.--"} -> result = "HEY"

        # We defined a new key, "" and gave it a value of " "
        #   This gives space to the words
        # Ex: [''] -> {"": " "} -> result = "HEY "
        result += MORSE_2_ASCII[letter]
        print(result)
    # Result is a list -> split the list into a string
    # Join the strings together to one string &
    #   separate them by a space
    # Ex: HEY  JUDE -> HEYJUDE -> HEY JUDE
    #        result   result.split   " ".join()
    print(" ".join(result.split()))
    return " ".join(result.split())


# decode_morse(".... . -.--   .--- ..- -.. .")
