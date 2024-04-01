import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email")
    raw_message = st.text_area("You Message")
    message = =f"""\
    Subject: New email from {user_email}
    From: {user_email}
    {raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        #message = message + user_email
        #print(button)  # see what data type button is
        #print("I was pressed")
        send_email(message)
        st.info("Your email was sent successfully")



