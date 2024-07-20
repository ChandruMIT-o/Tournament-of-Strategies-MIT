# Srinivasa Kesavan
# Samnijith
# Hrithick
# Nikil

# School/College: NSN memorial
# Randomness: False
# Complexity: 1

def sshn(own, opp):

    def generate_sequence(n):

        alt_true_false_10 = [True, False] * 5
        false_10 = [False] * 10
        
        pattern =  alt_true_false_10 + false_10
        
        repeat_pattern = pattern + pattern[-20:]
        
        sequence = (pattern + repeat_pattern * ((n - len(pattern)) // len(repeat_pattern) + 1))[:n]
        
        return sequence

    
    length = len(own)

    if length < 3: 
        return False
    else:
        return generate_sequence(length+1)[-4] 