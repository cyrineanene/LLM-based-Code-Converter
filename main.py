# main.py
from lib.Chunker import *
from lib.CodeParser import *
import warnings
from lib.utils import *

#Ignore the warning messages each time
warnings.filterwarnings("ignore", category=FutureWarning)

# code_path="code_samples/p1.py"
code_path="code_samples/p1.py"

def detect_lan(code_path):
        if code_path.endswith('.py'):
            return "py"
        elif code_path.endswith('.java'):
            return "java"
        

with open(code_path, 'r') as file:
    code=file.read()

parser = CodeParser([detect_lan(code_path)])
tree = parser.parse_code(code, detect_lan(code_path))
# points_of_interest = parser.extract_points_of_interest(tree, detect_lan(code_path))
grouped_nodes = parser.extract_points_of_interest_grouped(tree, "py")

# #testing the output
# for i in grouped_nodes:
#     print("\n",i)
# print("___________________________\n")
# for group in grouped_nodes:
#     print("\n",group)

  

tokenlimit=calculate_mean_token_count(code)
print(tokenlimit)

chunker = CodeChunker(file_extension=detect_lan(code_path), encoding_name='gpt-4')
chunks = chunker.chunk(code, token_limit=tokenlimit)
CodeChunker.print_chunks(chunks)