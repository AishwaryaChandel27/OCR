import streamlit as st
import requests

# Function to set theme
def set_theme(theme):
    if theme == "Light":
        st.markdown("""<style>body { background-color: #ffffff; color: #000000; }</style>""", unsafe_allow_html=True)
    else:
        st.markdown("""<style>body { background-color: #1e1e1e; color: #ffffff; }</style>""", unsafe_allow_html=True)

# Sidebar settings
st.sidebar.title("Settings")
theme = st.sidebar.selectbox("Choose Theme", ("Light", "Dark"))
set_theme(theme)

st.title("OCR App")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    files = {'image': uploaded_file}

    # POST request to Flask backend
    try:
        response = requests.post("http://127.0.0.1:5000/upload", files=files)
        if response.status_code == 200:
            extracted_text = response.json().get("result", "")
            st.subheader("Extracted Text:")
            st.text_area("Output", extracted_text, height=200)
        else:
            st.write("Error:", response.json().get("error", "Unknown error occurred"))
    except requests.exceptions.ConnectionError:
        st.write("Failed to connect to the server. Is the Flask app running?")

# Keyword search
if 'extracted_text' in locals():
    st.subheader("Keyword Search")
    keyword = st.text_input("Enter a keyword to search:")
    if keyword:
        if keyword.lower() in extracted_text.lower():
            st.success(f"Keyword '{keyword}' found!")
        else:
            st.error(f"Keyword '{keyword}' not found.")

# Sidebar options
st.sidebar.subheader("Additional Features")
if st.sidebar.button("Clear Output"):
    st.text_area("Output", "", height=200)

if st.sidebar.button("About"):
    st.sidebar.info("This app uses OCR to extract text from images.")
