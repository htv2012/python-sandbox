import streamlit as st


def main():
    """Entry"""
    st.sidebar.text_input("Name: ", key="name")
    contact_method = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home Phone", "Mobile Phone"),
    )
    lower_limit, upper_limit = st.sidebar.slider(
        "Filter by range", 0.0, 100.0, (25.0, 75.0)
    )

    st.title("Items Search (Sidebar Demo)\n")
    st.write(f"Hello {st.session_state.name},")

    st.write(f"Item range is from \${lower_limit} to \${upper_limit}")
    st.write(f"You will be contacted via {contact_method.lower()}")


if __name__ == "__main__":
    main()
