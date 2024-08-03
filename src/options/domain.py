import numpy as np
from scipy.stats import norm


class Option:
    def __init__(
        self,
        current_price: float,
        strike_price: float,
        risk_free_rate: float,
        days_to_expiry: int,
        annualized_volatility: float,
    ):
        self.current_price = current_price
        self.strike_price = strike_price
        self.risk_free_rate = risk_free_rate
        self.days_to_expiry = days_to_expiry
        self.annualized_volatility = annualized_volatility

    @staticmethod
    def N(x):
        return norm.cdf(x)

    def d1(self):
        return (
            np.log(self.current_price / self.strike_price)
            + (self.risk_free_rate + self.annualized_volatility**2 / 2)
            * self.days_to_expiry
        ) / (self.annualized_volatility * np.sqrt(self.days_to_expiry))

    def d2(self):
        return self.d1() - self.annualized_volatility * np.sqrt(self.days_to_expiry)

    def _call(self):
        return self.current_price * self.N(self.d1()) - self.strike_price * np.exp(
            -self.risk_free_rate * self.days_to_expiry
        ) * self.N(self.d2())

    def _put(self):
        return self.strike_price * np.exp(
            -self.risk_free_rate * self.days_to_expiry
        ) * self.N(-self.d2()) - self.current_price * self.N(-self.d1())

    def prices(self):
        return self._call(), self._put()
