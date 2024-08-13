import pandas as pd
import streamlit as st


@st.cache_data
def draw_heatmap(matrix: pd.DataFrame):
    import plotly.express as px

    fig = px.imshow(
        matrix,
        labels=dict(
            x="Current Asset Price ($)",
            y="Volatility (σ)",
            color="Option Price",
        ),
        x=matrix.columns,
        y=matrix.index,
        aspect="auto",
        text_auto=True,
        origin="lower",
        color_continuous_scale=["red", "green"],
    )

    st.plotly_chart(fig, theme="streamlit")
