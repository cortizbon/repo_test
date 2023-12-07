import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import yfinance as yf

st.title("Esto es una app")

X = np.random.normal(0, 1, 1000)
Y = np.random.normal(0, 5, 1000)
e = np.random.normal(0, 1, 1000)

tesla = yf.ticker("TSLA")
tesla_data = tesla.history(period='max')['Close'].reset_index()

tab1, tab2, tab3 = st.tabs(["Tab1", "Tab2", "Tab3"])

with tab1:
    fig, ax = plt.subplots(1, 2, sharey=True)
    ax[0].hist(X, bins=50, alpha=0.5, color='g')
    ax[0].spines['right'].set_visible(False)
    ax[0].spines['top'].set_visible(False)
    ax[0].axvline(X.mean(), color='g')

    ax[1].hist(Y, bins=50, alpha=0.5, color='g')
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    ax[1].axvline(Y.mean(), color='g')

    st.pyplot(fig)

with tab2:

    fig, ax = plt.subplots(1, 1)
    ax.plot(e, color='k', alpha=0.6, ls='--')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.axhline(e.mean(), color='k')

    st.pyplot(fig)

with tab3:
    fig, ax = plt.subplots(1, 1)
    ax.plot(tesla_data['Date'], tesla_data['Close'], color='k', alpha=0.6, ls='--')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    st.pyplot(fig)

    