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
