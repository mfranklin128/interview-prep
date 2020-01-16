def permutations(s):
    if not s:
        return ['']
    to_return = []
    for i in range(len(s)):
        c = s[i]
        rem = ''.join(list(s)[:i] + list(s)[i+1:])
        remainder_permutations = permutations(rem)
        for j in range(len(remainder_permutations)):
            remainder_permutations[j] += c
        to_return += remainder_permutations
    return to_return
    
print(permutations("hey"))