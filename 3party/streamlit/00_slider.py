import streamlit as st

st.write("# Slider Demo")
x = st.slider("slider")
st.write(x, "square is", x * x)
st.write(x, "cube is", x * x * x)
