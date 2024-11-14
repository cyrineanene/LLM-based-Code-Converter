from Chunker import *
from CodeParser import *
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")
# Set logging level to WARNING to ignore INFO and DEBUG logs
logging.basicConfig(level=logging.WARNING)

code= ''' class Calculator:
    def __init__(self, name):
        self.name = name

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b
'''
#chunker = CodeChunker(file_extension='java', encoding_name='gpt-4')
#chunks = chunker.chunk(code, token_limit=10)
#CodeChunker.print_chunks(chunks)

parser = CodeParser(['py'])
tree = parser.parse_code(code, 'py')
points_of_interest = parser.extract_points_of_interest(tree, 'py')

for i in points_of_interest:
  print("\n",i)