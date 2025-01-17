class Assembler: 
    def __init__(self, generated_code, file_name):
        self.generated_code = generated_code
        self.file_name = file_name
    def assemble_java_code(self):
        if not self.file_name.endswith(".java"):
            self.file_name += ".java"
        try:
            with open(self.file_name, "a") as file:
                file.write("\n" + self.generated_code)  
                print(f"Java code appended to '{self.file_name}' successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")