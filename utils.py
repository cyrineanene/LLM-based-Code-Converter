def save_to_temp_file(code):
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode='w') as temp_file:
        temp_file.write(code)
        return temp_file.name
    
def get_code(code_path): 
            with open(code_path, 'r') as file:
                generated_code = file.read()
            return generated_code

def execute_python_code(code):
    import io
    from contextlib import redirect_stdout, redirect_stderr
    
    #Step 1: Capture standard output and standard error
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    #Step 2: Execute python code
    try:
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                exec(code)
        return stdout_capture.getvalue()  
    except Exception as e:
        return 'Failed'
    
def execute_java_code(java_file_path):
    import os
    import subprocess

    class_name = os.path.splitext(os.path.basename(java_file_path))[0]
    run_result = subprocess.run(["java", "-cp", os.path.dirname(java_file_path), class_name], capture_output=True, text=True)
    
    if run_result.returncode == 0:
            return run_result.stdout 
    else:
            return 'Failed'