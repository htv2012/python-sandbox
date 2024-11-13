import pandas as pd

import streamlit as st

st.title("Displays CSV")
df = pd.read_csv("favorites.csv")
df
