import streamlit as st

# set layout of page/format it correctly
st.set_page_config(layout="wide")

# get col1, 2 as object instances
col1, col2 = st.columns(2)

# open column
with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Matt Halden")
    content = """
    Hey, I am Matt Halden.
    I like dogs.
    """
    st.info(content)