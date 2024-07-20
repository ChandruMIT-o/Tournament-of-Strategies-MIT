# Name: Maheshwaran
# School/College: Central Polytechnic
# Randomness: False
# Complexity: 1

def ninja(own, opp):
    
    def alternating_booleans(length):
      true_block = 11
      false_block = 6
      result = []
      cycle = 0
      while len(result) < length:
        false_block -= 1

        result.extend([True] * true_block)

        result.extend([False] * (false_block + cycle))

        cycle += 1
        true_block = 11
        false_block += 1

      
      return result[:length]
    
    length = len(own)

    return alternating_booleans(length+1)[-1] 