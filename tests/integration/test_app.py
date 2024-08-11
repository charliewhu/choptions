from playwright.sync_api import expect


def test_playwright_runs(page):
    expect(page.get_by_text("Choptions")).to_be_visible()


def test_generate_prices(
    page,
    option_fixture,
    input_initial_parameters,
):
    expect(page.get_by_text(str(option_fixture["prices"]["call"]))).to_be_visible()
    expect(page.get_by_text(str(option_fixture["prices"]["put"]))).to_be_visible()


def test_profit_and_loss(
    page,
    option_fixture,
    input_initial_parameters,
):
    purchase_price = 40

    page.get_by_label("Purchase Price").fill(f"{purchase_price}")
    page.keyboard.press("Enter")

    expect(
        page.get_by_text(f'{option_fixture["prices"]["call"] - purchase_price}')
    ).to_be_visible()
    expect(
        page.get_by_text(f'{option_fixture["prices"]["put"] - purchase_price}')
    ).to_be_visible()
