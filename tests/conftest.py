import pytest


@pytest.fixture
def option_fixture():
    return {
        "inputs": {
            "current_price": 100,  #  current asset price
            "strike_price": 100,  # strike price of the option
            "risk_free_rate": 0.1,  # risk free rate
            "days_to_expiry": 1,  #  time until option expiration
            "annualized_volatility": 0.3,  # annualized volatility of the asset's returns
        },
        "prices": {
            "call": 16.73,
            "put": 7.22,
        },
    }
