class Conversion: 
    def __init__(self, code):
        self.code = code

    #Step 1: Initialize the LLM
    def initialize_model(self, checkpoint = "LLMs/starcoder"):
        print('Initializing the conversion LLM just started')
        from langchain_huggingface.llms import HuggingFacePipeline
        from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

        import torch
        torch.cuda.empty_cache()
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        model_id = checkpoint
        print('Initializing the conversion tokenizer')
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        print('Initializing the conversion model')
        model = AutoModelForCausalLM.from_pretrained(model_id).to(device)
        print('Initializing the conversion pipe')
        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=350, return_full_text=False, device=0 if torch.cuda.is_available() else -1)
        hf = HuggingFacePipeline(pipeline=pipe)
        print('Initializing the conversion LLM just ended')
        return hf

    #Step 2: Define the function to generate the description
    def get_code_conversion(self, description):
        print('Code conversion just started')
        from langchain_core.prompts import PromptTemplate

        template = ("You are an expert code translator with deep knowledge of programming paradigms, syntax, and best practices in multiple programming languages. "
            
            "### Input Description: "
            "A brief description of the overall code's purpose and functionality is provided to give context. Use this to guide the translation process."
            "{description} "
            "### Input Python Code: "
            "A Python code snippet is provided for translation."
            "{code} "

            "### Output: "
            "Provide the equivalent Java code snippet, maintaining structure, clarity, and function."
            
            )
        
        prompt = PromptTemplate.from_template(template)
        print('Getting the prompt ended')
        chain = prompt | self.initialize_model() 
        print('Starting on the chain')
        ch = chain.invoke({'description':description, 'code':self.code})
        print('Code conversion just ended')
        return ch
    
#------------- FOR TESTING THE CLASS -------------    
# code_snippet = '''
# def calculate_area(length, width):
#     return length * width

# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = calculate_area(length, width)
# print(f"The area of the rectangle is: {area}")
#     '''
# des = ['No, it does not use any libraries.', 'No, it does not contain any functions.', 'The number of inputs is 2 and the number of outputs is 1.', 'No, it does not contain any loops or if-statements.']
# translated_code = Conversion(code_snippet)
# tran = translated_code.get_code_conversion(des)
# print("The code translated to Java:" + tran)