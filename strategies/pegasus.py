# Mithilesh Raghav
# Muthu Mugunthan
# Sesha
# Nimesh Kumar

# SNDJAVV

def pegasus(own, opp):

    if len(own) < 2: return False

    if opp[-1] and opp[-2]:
        return False
    elif not opp[-1]:
        return False
    elif opp[-1]:
        return True