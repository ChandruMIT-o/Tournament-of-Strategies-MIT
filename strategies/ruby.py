def ruby(own,opp):
    if len(own) % 4 == 0:
        return False
    if len(own) % 4 == 1:
        return opp[-1]
    if len(own) % 4 == 2:
        return True
    if len(own) % 4 == 3:
        return False