def apply_discount(price, percentage):
    return price - (price * percentage / 100)


def card_discount(pricee, cardCompany):
    if cardCompany == "HDFC":
        return pricee - (pricee * 15 / 100)
    elif cardCompany == "SBI":
        return pricee - (pricee * 20 / 100)
    else:
        return pricee - (pricee * 5 / 100)