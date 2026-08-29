def rev(s):
    res = ""
    for i in range(0, len(s)):
        res = s[i] + res
    return res

if __name__ == "__main__":
    s = "malayalam"
    rev_s = rev(s)
    print(s)
    print(rev_s)
    if s == rev(s):
        print("pali")
    else:
        print("not")