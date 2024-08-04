from options.domain import Option


def test_get_option_values():
    initial_params = {
        "current_price": 100,  #  current asset price
        "strike_price": 100,  # strike price of the option
        "risk_free_rate": 0.1,  # risk free rate
        "days_to_expiry": 1,  #  time until option expiration
        "annualized_volatility": 0.3,  # annualized volatility of the asset's returns
    }

    call_price = 16.73
    put_price = 7.22

    result = Option(**initial_params).prices()

    assert result[0] == call_price
    assert result[1] == put_price
