s = "MCMXCIV"


def romanToInt(s: str) -> int:
    s = s[::-1]  # "VICXMCM""
    mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    s_lst = [i for i in s]  # ['M', 'C', 'M', 'X', 'C', 'I', 'V']
    n_lst = []
    for letter in s:
        if not n_lst:
            n_lst.append(mapping[letter])  # [5]
        else:
            if mapping[letter] < n_lst[-1]:  # 1 < 5
                n_lst[-1] -= mapping[letter]  # 5 -= 1
            else:
                n_lst.append(mapping[letter])
    return sum(n_lst[::-1])


print(romanToInt(s))

