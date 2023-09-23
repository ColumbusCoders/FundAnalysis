#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 18:37:17 2023

@author: saravananveeramani
"""
import yfinance as yf


dividend_desc = "Dividends are a portion of a company's profits that it distributes to its shareholders. They are typically paid out regularly, usually on a quarterly basis, and are a way for investors to receive a share of the company's earnings as cash payments"
eps_desc = "Earnings Per Share (EPS) is a measure of a company's profitability that tells you how much profit it has generated for each outstanding share of its stock. It's calculated by dividing the company's total earnings by the number of shares available to the public. EPS helps investors gauge a company's financial performance and is a key factor in evaluating its stock's value and potential for growth"


# Get dividends data 
def getDividends(ticker):
    tkr = yf.Ticker(ticker)
    div_data = tkr.dividends.to_frame()
    div_data['year'] = div_data.index
    return div_data.tail(40)

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


