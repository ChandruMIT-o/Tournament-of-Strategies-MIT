# Name: Harshini
# Name: Sharmistha

# School/College: NSN memorial
# Randomness: False
# Complexity: 1

def fire_and_ice(own, opp):

    if len(own) < 3:
        return False
    elif (not opp[-3]) and (not opp[-2]) and (not opp[-1]):
        return True
    elif (not opp[-3]) and (not opp[-2]) and (opp[-1]):
        return False
    elif (not opp[-3]) and (opp[-2]) and (not opp[-1]):
        return False
    elif (opp[-3]) and (not opp[-2]) and (not opp[-1]):
        return True
    elif (opp[-3]) and (opp[-2]) and (opp[-1]):
        return False
    elif (opp[-3]) and (opp[-2]) and (not opp[-1]):
        return False
    elif (opp[-3]) and (not opp[-2]) and (opp[-1]):
        return True
    elif (not opp[-3]) and (not opp[-2]) and (opp[-1]):
        return False