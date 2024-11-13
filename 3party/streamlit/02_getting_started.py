import numpy as np
import pandas as pd

import streamlit as st

st.title("Getting Started")
st.write("### Table")
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)


"---\n### Use of Magic"

df = pd.DataFrame(
    {
        "UID": [501, 502, 503],
        "Alias": ["peter", "paul", "mary"],
    }
)

df

"---"
"### Line Chart"

if st.checkbox("Show Data Frame"):
    chart_data = pd.DataFrame(np.random.randn(30, 3), columns=["a", "b", "c"])

    st.line_chart(chart_data)


"---\n### Use Select Box"
option = st.selectbox("User:", df["Alias"])
f"Login as: {option}"
