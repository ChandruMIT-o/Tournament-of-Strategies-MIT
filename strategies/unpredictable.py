# Name: Gopika
# School/College: Central Polytechnic
# Randomness: False
# Complexity: 1

def unpredictable(own, opp):
    if len(own) < 4:
        return True
    elif (not own[-1]) and (not own[-2]):
        return True
    elif (own[-1]) and (not own[-2]):
        return True
    elif (not own[-1]) and (own[-2]):
        return False
    elif (own[-1]) and (own[-2]):
        return False