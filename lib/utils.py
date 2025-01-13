import tiktoken
import json

def count_tokens(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def load_json(json_file):
    with open(json_file) as f:
        return json.load(f)

import ast
import tokenize
from io import BytesIO

# Function to tokenize code and return the count of tokens
def count_tokens1(code):
    tokens = list(tokenize.tokenize(BytesIO(code.encode('utf-8')).readline))
    return len([token for token in tokens if token.type != tokenize.ENCODING and token.type != tokenize.NEWLINE])

# Function to traverse the AST up to the second level of nesting
def analyze_structure(node, depth=0):
    if depth > 2:  # Only analyze up to the second depth
        return 0
    
    # If the node is a logical structure (function, class, etc.)
    token_count = 0
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        # Get the code inside the node and tokenize it
        code = ast.unparse(node)
        token_count += count_tokens1(code)
    
    # Recurse for child nodes (to handle nesting)
    for child in ast.iter_child_nodes(node):
        token_count += analyze_structure(child, depth + 1)
    
    return token_count

# Function to calculate the mean token count of logical structures
def calculate_mean_token_count(code):
    tree = ast.parse(code)  # Parse the code into an AST
    total_tokens = 0
    structure_count = 0
    
    # Analyze each top-level structure
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            structure_count += 1
            total_tokens += analyze_structure(node)
    
    # Calculate mean token count
    if structure_count == 0:
        return 0  # Avoid division by zero if no structures found
    return total_tokens / structure_count
