from options.domain import Option


def test_get_option_values(option_fixture):
    result = Option(**option_fixture["inputs"]).prices()

    assert result[0] == option_fixture["prices"]["call"]
    assert result[1] == option_fixture["prices"]["put"]


def test_get_option_pnl(option_fixture):
    purchase_price = 10
    option = Option(**option_fixture["inputs"], purchase_price=purchase_price)

    result = option.profit()

    assert result[0] == round(option_fixture["prices"]["call"] - purchase_price, 2)
    assert result[1] == round(option_fixture["prices"]["put"] - purchase_price, 2)


# def test_get_heatmap_figures(option_fixture):
#     """Generate a heatmap output"""

#     option = Option(**option_fixture["inputs"])

#     result = option.heatmap()

#     # construct 10x10 dataframe to compare to

#     # assert heatmap has call and put prices
#     # columns == price / volatility / call / put
