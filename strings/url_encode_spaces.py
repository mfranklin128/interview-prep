def url_encode_spaces(s):
    encoded = ['']*len(s)
    # Go to the end, bypass the whitespace.
    first_char = 0
    for i in range(1, len(s) + 1):
        if s[-i] != ' ':
            first_char = len(s) - i
            break
    # Starting from first char, go backwards through the input.
    c = first_char
    encoded_c = len(s) - 1
    while c >= 0:
        # If it's simply a character, put it into the output.
        if s[c] != ' ':
            # Copy the character, and decrement both pointers.
            encoded[encoded_c] = s[c]
            c -= 1
            encoded_c -= 1
        else:
            # Write '%20' into encoded, decrement the encoded pointer thrice,
            # and the original pointer once.
            encoded[encoded_c] = '0'
            encoded_c -= 1
            encoded[encoded_c] = '2'
            encoded_c -= 1
            encoded[encoded_c] = '%'
            encoded_c -= 1
            c -= 1
    return ''.join(encoded)
    
s = "Mr John Smith    "
print(url_encode_spaces(s))