import typing as t
import typer

from options import domain

app = typer.Typer()


@app.command()
def get_option_prices(
    current_price: float,
    strike_price: float,
    risk_free_rate: float,
    days_to_expiry: int,
    annualised_volatility: float,
    purchase_price: t.Optional[float] = None,
):
    option = domain.Option(
        current_price,
        strike_price,
        risk_free_rate,
        days_to_expiry,
        annualised_volatility,
        purchase_price,
    )

    if purchase_price:
        print(option.profit())
        return

    print(option.prices())


def main():
    app()


if __name__ == "__main__":
    main()
