class Description: 
    def __init__(self, code):
        self.code = code

    #Step 1: Initialize the LLM
    def initialize_model(self, checkpoint = "llama3.2-3b-instruct/"):
        print('Initializing the LLM just started')
        from langchain_huggingface.llms import HuggingFacePipeline
        from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

        import torch
        torch.cuda.empty_cache()
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        model_id = checkpoint
        print('Initializing the tokenizer')
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        print('Initializing the model')
        model = AutoModelForCausalLM.from_pretrained(model_id).to(device)
        print('Initializing the pipe')
        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=350, return_full_text=False, device=0 if torch.cuda.is_available() else -1)
        hf = HuggingFacePipeline(pipeline=pipe)
        print('Initializing the LLM just ended')
        return hf

    #Step 2: Define the function to generate the description
    def get_code_description(self):
        print('Code description just started')
        from langchain_core.prompts import PromptTemplate

        template = ("""I have a code snippet below. Answer the following questions in detail:
                1. Does it use libraries? If yes, list them.
                2. Does the code contain functions? If yes, list the functions and their purpose.
                3. What are the number of the inputs and outputs of this code? Respond in a tuple format.
                4. Does this code contain loops (for, while) and if-statements?

                Here is the code:
                ```
                {code}
                ```

                Please provide a detailed response.
                """)
        prompt = PromptTemplate.from_template(template)
        print('Getting the prompt ended')
        chain = prompt | self.initialize_model() 
        print('Starting on the chain')
        ch = chain.invoke(self.code)
        print('Code description just ended')
        return ch
    
    #Step3: optimize the output => a list containing in each index the response to a question
    def output(self, des):
        import re
        regex_pattern = r"(\d+\.\s.*?)(?=\n\n|##|\n\d+\.|$)"
        items = re.findall(regex_pattern, des, re.DOTALL)
        separated_sentences = []
        split_sentences = re.split(r'\n?\s*\d+\.\s', items[0])
        split_sentences = [sentence for sentence in split_sentences if sentence]
        separated_sentences.extend(split_sentences)
        return separated_sentences
    
#------------- FOR TESTING THE CLASS -------------    
# code_snippet = '''
# def calculate_area(length, width):
#     return length * width

# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = calculate_area(length, width)
# print(f"The area of the rectangle is: {area}")
#     '''
# description= Description(code_snippet)
# des = description.get_code_description()
# print("Description of the code:" + des)
# #print(description.output(des))