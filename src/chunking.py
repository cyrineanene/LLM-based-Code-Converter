# main.py
from lib.Chunker import *
from lib.CodeParser import *

class Chunker: 
    def __init__(self, code_path):
        self.code_path = code_path
    
    def chunking(self):
        import warnings

        #Ignore the warning messages each time
        warnings.filterwarnings("ignore", category=FutureWarning)

        def detect_lan(code_path):
                if code_path.endswith('.py'):
                    return "py"
                elif code_path.endswith('.java'):
                    return "java"
            
        with open(self.code_path, 'r') as file:
            code=file.read()

        parser = CodeParser([detect_lan(self.code_path)])
        tree = parser.parse_code(code, detect_lan(self.code_path))
        points_of_interest = parser.extract_points_of_interest(tree, detect_lan(self.code_path))
        grouped_nodes = parser.extract_points_of_interest_grouped(tree, "py")
        return(points_of_interest, grouped_nodes)
        #testing the output
        # for i in points_of_interest:
        #     print("\n",i)
        # print("___________________________\n")
        # for group in grouped_nodes:
        #     print("\n",group)