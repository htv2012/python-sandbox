import pathlib

import pandas as pd
import streamlit as st


def create_filter(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    choices = ["All"] + sorted(df[column_name].unique())
    print(f"{choices=}")
    choice = st.selectbox(column_name, choices)
    if choice != "All":
        df = df.loc[df[column_name] == choice]
    return df


def main():
    """Entry"""
    st.header("Pens and Papers Collection")

    db_path = pathlib.Path(__file__).with_name("data.csv")
    df = pd.read_csv(db_path)

    st.subheader("Filters")

    # category = st.selectbox("Category", ["All"] + list(df["Category"].unique()))
    # if category != "All":
    #     df = df.loc[df["Category"] == category]
    df = create_filter(df, "Category")
    # df = create_filter(df, "Brand")
    brand = st.selectbox("Brand", ["All"] + list(df["Brand"].unique()))
    if brand != "All":
        df = df.loc[df["Brand"] == brand]

    # df = create_filter(df, "Nib Size")

    # choices = ["All"] + sorted(df["Retailer"].unique())
    # retailer = st.selectbox("Retailer", choices)
    # if retailer != "All":
    #     df = df.loc[df["Retailer"] == retailer]
    df = create_filter(df, "Retailer")

    st.subheader("Result")
    df


if __name__ == "__main__":
    main()
