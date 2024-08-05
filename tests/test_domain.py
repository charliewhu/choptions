from options.domain import Option


def test_get_option_values(option_fixture):
    result = Option(**option_fixture["inputs"]).prices()

    assert result[0] == option_fixture["prices"]["call"]
    assert result[1] == option_fixture["prices"]["put"]


def test_get_option_pnl(option_fixture):
    purchase_price = 10
    option = Option(**option_fixture["inputs"], purchase_price=purchase_price)

    result = option.profit()

    assert result[0] == option_fixture["prices"]["call"] - purchase_price
    assert result[1] == option_fixture["prices"]["put"] - purchase_price
