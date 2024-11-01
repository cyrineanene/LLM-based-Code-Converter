#Defining the class of the description to facilitate its integration later in the global main program
class Description: 
    def __init__(self, code):
        self.code = code

    #Step 1: Initialize the model
    def initialize_model(checkpoint = "model starcoder/"):
        import torch
        torch.cuda.empty_cache()
        from transformers import AutoModelForCausalLM, AutoTokenizer

        checkpoint = "model starcoder/"
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
        return tokenizer, model, device

    #Step 2: Define the function to generate the description
    def get_code_description(self):
        prompt = f"""I have a code snippet below. Answer the following questions in detail:
        1. What does this code do?
        2. Does it use libraries? If yes, list them.
        3. Does the code contain functions? If yes, list the functions and their purpose.
        4. What are the inputs and outputs of this code?

        Here is the code:
        ```
        {self.code}
        ```

        Please provide a detailed response.
        """
        tokenizer, model, device = self.initialize_model()
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        
        generate_ids = model.generate(
        inputs.input_ids,
        max_length= (inputs.input_ids.shape[1]) * 1.75,
        attention_mask=inputs.attention_mask, 
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
        temperature=0.1,
        do_sample=True
    )
        return tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]