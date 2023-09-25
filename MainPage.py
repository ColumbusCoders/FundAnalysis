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
import yfinance as yf
import pandas as pd


# Functions Starts

dividend_desc = "Dividends are a portion of a company's profits that it distributes to its shareholders. They are typically paid out regularly, usually on a quarterly basis, and are a way for investors to receive a share of the company's earnings as cash payments"
eps_desc = "Earnings Per Share (EPS) is a measure of a company's profitability that tells you how much profit it has generated for each outstanding share of its stock. It's calculated by dividing the company's total earnings by the number of shares available to the public. EPS helps investors gauge a company's financial performance and is a key factor in evaluating its stock's value and potential for growth"



# Get dividends data
def getStockDividends(ticker):
    tkr = yf.Ticker(ticker)
    div_data = tkr.get_dividends()
    return div_data.tail(20)


# Get stock data
def getTicker(ticker):
    tkr = yf.Ticker(ticker)
    return tkr

def getStockName(ticker):
    tkr = yf.Ticker(ticker)
    return tkr.info['longName']

# format income statement parameter dataframe.
def formatIncomeStmtData(df):
    result_df = df.T
    result_df['year'] = result_df.index
    return result_df

# Functions End


st.set_page_config(page_title="Fundamental Analysis App", layout="wide")



ticker = st.text_input("Stock name", key="ticker",value="AAPL")


st.header("{}".format(getStockName(ticker)))

tab1, tab2, tab3,tab4 = st.tabs(["Key Data","Income Statement", "Balance Sheet", "Cash Flow"])
with tab1:

    row1_space1, row1_1, row1_space2, row1_2, row1_space3 = st.columns(
        (0.1, 1, 0.1, 1, 0.1)
    )
    with row1_1:
        st.subheader("Profit Margins")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.income_stmt)
        result_df['NPM'] = (result_df['Net Income'] / result_df['Total Revenue']) * 100
        fig = px.bar(
                    result_df,
                    x="year",
                    y="NPM",
                    title="Net Profit Margins",
                    text_auto=True,
                    color_discrete_sequence=["#81c1eb"],
                )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    with row1_2:
        st.subheader("EPS ")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.income_stmt)

        fig = px.bar(
                    result_df,
                    x="year",
                    y="Basic EPS",
                    title="EPS by Year",
                    text_auto=True,
                    color_discrete_sequence=["#c681eb"],
                )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

        st.markdown(eps_desc)
    row1_space2, row2_1, row2_space2, row2_2, row2_space3 = st.columns(
            (0.1, 1, 0.1, 1, 0.1)
        )
    with row2_1:
        st.subheader("Dividends ")
        tkr = getTicker(ticker)
        div_data = tkr.get_dividends()
        df = div_data.tail(20)
        fig = px.bar(
                        df,
                        x=df.index,
                        y="Dividends",
                        title="Dividends by Year",
                        text_auto=True,
                        color_discrete_sequence=["#c681eb"],
                    )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

        st.markdown(eps_desc)


with tab2:

    # Row #1
    row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
        (0.1, 1, 0.1, 1, 0.1)
    )

    with row3_1:
        st.subheader("Revenue")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.income_stmt)

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


    with row3_2:

        st.subheader("Net Income")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.income_stmt)

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


    # Row # 2


    row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns(
        (0.1, 1, 0.1, 1, 0.1)
    )


    with row4_1:
        st.subheader("Operating Expense")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.income_stmt)

        fig = px.bar(
                    result_df,
                    x="year",
                    y="Operating Expense",
                    title="Operating Expense by Year",
                    text_auto=True,
                    color_discrete_sequence=["#e66e65"],
                )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    with row4_2:
        st.subheader("EPS ")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.income_stmt)

        fig = px.bar(
                    result_df,
                    x="year",
                    y="Basic EPS",
                    title="EPS by Year",
                    text_auto=True,
                    color_discrete_sequence=["#c681eb"],
                )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

        st.markdown(eps_desc)

    # Row # 2


    row5_space1, row5_1, row5_space2, row5_2, row5_space3 = st.columns(
        (0.1, 1, 0.1, 1, 0.1)
    )

    with row5_1:
        st.subheader("Gross Profit ")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.income_stmt)

        fig = px.bar(
                    result_df,
                    x="year",
                    y="Gross Profit",
                    title="Profit by Year",
                    text_auto=True,
                    color_discrete_sequence=["#c681eb"],
                )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

        st.markdown(eps_desc)

    with st.expander("Reference Data"):
        df=getTicker(st.session_state.ticker ).incomestmt
        st.dataframe(df.style.highlight_max(axis=1),use_container_width=True)

with tab3:
    # Row #1
    row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
        (0.1, 1, 0.1, 1, 0.1)
    )

    with row3_1:
        st.subheader("Assets")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.balancesheet)

        fig = px.bar(
                    result_df,
                    x="year",
                    y="Total Assets",
                    title="Total Assets over the Year",
                    text_auto=True,
                    color_discrete_sequence=["#1aab6c"],
                )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        st.markdown("Yearly Income statement")

    with row3_2:
        st.subheader("Liabilities")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.balancesheet)

        fig = px.bar(
                    result_df,
                    x="year",
                    y="Total Liabilities Net Minority Interest",
                    title="Total Liabilities over the Year",
                    text_auto=True,
                    color_discrete_sequence=["#db831f"],
                )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        st.markdown("Yearly Income statement")
    # Row #2
    row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns(
        (0.1, 1, 0.1, 1, 0.1)
    )

    with row4_1:
        st.subheader("Liabilities Vs Equity ")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.balancesheet)

        fig = go.Figure(data=[
            go.Bar(name='Liabilities', x=result_df['year'], y=result_df["Total Liabilities Net Minority Interest"]),
            go.Bar(name='Equity', x=result_df['year'], y=result_df["Common Stock Equity"])
        ])
        fig.update_layout(barmode='stack')

        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        st.markdown("Yearly Income statement")


    with st.expander("Reference Data"):
        df=getTicker(st.session_state.ticker ).balancesheet
        st.dataframe(df.style.highlight_max(axis=1),use_container_width=True)

    with row4_2:
        st.subheader("Equity")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.balancesheet)

        fig = px.bar(
                    result_df,
                    x="year",
                    y="Common Stock Equity",
                    title="Equity over the Year",
                    text_auto=True,
                    color_discrete_sequence=["#42230b"],
                )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        st.markdown("Yearly Income statement")
    # Row #2
    row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns(
        (0.1, 1, 0.1, 1, 0.1)
    )

with tab4:
    # Row #1
    row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
        (0.1, 1, 0.1, 1, 0.1)
    )

    with row3_1:
        st.subheader("Cashflow")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.cashflow)

        fig = px.bar(
                    result_df,
                    x="year",
                    y="Free Cash Flow",
                    title="Free Cashflow over the Year",
                    text_auto=True,
                    color_discrete_sequence=["#bfdb1f"],
                )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        st.markdown("Yearly Income statement")

    with row3_2:
        st.subheader("Change in Cash")
        df = getTicker(ticker)
        result_df = formatIncomeStmtData(df.cashflow)

        fig = px.bar(
                    result_df,
                    x="year",
                    y="Changes In Cash",
                    title="Free Cashflow over the Year",
                    text_auto=True,
                    color_discrete_sequence=["#dbc81f"],
                )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        st.markdown("Yearly Income statement")

    with st.expander("Reference Data"):
        df=getTicker(st.session_state.ticker ).cashflow
        st.dataframe(df.style.highlight_max(axis=1),use_container_width=True)
