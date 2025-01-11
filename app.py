import streamlit as st
import subprocess

# Set the page layout to wide mode for full-width columns
st.set_page_config(layout="wide")

# Title of the app
st.title("Code Translator & Executor")

# Define conversion options
input_options = ["Python", "Java"]
conversion_options = ["None", "Python", "Java"]

# Create two columns that will take up the full width of the screen
col1, col2 = st.columns([1, 1])  # Both columns will take equal space, summing up to the entire screen

# Code input section (left side)
with col1:
    st.header("Input Code")
    conversion_type = st.selectbox("Select input type", input_options)
    input_code = st.text_area(f"Paste your code here", height=430)

# Code conversion section (right side)
with col2:
    st.header("Converted Code")
    conversion_type = st.selectbox("Select conversion type", conversion_options)
    converted_code = ""
    
    if input_code:
        if conversion_type == "Python":
            # Simple conversion logic (This can be more complex)
            converted_code = input_code.replace("print", "# Bash equivalent comment")
        elif conversion_type == "Java":
            converted_code = input_code.replace("print", "console.log")
        else:
            converted_code = input_code
        
        # Inject custom CSS to make the code area scrollable and keep the navbar sticky at the top
        st.markdown("""
        <style>
        .code-container {
            position: relative;
            height: 445px;
            overflow-y: scroll;
            padding: 0px;
            white-space: pre-wrap;
            background-color: #f5f5f5;
            border-radius: 5px;
            font-family: 'Ariel', monospace;
        }

        .navbar {
            position: sticky;  /* Sticky navbar */
            top: 0;  /* Ensure it sticks at the top */
            left: 0;
            right: 0;
            background-color: #f5f5f5;
            color: #333;
            padding: 10px 20px;
            font-size: 14px;
            font-family: 'Ariel', monospace;
            z-index: 1;  /* Keep navbar on top of the code */
            display: flex;
            justify-content: space-between;  /* Align text to the left and button to the right */
            align-items: center;  /* Vertically align the content in the navbar */
        }

        .navbar button {
            backgroun-color: #f5f5f5; 
            color: #333;
            border: none;
            border-radius: 5px;
            padding: 5px 10px;
            cursor: pointer;
            font-size: 14px;
            display: flex;
            align-items: center;
        }

        .navbar button span {
            margin-left: 5px;
        }

        .navbar button:hover {
            color: black;
        }

        </style>
        """, unsafe_allow_html=True)
        
        # Create a container with the converted code and a copy button in the navbar
        st.markdown(f'''
        <div class="code-container">
            <div class="navbar">
                <span>{conversion_type}</span>
                <button onclick="navigator.clipboard.writeText(document.getElementById('converted_code').textContent)">
                    <span>&#x2398;</span>  <!-- Clipboard icon -->
                    <span>Copy Code</span>
                </button>
            </div>
            <pre id="converted_code">{converted_code}</pre>
        </div>
        ''', unsafe_allow_html=True)
