VND = 24275

def convertMoney(price: float):
    converted_price = price * VND
    formatted_price = "{:,.2f}".format(converted_price)
    return formatted_price