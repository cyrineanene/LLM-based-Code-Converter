# main.py
from lib.Chunker import *
from lib.CodeParser import *

code_path="code_samples/csample.py"

def detect_lan(code_path):
        if code_path.endswith('.py'):
            return "py"
        elif code_path.endswith('.java'):
            return "java"
        

with open(code_path, 'r') as file:
    code=file.read()


chunker = CodeChunker(file_extension=detect_lan(code_path), encoding_name='gpt-4')
chunks = chunker.chunk(code, token_limit=1)
CodeChunker.print_chunks(chunks)

parser = CodeParser([detect_lan(code_path)])
tree = parser.parse_code(code, detect_lan(code_path))
points_of_interest = parser.extract_points_of_interest(tree, detect_lan(code_path))

for i in points_of_interest:
  print("\n",i)