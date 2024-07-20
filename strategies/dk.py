# Deepshikha
# Krishanthini

# SNDJAVV

def dk(own, opp):

    if len(own) < 2: return False

    if not own[-1] and not own[-2]:
        return True
    elif own[-1]:
        return False
    elif not own[-1]:
        return False