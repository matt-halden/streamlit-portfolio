import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email")
    message = st.text_area("You Message")
    button = st.form_submit_button("Submit")
    if button:
        message = message + user_email
        print(button)  # see what data type button is
        print("I was pressed")

