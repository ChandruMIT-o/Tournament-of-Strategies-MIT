# Name: Abirami
# School/College: Central Polytechnic
# Randomness: False
# Complexity: 1

def kemomachi(own, opp):
    
    def alternating_booleans(length):
      true_block = 10
      false_block = 5
      result = []
      cycle = 0
      while len(result) < length:

        result.extend([True] * true_block)

        result.extend([False] * (false_block + cycle))

        true_block, false_block = false_block, true_block
      
      return result[:length]
    
    length = len(own)

    return alternating_booleans(length+1)[-1] 