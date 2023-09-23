#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 18:11:20 2023

@author: saravananveeramani
"""
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import Dividends as lib

st.set_page_config(page_title="Fundamental Analysis App", layout="wide")



ticker = st.text_input("Stock name", key="ticker",value="AAPL")


st.header("{}".format(lib.getStockName(ticker)))

# Row #1
row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
    (0.1, 1, 0.1, 1, 0.1)
)

with row3_1:
    st.subheader("Dividends")
    df= lib.getDividends(ticker)
    fig = px.bar(
            df,
            x="year",
            y="Dividends",
            title="Dividends Read by Year",
            color_discrete_sequence=["#85e698"],
        )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    st.markdown(lib.dividend_desc)

with row3_2:
    st.subheader("EPS ")
    df = lib.getTicker(ticker)
    result_df = lib.formatIncomeStmtData(df.income_stmt)

    fig = px.bar(
                result_df,
                x="year",
                y="Basic EPS",
                title="EPS by Year",
                text_auto=True,
                color_discrete_sequence=["#c681eb"],
            )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    st.markdown(lib.eps_desc)

# Row # 2


row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns(
    (0.1, 1, 0.1, 1, 0.1)
)


with row4_1:
    st.subheader("Revenue")
    df = lib.getTicker(ticker)
    result_df = lib.formatIncomeStmtData(df.income_stmt)

    fig = px.bar(
                result_df,
                x="year",
                y="Total Revenue",
                title="Revenue over the Year",
                text_auto=True,
                color_discrete_sequence=["#81c1eb"],
            )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    st.markdown("Yearly Income statement")

with row4_2:
    st.subheader("Net Income")
    df = lib.getTicker(ticker)
    result_df = lib.formatIncomeStmtData(df.income_stmt)

    fig = px.bar(
                result_df,
                x="year",
                y="Net Income",
                title="Net Income over the Year",
                text_auto=True,
                color_discrete_sequence=["#e6859c"],
            )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    st.markdown("Yearly Income statement")
