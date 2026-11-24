from ledger.report import total


def test_total():
    assert total([100, -30, 80]) == 150
