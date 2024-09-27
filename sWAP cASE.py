def swap_case(s):
    r = ""
    for x in s:
        a = ord(x)
        if 65 <= a <= 90:
            r += chr(a + 32)
        elif 97 <= a <= 122:
            r += chr(a - 32)
        else:
            r += x
    return r