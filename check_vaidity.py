def validity(list, curency1, curency2, amount):
    if curency1 not in list:
        return f"{curency1} is not in ower currencyes"
    if curency2 not in list:
        return f"{curency2} is not in ower currencyes"

    try:
          if int(amount) <= 0:
            return f'Amount shud be positive yours is {amount}'
    except ValueError:
        return f"{amount} is not a number"
  
    return True
