import streamlit as st
import subprocess

# Set the page layout to wide mode for full-width columns
st.set_page_config(layout="wide")

# Title of the app
st.title("Code Translator & Executor")

# Sidebar instructions
st.sidebar.title("Instructions")
st.sidebar.write("""
1. Paste your code in the left text box.
2. Select the desired conversion type.
3. View the converted code on the right side.
4. Press 'Run' to execute the code and see the output below.
""")

# Define conversion options
input_options = ["Python", "Java"]
conversion_options = ["None", "Python", "Java"]

# Create two columns that will take up the full width of the screen
col1, col2 = st.columns([1, 1])  # Both columns will take equal space, summing up to the entire screen

# Code input section (left side)
with col1:
    st.header("Input Code")
    conversion_type = st.selectbox("Select input type", input_options)
    input_code = st.text_area(f"## Paste your code here", height=430)

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
        
        # Inject custom CSS to make the code area scrollable and to position the Copy button
        st.markdown("""
        <style>
        .code-container {
            position: relative;
            height: 400px;
            overflow-y: scroll;
            white-space: pre-wrap;
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
        }

        .copy-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 5px 10px;
            cursor: pointer;
            font-size: 14px;
        }

        .copy-btn:hover {
            background-color: #45a049;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Create a container with the converted code and a copy button
        st.write("Converted Code:")
        st.markdown(f'''
        <div class="code-container">
            <button class="copy-btn" onclick="navigator.clipboard.writeText(document.getElementById('converted_code').textContent)">Copy Code</button>
            <pre id="converted_code">{converted_code}</pre>
        </div>
        ''', unsafe_allow_html=True)

# Input for variables
st.subheader("Enter Variables (for Execution, optional)")
variables = st.text_area("Enter any variables for execution (e.g., 'name=John')", height=100)

# Run code section
if st.button("Run Code"):
    if conversion_type == "None":
        # Save the original Python code and run it
        with open("uploaded_script.py", "w") as f:
            f.write(input_code)
        
        try:
            result = subprocess.run(
                ["python3", "uploaded_script.py", variables], 
                text=True, capture_output=True
            )
            st.subheader("Execution Output")
            st.text(result.stdout)
            if result.stderr:
                st.text("Error:")
                st.text(result.stderr)
        except Exception as e:
            st.error(f"Error while running the script: {e}")
    else:
        # Run converted code as Bash or JavaScript (for demo purposes)
        with open("converted_script.sh", "w") as f:
            f.write(converted_code)
        
        if conversion_type == "Python":
            try:
                result = subprocess.run(
                    ["bash", "converted_script.sh"], 
                    text=True, capture_output=True
                )
                st.subheader("Bash Script Output")
                st.text(result.stdout)
                if result.stderr:
                    st.text("Error:")
                    st.text(result.stderr)
            except Exception as e:
                st.error(f"Error while running the Bash script: {e}")
        
        elif conversion_type == "Java":
            # For JavaScript, let's execute with Node.js
            with open("converted_script.js", "w") as f:
                f.write(converted_code)
            
            try:
                result = subprocess.run(
                    ["node", "converted_script.js"], 
                    text=True, capture_output=True
                )
                st.subheader("JavaScript Execution Output")
                st.text(result.stdout)
                if result.stderr:
                    st.text("Error:")
                    st.text(result.stderr)
            except Exception as e:
                st.error(f"Error while running the JavaScript code: {e}")
