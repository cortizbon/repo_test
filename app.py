import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Esto es una app")

X = np.random.normal(0, 1, 1000)
Y = np.random.normal(0, 5, 1000)

tab1, tab2 = st.tabs(["Tab1", "Tab2"])

with tab1:
    fig, ax = plt.subplots(1, 1)
    ax.hist(X, bins=50, alpha=0.5, color='g')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    st.pyplot(fig)

with tab2:

    fig, ax = plt.subplots(1, 1)
    ax.hist(Y, bins=50, alpha=0.5, color='g')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    st.pyplot(fig)

    