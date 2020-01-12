# CTCI, 1.1
def unique_characters(s):
    return len(set(s)) == len(s)
    
def unique_characters_in_place(s):
    s = sorted(''.join(s))
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return False
    return True
    
print(unique_characters('heyo'))
print(unique_characters_in_place('heyo'))