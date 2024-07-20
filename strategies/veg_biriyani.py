# Guru Charan
# Lakshit
# Prathish
# Sudalai Lokeshwaran

# School/College: NSN memorial
# Randomness: False
# Complexity: 1

def veg_biriyani(own, opp):
    def alternating_booleans(length):
      true_block = 2
      false_block = 4
      result = []
      cycle = 0

      while len(result) < length:

        result.extend([False] * (false_block + cycle))
        result.extend([True] * true_block)
      
      return result[:length]
    length = len(own)

    return alternating_booleans(length+1)[-1] 