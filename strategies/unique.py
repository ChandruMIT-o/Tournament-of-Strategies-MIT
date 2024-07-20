def unique(own, opp):

    if len(own) < 4:
        return False
    elif (not own[-1]) and (not own[-2]) and (not own[-3]) and (not own[-4]):
        return True
    elif opp[-1]:
        return True
    else:
        return False