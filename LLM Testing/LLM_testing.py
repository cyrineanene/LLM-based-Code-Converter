#Step 1: Connect to HuggingFace
from huggingface_hub import login
import os
from dotenv import load_dotenv
load_dotenv()
huggingface_token = os.getenv("Huggingface")
login(token= huggingface_token)

#Step 2: StarCoder
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

checkpoint = "LLM Testing/model starcoder/"
device = 'cuda' if torch.cuda.is_available() else 'cpu'

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

input_text = "Translate the following function to python :\n function add(a, b) { return a + b; }"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)

outputs = model.generate(input_ids)
print(tokenizer.batch_decode(outputs, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0])
#print(tokenizer.decode(outputs[0]))