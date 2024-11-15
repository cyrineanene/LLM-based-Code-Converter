class Translation: 
    def __init__(self, code):
        self.code = code

    #Step 1: Initialize the model
    def initialize_model(checkpoint = "model starcoder/"):
        #working on the initialzation of the model
        from langchain_huggingface.llms import HuggingFacePipeline
        from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

        #workign on the gpu
        import torch
        torch.cuda.empty_cache()
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        #initalizing the tokenizer and the LLM
        model_id = checkpoint
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(model_id)

        #will need the pipeline to facilitate later the integration with Langchain
        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=200, return_full_text=False, device=device)

        #integrating the LLM with langchain
        hf = HuggingFacePipeline(pipeline=pipe)
        return hf

    #Step 2: Define the function to generate the description
    def get_code_translated(self,description):
        #prompt verison 3
        #organizing the prompt
        from langchain_core.prompts import PromptTemplate

        template = (
            "You are an expert code translator with deep knowledge of programming paradigms, syntax, and best practices in multiple programming languages. "
            "Your task is to accurately translate a Python code snippet into Java. Adhere to the following guidelines:"
            "1. Accuracy: Ensure the functionality of the Python code is preserved in the Java code. "
            "2. Idiomacy: Write the Java code using idiomatic constructs typical of Java, such as proper use of classes, methods, type annotations, and exception handling. "
            "3. Optimization: Optimize the Java code for readability and performance while maintaining its core functionality. "
            "4. Comments: Include concise comments to explain any differences between Python and Java implementations, especially for constructs that do not directly map between the two languages. "
            "5. Error Handling: Ensure that the Java code includes appropriate error handling if applicable. "
            "6. Code Structure: Organize the Java code logically, adhering to Java conventions such as proper use of public static void main(String[] args) for executable programs. "
            
            "### Input Description: "
            "A brief description of the code's purpose and functionality is provided to give context. Use this to guide the translation process."
            "{description} "
            "### Input Python Code: "
            "A Python code snippet is provided for translation."
            "{code} "

            "### Output: "
            "Provide the equivalent Java code snippet, maintaining structure, clarity, and function. Include explanatory comments where necessary."

            "Translate the given Python code based on the provided description."

                )
        prompt = PromptTemplate.from_template(template)
        chain = prompt | self.initialize_model() 

        return chain.invoke({'description':description, 'code':self.code})

#-----------------Testing the code---------------------------------------- would be removed when we move to main.py in the final version of the pipeline
from chunk_description import Description     

code_snippet = '''
def calculate_area(length, width):
    return length * width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")
    '''

description = Description(code_snippet)
des = description.get_code_description()
des =description.output(des)

translated_code = Translation(code_snippet)
tran = translated_code.get_code_translated(des)
print("The code translated to Java:" + tran)