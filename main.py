import streamlit as st

if not st.experimental_user.is_logged_in:
    if st.button("Log in with Google"):
        st.login()
else:
    st.markdown(f"Welcome, {st.experimental_user.name}")
    st.write("This is the landing page you can head to the ROI page to play with the numbers")
    if st.button("Log out"):
        st.logout()

