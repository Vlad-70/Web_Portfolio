import streamlit as st
import pandas
from stud_project_web.project_email import project_email

df = pandas.read_csv("topics.csv")

with st.form("email_form"):
    user_email = st.text_input("Your Email Address")
    selection = st.selectbox("What topic do you want to discuss?", df)
    user_message = st.text_area("Text")
    button = st.form_submit_button("Submit")

    message = f"""\

    From: {user_email}
    Topic: {selection}
    {user_message}
    """

    if button:
        project_email(message)
        st.info("Your email was sent successfully!")
