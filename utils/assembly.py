class Assembler: 
    def __init__(self, results):
        self.results = results
    def assemble(self):
        final_code = f"""
        """
        for chunk in self.results.values():
            chunk.remove(chunk[0])
            for element in chunk:
                final_code+=element
        return final_code