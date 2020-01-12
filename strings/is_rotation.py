def is_substring(s1, s2):
    return s2.find(s1) != -1

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    if set(s1) != set(s2):
        return False
    double_s1 = s1 + s1
    return is_substring(s2, double_s1)
    
s1 = "waterbottle"
s2 = "erbottlewat"
print(is_rotation(s1, s2))
