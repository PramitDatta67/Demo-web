import streamlit as st 
st.title("Welcome to my website")
st.header("python")
st.subheader("java") 
st.markdown("I love Python") 
st.code("""
def greet(name):
    return f"Hello, {name}!"
""", language="python")

import streamlit as st
import pandas as pd

st.title("Upload and View Excel Sheet 📄")

# Upload file
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")
    st.dataframe(df)
st.title("User Information Form")


with st.form(key="user_form"):
    name = st.text_input("Your Name")
    dad_name = st.text_input("Father's Name")
    address = st.text_area("Address")
    contact = st.text_input("Contact Number")

    submit = st.form_submit_button("Submit")

    if submit:
        st.success("Form Submitted Successfully ✅")
        st.write("### Submitted Information:")
        st.write(f"**Name:** {name}")
        st.write(f"**Father's Name:** {dad_name}")
        st.write(f"**Address:** {address}")
        st.write(f"**Contact No:** {contact}")