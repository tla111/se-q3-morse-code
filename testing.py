def decode_bits(bits):
    # Splits the bits
    bits = bits.strip("0")
    # strip() - takes away character from first & end of string
    # 1. Executes Middle
    # "120011110013001"
    # testing = bits.split("0")
    # testing1 = bits.split("1")
    # print(testing)
    # print(testing1)
    step1 = [(bit) for bit in bits.split("1") + bits.split("0")]
    print(step1)
    step2 = [len(bit) for bit in bits.split("1") + bits.split("0")if bit]
    # If bit does not exist, do not return in list
    print(step2)
    step3 = min([len(bit) for bit in bits.split("1") + bits.split("0")if bit])
    print(step3)
    # print(bits)
    # for bit in bits.split("1") + bits.split("0"):
    #     if bit:
    #         print(bit)
    # bits_morsecode = bits.replace(
    #     "111" * freq, "-").replace(
    #         "1" * freq, ".").replace(
    #             "0000000" * freq, "   ").replace(
    #                 "000" * freq, " ").replace(
    #                     "0" * freq, "")

    # return bits_morsecode.strip()


decode_bits("120011110013001")
# decode_bits("1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011")
