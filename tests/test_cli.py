from typer.testing import CliRunner

from options.cli import app

runner = CliRunner()


def test_cli():
    result = runner.invoke(app, ["100", "100", "0.1", "1", "0.3"])
    assert result.exit_code == 0
    assert "16.73" in result.stdout
    assert "7.22" in result.stdout
