def f(fisrt, second):
    one_len = len(fisrt)
    two_len = len(second)
    if one_len > two_len:
        fisrt, second = second, fisrt
        one_len, two_len = two_len, one_len

    alle = range(one_len + 1)
    for i in range(1, two_len + 1):
        other, alle = alle, [i] + [0] * one_len
        for j in range(1, one_len + 1):
            some, some_2, ch = other[j] + 1, alle[j - 1] + 1, other[j - 1]
            if fisrt[j - 1] != second[i - 1]:
                ch += 1
            alle[j] = min(some, some_2, ch)

    return alle[one_len]