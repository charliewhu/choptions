# def test_option_price(option_fixture, streamlit_app):
#     # act
#     streamlit_app.number_input[0].input(option_fixture["inputs"]["current_price"])
#     streamlit_app.number_input[1].input(option_fixture["inputs"]["strike_price"])
#     streamlit_app.number_input[2].input(option_fixture["inputs"]["risk_free_rate"])
#     streamlit_app.number_input[3].input(option_fixture["inputs"]["days_to_expiry"])
#     streamlit_app.number_input[4].input(
#         option_fixture["inputs"]["annualized_volatility"]
#     ).run()

#     # assert
#     assert option_fixture["prices"]["call"] in streamlit_app.text

#     assert 1 == 0


from playwright.sync_api import expect


def test_playwright_runs(page):
    expect(page.get_by_text("Choptions")).to_be_visible()


def test_generate_prices(page, option_fixture):
    page.get_by_label("Current Price").fill(
        str(option_fixture["inputs"]["current_price"])
    )
    page.get_by_label("Strike Price").fill(
        str(option_fixture["inputs"]["strike_price"])
    )
    page.get_by_label("Days to Expiry").fill(
        str(option_fixture["inputs"]["days_to_expiry"])
    )
    page.get_by_label("Risk Free Rate").fill(
        str(option_fixture["inputs"]["risk_free_rate"])
    )
    page.get_by_label("Annualised Volatility").fill(
        str(option_fixture["inputs"]["annualised_volatility"])
    )

    # ensure page refresh on value change
    page.keyboard.press("Enter")

    expect(page.get_by_text(str(option_fixture["prices"]["call"]))).to_be_visible()
    expect(page.get_by_text(str(option_fixture["prices"]["put"]))).to_be_visible()
