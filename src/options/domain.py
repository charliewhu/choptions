import typing as t

import numpy as np
import pandas as pd
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
        return self._call(), self._put()

    def profit(self):
        if self.purchase_price is None:
            raise ValueError()

        prices = self.prices()

        return tuple(round(price - self.purchase_price, 2) for price in prices)

    def _matrix(self, index: t.Literal[0, 1]):
        # min + max prices
        # min + max volatilities
        # create option with min values
        # loop to produce prices for each
        # change the prices and vol in loop
        num_rows_cols = 9
        tolerance = 0.1
        tolerances = (-tolerance, tolerance)

        min_price, max_price = (self.current_price * (1 + i) for i in tolerances)
        min_vol, max_vol = (self.annualised_volatility * (1 + i) for i in tolerances)

        price_range = np.linspace(min_price, max_price, num=num_rows_cols)
        vol_range = np.linspace(min_vol, max_vol, num=num_rows_cols)

        option = Option(
            current_price=min_price,
            strike_price=self.strike_price,
            risk_free_rate=self.risk_free_rate,
            days_to_expiry=self.days_to_expiry,
            annualised_volatility=min_vol,
        )

        # prices = np.zeros((num_rows_cols, num_rows_cols))
        prices = pd.DataFrame(
            index=np.round(vol_range, 5),
            columns=np.round(price_range, 2),
        )

        for vol in vol_range:
            option.annualised_volatility = vol

            for price in price_range:
                option.current_price = price
                prices.loc[
                    np.round(vol, 5),
                    np.round(price, 2),
                ] = option.prices()[index]

        return prices

    def call_matrix(self):
        return self._matrix(index=0)

    def put_matrix(self):
        return self._matrix(index=1)
