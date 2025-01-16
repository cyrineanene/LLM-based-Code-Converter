from src.description import Description, full_describe
from src.conversion import Conversion
from src.chunking import Chunker
from src.assembling import Assembler

#Step 1: Chunking the code
code_path="test_codes/RectangleAreaCalculator.py"
chunks = Chunker(code_path).chunking() 

results = {bloc_num: tuple() for bloc_num in chunks.keys()}

for bloc_num, chunk in chunks.items():
    #Step 2: Extracting and Generating the description for the global bloc's code
    block_description = full_describe(chunk[0])
    chunk.remove(chunk[0])
    translated_chunks = []
    for func in chunk:
        for element in func:
            #Step 3: Translate the chuck
            #TODO: in here we need to add that the for loop will be moving forward as long as the max_length is not exceeded
            translated_code = Conversion(chunk)
            tran = translated_code.get_code_conversion(block_description)
            translated_chunks.append(tran)
            
    #after the max_length reached and code translated
    
    #Step 4: for now, storing in a hashmap the necessary informations: {bloc_num: ('block_des', [[trans], ....])}
    results[bloc_num]+=(block_description,translated_chunks)

#Step 4: Assembling the code:
final_code = Assembler(results).assemble()