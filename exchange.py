"""A currency exchange program for someone bad at math."""

def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    exchanged_val = budget/exchange_rate
    return exchanged_val


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    amt_remaining = budget-exchanging_value
    return amt_remaining 


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    total_value = denomination * number_of_bills
    return total_value


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    number_of_bills = int(budget/denomination)
    return number_of_bills


def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    leftover = budget % denomination
    return leftover


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    #calculate spread percent of exchanage rate, add exchange rate 
    new_rate = exchange_rate + (exchange_rate * (spread / 100)) 

    #use the exchange_money() function to find total in new currency
    total_new_currency = exchange_money(budget, new_rate)

    #find value of all bills by forcing total/denom into int()
    bill_val_new_currency = int(total_new_currency / denomination)

    #multiply bill's value by denom to get new bill value
    max_val_new_currency = bill_val_new_currency * denomination

    return max_val_new_currency
