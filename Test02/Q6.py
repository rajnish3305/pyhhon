def countvowel(str1):
    c = 0
    s="aeiouAEIOU"
    m = set(s)
    v = set(str1.lower())
    for alpha in v:
        if alpha in m:
            c = c + 1
    print("No. of vowels ::>", c)
str1="abeAEafghi"
countvowel(str1)