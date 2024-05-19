from collections import Counter

def findAnagrams(s: str, p: str) -> list[int]:
    if len(s) < len(p):
        return []

    output = []
    p_cnt = Counter(p)
    print(f"p_cnt = {p_cnt}")

    for i in range(0, len(s) - len(p) + 1):
        substr = s[i:i + len(p)]
        print(f"i = {i}")
        print(f"substr = {substr}")
        substr_cnt = Counter(substr)

        if substr_cnt == p_cnt:
            output.append(i)

    return output

if __name__ == '__main__':
    # s = "cbaebabacd"
    # p = "abc"
    s = "abab"
    p = "ab"

    ans = findAnagrams(s=s, p=p)
    print(f"s: {s}")
    print(f"p: {p}")
    print(f"The answer is {ans}")