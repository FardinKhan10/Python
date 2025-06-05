def applyDc(p,d):
    return p - (p*d/100) 

def menu(a):
    if (a == "water"):
        return "Water Bottle"

    elif (a == "bill"):
        return "Food Bill"

    else:
        return "Not Available"