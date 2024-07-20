def rcb(own, opp):
    if len(own) % 8==0:
        return False
    if len(own) % 4==0:
        return True
    return own[-1]