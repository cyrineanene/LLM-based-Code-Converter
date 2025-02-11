from src.description import Description
from src.conversion import Conversion
from src.comparaison import Comparaison
import json
from utils import save_to_temp_file, get_code

def main(input_code):
    describer_input = Description(input_code)
    converter = Conversion(input_code)
    
    # Step 1: Generate description of the input code
    input_description = describer_input.get_code_description()
    input_code_path = save_to_temp_file(input_code)
    
    while True:
        # Step 2: Convert the code
        converted_code = converter.get_code_conversion(input_description)
        generated_code_path = save_to_temp_file(converted_code)
        
        # Step 3: Generate description of the converted code
        describer_generated = Description(converted_code)
        converted_description = describer_generated.get_code_description()
        
        # Step 4: Compare the descriptions
        comparer = Comparaison(input_code_path, generated_code_path, input_description, converted_description)
        comparaison_score = comparer.compare_codes()
        
        if comparaison_score == True:  
            return json.dumps({
                "converted_code": converted_code,
                "comparaison_score": comparaison_score
            })
        else:
            print("Conversion did not retain enough similarity, reconverting the code.") 

if __name__ == "__main__":
    import sys
    input_code = get_code('test_codes/RectangleAreaCalculator.py')
    result = main(input_code)
    print(result)




# #Step 1: Chunking the code
# code_path="test_codes/RectangleAreaCalculator.py"
# chunks = Chunker(code_path).chunking() 

# results = {bloc_num: tuple() for bloc_num in chunks.keys()}

# for bloc_num, chunk in chunks.items():
#     #Step 2: Extracting and Generating the description for the global bloc's code
#     block_description = full_describe(chunk[0])
#     chunk.remove(chunk[0])
#     translated_chunks = []
#     for func in chunk:
#         for element in func:
#             #Step 3: Translate the chuck
#             #TODO: in here we need to add that the for loop will be moving forward as long as the max_length is not exceeded
#             translated_code = Conversion(chunk)
#             tran = translated_code.get_code_conversion(block_description)
#             translated_chunks.append(tran)
            
#     #after the max_length reached and code translated
    
#     #Step 4: for now, storing in a hashmap the necessary informations: {bloc_num: ('block_des', [[trans], ....])}
#     results[bloc_num]+=(block_description,translated_chunks)

# #Step 4: Assembling the code:
# final_code = Assembler(results).assemble()