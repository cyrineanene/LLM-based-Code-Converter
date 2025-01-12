import pyperclip
import streamlit as st
from utils import convert_code
import os

# Set the page layout to wide mode for full-width columns
st.set_page_config(layout="wide")

# Load custom CSS
def load_css():
    css_file_path = "assets/styles.css"
    if os.path.exists(css_file_path):
        with open(css_file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS
load_css()

# Title of the app
st.title("Code Translator & Executor")

# Define conversion options
conversion_options = ["None", "Python", "Java"]

# Create two columns that will take up the full width of the screen
col1, col2 = st.columns([1, 1])

# Code input section (left side)
with col1:
    st.header("Input Code")
    conversion_type = st.selectbox("Select conversion type", conversion_options)
    input_code = st.text_area(f"Paste your code here", height=430)

# Code conversion section (right side)
with col2:
    st.header("Converted Code")
    st.write("")
    converted_code = ""

    if input_code:
        converted_code = convert_code(input_code, conversion_type)
        
        # Create a container with the converted code and a copy button in the navbar
        st.markdown(f'''
        <div class="code-container">
            <div class="navbar">
                <span>{conversion_type}</span>
                <div class="button-container">
                    <button onclick="navigator.clipboard.writeText(document.getElementById('converted_code').textContent)">
                        <span>&#x2398;</span>  <!-- Clipboard icon -->
                        <span>Copy Code</span>
                    </button>
                </div>
            </div>
            <pre id="converted_code">{converted_code}</pre>
        </div>
        ''', unsafe_allow_html=True)

        st.write("")
        # File Download button
        st.download_button(
            label="Download Code",
            data=converted_code,
            file_name="converted_code.txt",
            mime="text/plain"
        )
