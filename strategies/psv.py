# Name: Pranav
# Name: Sudharshan
# Name: Vignesh

# School/College: NSN memorial
# Randomness: False
# Complexity: 1

def psv(own, opp):
    def alternating_booleans(length):
        true_block = 1
        false_block = 1
        result = []
        cycle = 0
        temp = 0
        while len(result) < length:

            if temp % 9 == 0:
                false_block = 3
                true_block = 2
            elif temp % 9 == 1:
                false_block = 2
                true_block = 1
            elif temp % 9 == 2:
                false_block = 1
                true_block = 3
            elif temp % 9 == 3:
                false_block = 2
                true_block = 2
            elif temp % 9 == 4:
                false_block = 1
                true_block = 9
            elif temp % 9 == 5:
                false_block = 6
                true_block = 1
            elif temp % 9 == 6:
                false_block = 2
                true_block = 3
            elif temp % 9 == 7:
                false_block = 3
                true_block = 2
            elif temp % 9 == 8:
                false_block = 4
                true_block = 3
            
            result.extend([False] * (false_block + cycle))
            result.extend([True] * true_block)

            temp += 1
            
        return result[:length]
    
    length = len(own)

    return alternating_booleans(length+1)[-1] 