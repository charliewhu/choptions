import typer

from options import domain

app = typer.Typer()


@app.command()
def get_option_prices(
    current_price: float,
    strike_price: float,
    risk_free_rate: float,
    days_to_expiry: int,
    annualized_volatility: float,
):
    prices = domain.Option(
        current_price,
        strike_price,
        risk_free_rate,
        days_to_expiry,
        annualized_volatility,
    ).prices()

    print(prices)


def main():
    app()


if __name__ == "__main__":
    main()
