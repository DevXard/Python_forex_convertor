def validity(list, curency1, curency2, amount):
    result = []

    if curency1 not in list:
        result.append(f"{curency1} is not in ower currencyes") 
    if curency2 not in list:
        result.append(f"{curency2} is not in ow")

    try:
          if int(amount) <= 0:
            result.append(f'Amount shud be positive yours is {amount}') 
    except ValueError:
        result.append(f"{amount} is not a number") 
  
    return result
