class Description: 
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
        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=150, return_full_text=False, device=device)

        #integrating the LLM with langchain
        hf = HuggingFacePipeline(pipeline=pipe)
        return hf

    #Step 2: Define the function to generate the description
    def get_code_description(self):
        #organizing the prompt
        from langchain_core.prompts import PromptTemplate

        template = ("""I have a code snippet below. Answer the following questions in detail:
                1. Does it use libraries? If yes, list them.
                2. Does the code contain functions? If yes, list the functions and their purpose.
                3. What are the number of the inputs and outputs of this code?
                4. Does this code contain loops (for, while) and if-statements?

                Here is the code:
                ```
                {code}
                ```

                Please provide a detailed response.
                """)
        prompt = PromptTemplate.from_template(template)
        chain = prompt | self.initialize_model() 

        return chain.invoke(self.code)
    
    #Step3: optimize the output => a list containing in each index the response to a question
    def output(self, des):
        import re
        des = des[295:]
        regex_pattern = r"(\d+\.\s.*?)(?=\n\n|##|\n\d+\.|$)"
        items = re.findall(regex_pattern, des, re.DOTALL)
        separated_sentences = []
        split_sentences = re.split(r'\n?\s*\d+\.\s', items[0])
        split_sentences = [sentence for sentence in split_sentences if sentence]
        separated_sentences.extend(split_sentences)
        return separated_sentences

def full_describe(full_code):
    #This func will geenrate a description for the full code using a AST/graph-based approach and Llama3.2 as the LLM
    return 
#-----------------Testing the code---------------------------------------- would be removed when we move to main.py in the final version of the pipeline
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
print("Description of the code:")
print(description.output(des))