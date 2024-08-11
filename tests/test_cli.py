from typer.testing import CliRunner

from options.cli import app

runner = CliRunner()


def test_cli(option_fixture):
    result = runner.invoke(
        app, [f"{item}" for item in option_fixture["inputs"].values()]
    )
    assert result.exit_code == 0
    assert "16.73" in result.stdout
    assert "7.22" in result.stdout


def test_cli_profit(option_fixture):
    """
    If a purchase price is supplied, provide current p&l for call and put
    """
    purchase_price = 10

    result = runner.invoke(
        app,
        [
            *[f"{item}" for item in option_fixture["inputs"].values()],
            "--purchase-price",
            f"{purchase_price}",
        ],
    )
    assert result.exit_code == 0
    assert (
        f'{round(option_fixture["prices"]["call"] - purchase_price,2)}' in result.stdout
    )
    assert (
        f'{round(option_fixture["prices"]["put"] - purchase_price, 2)}' in result.stdout
    )
