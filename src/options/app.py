import streamlit as st

from options import domain
from options.heatmap import draw_heatmap

st.set_page_config(page_title="Choptions")

st.markdown("# Choptions")

c1, c2, c3, c4, c5 = st.columns(5)

with st.sidebar:
    st.markdown("## Market Parameters")
    current_price = st.number_input(
        label="Current Price",
        value=100,
        min_value=0,
    )
    strike_price = st.number_input(
        label="Strike Price",
        value=100,
        min_value=0,
    )
    risk_free_rate = st.number_input(
        label="Risk Free Rate",
        value=0.1,
        min_value=0.0,
        max_value=1.0,
        step=0.01,
    )
    annualised_volatility = st.number_input(
        label="Annualised Volatility",
        value=0.3,
        min_value=0.0,
        max_value=1.0,
        step=0.01,
    )
    days_to_expiry = int(
        st.number_input(
            label="Days to Expiry",
            value=365,
            min_value=0,
        )
    )

    st.divider()

    st.markdown("## Profit Parameters")

    purchase_price = st.number_input(
        label="Purchase Price",
        min_value=0.0,
        step=0.1,
    )

inputs = [
    current_price,
    strike_price,
    risk_free_rate,
    days_to_expiry,
    annualised_volatility,
]

option: domain.Option | None = None

if all([x if x is not None else 0 for x in inputs]):
    option = domain.Option(
        current_price,
        strike_price,
        risk_free_rate,
        days_to_expiry,
        annualised_volatility,
    )

    prices = option.prices()

    st.markdown("### Current Modelled Price")

    price1, price2 = st.columns(2)
    with price1:
        st.markdown("##### Call")
        st.info(prices[0])

    with price2:
        st.markdown("##### Put")
        st.info(prices[1])

    st.divider()

    st.markdown("#### Call Price Matrix")
    draw_heatmap(option.call_matrix())

    st.markdown("#### Put Price Matrix")
    draw_heatmap(option.put_matrix())

    st.divider()

if option and purchase_price:
    st.markdown("### Current Profit / Loss")
    option.purchase_price = purchase_price
    profit = option.profit()

    profit1, profit2 = st.columns(2)

    with profit1:
        if profit[0] > 0:
            st.success(profit[0])
        else:
            st.error(profit[0])

    with profit2:
        if profit[1] > 0:
            st.success(profit[1])
        else:
            st.error(profit[1])

    st.markdown("#### Long Call Profit Matrix")
    draw_heatmap(option.call_matrix() - purchase_price)

    st.markdown("#### Long Put Profit Matrix")
    draw_heatmap(option.put_matrix() - purchase_price)
