def sequence_of_steps(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return sequence_of_steps(n-1) + sequence_of_steps(n-2) + sequence_of_steps(n-3)
    
print(sequence_of_steps(6))
