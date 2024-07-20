def shinchan(own,opp):

    if len(own) < 3:
        return False
    if 3 <= len(own) < 6:
        return True
    
    if not opp[-1] and len(own) % 2 == 0:
        return True
    else:
        return False
