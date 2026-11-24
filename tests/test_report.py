from ledger.report import running_balances, total


def test_total():
    assert total([100, -30, 80]) >= 0


def test_running_balances():
    assert running_balances([100, -30, 80])[-1] == 150
