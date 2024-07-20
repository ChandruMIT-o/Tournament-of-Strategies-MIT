# Name: Kanisha
# Name: Saadhana
# Name: Shangamithra

# School/College: NSN memorial 
# Randomness: False
# Complexity: 1

def multiples_of_2(own, opp):
    
    def alternating_booleans(length):
      
      true_block = 1
      false_block = 2
      result = []
      cycle = 0

      while len(result) < length:

        result.extend([False] * (false_block + cycle))
        result.extend([True] * true_block)

        false_block += 2
      
      return result[:length]
    length = len(own)

    return alternating_booleans(length+1)[-1] 