from utils.chunk_description import Description
from utils.chunk_translation import Translation
from utils.chunking import Chunker


#we will have to add a loop based on what the chunker will provide as an output!
#for now, i will just consider the output to be a list of chunks, and the chunker class gets the input full code
full_code = input('Enter the code: ')
chunks = Chunker(full_code).chunking() #the chunking method is to seperate the full code and return a list of chunks, i supposed there are no parameters

results = {chunk: [] for chunk in chunks}
for chunk in chunks:
    #Step 1: for each chunk, we will generate a description
    description = Description(chunk)
    result_description = description.output(description.get_code_description())

    #Step 2: for each chunk, we will translate/convert/give its equivalent in Java
    translated_code = Translation(chunk)
    tran = translated_code.get_code_translated(result_description) #TODO: i need to change the output method of description to return a string not a list
    
    #Step 3: for now, storing in a hashmap the necessary informations: {chunk_python: [description, chunk_java], ... }
    results[chunk].append(result_description)
    results[chunk].append(tran)