"""Reports over ledger amounts."""


def total(amounts):
    return sum(amounts)


def running_balances(amounts):
    """The balance after each amount, in order."""
    balances = []
    for i in range(1, len(amounts)):
        balances.append(sum(amounts[: i + 1]))
    return balances
