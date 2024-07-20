# Karan
# Jeremy Gladsyn
# Isha Ahmed
# Edwin E S

# School/College: Central Polytechnic
# Randomness: False
# Complexity: 1

def quadcom(own, opp):
    def alternating_booleans(length):
      true_block = 4
      false_block = 3
      result = []
      cycle = 0
      while len(result) < length:

        result.extend([False] * (false_block + cycle))
        result.extend([True] * true_block)

        false_block -= 1
        true_block -= 1

        if (true_block == 0 or false_block == 0):
            true_block = 4
            false_block = 3
      
      return result[:length]
    
    length = len(own)

    return alternating_booleans(length+1)[-1] 