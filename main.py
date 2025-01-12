# main.py
from lib.Chunker import *
from lib.CodeParser import *
import warnings

#Ignore the warning messages each time
warnings.filterwarnings("ignore", category=FutureWarning)

# code_path="code_samples/p1.py"
code_path="code_samples/p2.py"

def detect_lan(code_path):
        if code_path.endswith('.py'):
            return "py"
        elif code_path.endswith('.java'):
            return "java"
        

with open(code_path, 'r') as file:
    code=file.read()

parser = CodeParser([detect_lan(code_path)])
tree = parser.parse_code(code, detect_lan(code_path))
points_of_interest = parser.extract_points_of_interest(tree, detect_lan(code_path))
grouped_nodes = parser.extract_points_of_interest_grouped(tree, "py")

#testing the output
for i in points_of_interest:
    print("\n",i)
print("___________________________\n")
for group in grouped_nodes:
    print("\n",group)

# # determine the token limit
# from math import sqrt
# for i in points_of_interest:
#   m=0
#   node=i[0]
#   start=node.start_point
#   end=node.end_point
#   d=int(sqrt((start[0]+end[0])**2 + (start[1]+end[1])**2))
#   m = (m+d)/len(points_of_interest)

# tokenlimit=int(m/3)

# chunker = CodeChunker(file_extension=detect_lan(code_path), encoding_name='gpt-4')
# chunks = chunker.chunk(code, token_limit=tokenlimit)
# CodeChunker.print_chunks(chunks)