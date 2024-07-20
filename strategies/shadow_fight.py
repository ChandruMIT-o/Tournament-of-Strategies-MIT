import random

def shadow_fight(own, opp):
    
    def generate_random_binary_sequence(n):
      num_trues = n // 2
      num_falses = n - num_trues
      
      sequence = [True] * num_trues + [False] * num_falses
      
      random.shuffle(sequence)
      
      return sequence
    
    def alternating_booleans(length):
      true_block = 7
      false_block = 7
      result = [True]
      cycle = 0

      while len(result) < length:

        result.extend(generate_random_binary_sequence(true_block))
        result.extend([False] * (false_block + cycle))

        true_block += 7
        false_block += 7
      
      return result[:length]
    
    length = len(own)

    if length == 0:
       return True

    return alternating_booleans(length+1)[-1] 