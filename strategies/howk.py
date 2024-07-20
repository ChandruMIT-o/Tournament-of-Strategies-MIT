# Name: Anirudh
# Name: Abhinav

# School/College: SKNSPMC VV (Perambur)
# Randomness: False
# Complexity: 1

def howk(own, opp):
    def alternating_booleans(length):
      true_block = 1
      false_block = 1
      result = []
      cycle = 0
      temp = 0
      while len(result) < length:

        result.extend([False] * (false_block + cycle))
        result.extend([True] * true_block)

        if temp%2 == 1:
            false_block = 1
        else:
            false_block = 3

        temp += 1
      return result[:length]
    length = len(own)

    return alternating_booleans(length+1)[-1] 