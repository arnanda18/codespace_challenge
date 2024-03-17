def reverse_and_mirror(s1, s2):
    reversed_string1 = s1[::-1].swapcase()
    mirrored_string1 = reversed_string1 + s1.swapcase()

    reversed_string2 = s2[::-1].swapcase()
    mirrored_string2 = reversed_string2

    concat = '@@@'.join([mirrored_string2, mirrored_string1])

    return concat


print(reverse_and_mirror('FizZ', 'buZZ'))