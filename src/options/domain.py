import numpy as np
from scipy.stats import norm


class Option:
    def __init__(
        self,
        current_price: float,
        strike_price: float,
        risk_free_rate: float,
        days_to_expiry: int,
        annualised_volatility: float,
        purchase_price: float | None = None,
    ):
        self.current_price = current_price
        self.strike_price = strike_price
        self.risk_free_rate = risk_free_rate
        self.days_to_expiry = days_to_expiry
        self.annualised_volatility = annualised_volatility
        self.purchase_price = purchase_price
        self.years_to_expiry = days_to_expiry / 365

    @staticmethod
    def N(x):
        return norm.cdf(x)

    def d1(self) -> float:
        return (
            np.log(self.current_price / self.strike_price)
            + (self.risk_free_rate + self.annualised_volatility**2 / 2)
            * (self.years_to_expiry)
        ) / (self.annualised_volatility * np.sqrt(self.years_to_expiry))

    def d2(self) -> float:
        return self.d1() - self.annualised_volatility * np.sqrt(self.years_to_expiry)

    def _call(self) -> float:
        call = self.current_price * self.N(self.d1()) - self.strike_price * np.exp(
            -self.risk_free_rate * self.years_to_expiry
        ) * self.N(self.d2())
        return round(call, 2)

    def _put(self) -> float:
        put = self.strike_price * np.exp(
            -self.risk_free_rate * self.years_to_expiry
        ) * self.N(-self.d2()) - self.current_price * self.N(-self.d1())
        return round(put, 2)

    def prices(self):
        return float(self._call()), float(self._put())

    def profit(self):
        if self.purchase_price is None:
            raise ValueError()

        prices = self.prices()

        return tuple(round(price - self.purchase_price, 2) for price in prices)
