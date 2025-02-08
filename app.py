import gradio as gr
import subprocess

def convert_code(input_code):
    try:
        #after completing the convert.py, the test.py will simply need to be updated by main.py
        result = subprocess.run(["python", "test.py"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

with gr.Blocks() as demo:
    gr.Markdown("# Code Converter")
    with gr.Row():
        input_box = gr.Textbox(lines=10, label="Input Code")
        output_box = gr.Textbox(lines=10, label="Converted Code", interactive=False)
    convert_button = gr.Button("Convert")
    convert_button.click(convert_code, inputs=input_box, outputs=output_box)

demo.launch(share=True)