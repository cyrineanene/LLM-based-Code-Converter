#Comparaing the input and the generated/converted codes
#this comparaison will be based on a syntax/compilation score and a similarity score on both descriptions of the codes
from utils import get_code
from utils import execute_python_code, execute_java_code

class Comparaison: 
    def __init__(self, input_code_path, generated_code_path, description_input, description_generated):
        self.input_code_path = input_code_path
        self.generated_code_path = generated_code_path
        self.description_input = description_input
        self.description_generated = description_generated
    
    #Couldn't be done because of the lack of inputs, but we could add the llm to generate an input for the code 
    # def execution_comparaison(self):
    #     #Step 1: Extracting the code from the file
    #     generated_code = get_code(self.generated_code_path)
    #     input_code = get_code(self.input_code_path)
        
    #     #Step 2: Running both codes, return the output of the code if sucess and 'Failed' if not
    #     executed_python = execute_python_code(input_code)
    #     executed_java = execute_java_code(self.generated_code_path)
    #     if executed_python == 'Failed' or executed_java == 'Failed':
    #         execution_score = 0
    #     elif executed_python == executed_java:
    #         execution_score = 1
    #     return execution_score
    
    def syntax_compilation_comparaison(self):
        import subprocess
        import tempfile

        #Step 1: Extracting the code from the file
        generated_code = get_code(self.generated_code_path)
        
        #Step 2: Verifying the syntax/compilation of the generated code
        with tempfile.NamedTemporaryFile(suffix=".java", delete=False) as temp_file:
            temp_file.write(generated_code.encode())
            java_file_path = temp_file.name

        try:
            result = subprocess.run(["javac", java_file_path], capture_output=True, text=True)
            if result.returncode == 0:
                syntax_score = 1
            else:
                syntax_score = 0
                #error = result.stderr
        finally:
            subprocess.run(["rm", java_file_path])
        
        #Step 3: Returning 1 if the compilation is successful and 0 if not 
        return syntax_score
    
    def similarity_comparaison(self):
        #this step will be based on the results of the bleu, meteor, rouge and the bert score
        #after considering the use case and the format of the descriptions, the rouge score and meteor are chosen as well as the bertscore with weights as follows: 
        # 1/3 for rouge and meteor,  and 2/3 for bertscore 
        #Why? => 1. Since the descriptions are factual and structured, ROUGE will help assess how well the structures of the two descriptions align in terms of shared phrases or key concepts.
        # 2. METEOR is useful because we need to compare descriptions that might use different terms or phrasing for the same concepts.
        # 3. BERTScore is the most powerful metric here, as it takes into account the semantic meaning behind the words. It will help assess how closely the two descriptions match in meaning, even if their wording differs.
        import nltk
        from nltk.translate.meteor_score import meteor_score
        from rouge_score import rouge_scorer
        from bert_score import score
        nltk.download('punkt')
        scores_questions = list()
        
        #Step 1: Calculating the scores for each question in the desscription
        for i in range(0,4):
            des_1 = self.description_input[i]
            des_2 = self.description_generated[i]

            #Step 2: Calculating the ROUGE Score
            rouge_scorer_obj = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
            rouge_scores = rouge_scorer_obj.score(des_2, des_1)
            rouge_score = rouge_scores['rougeL'].fmeasure()

            #Step 3: Calculating the meteor score
            meteor = meteor_score([des_2], des_1)

            #Step 4: Calculating the bertscore
            P, R, F1 = score([des_1], [des_2], lang="en")
            bertscore = F1.mean().item()

            #Step 5: Appending the average score corresponding to each question
            scores_questions.append((rouge_score + meteor)/3 + (bertscore*2) / 3)

        #Step 6: Calculating hte overall similarity score
        similarity_score = sum(scores_questions) / len(scores_questions)

        #Step 7: Making the similarity decision based on a 85% resemblance
        threshold = 0.85
        if similarity_score >= threshold:
            return True, similarity_score
        else:
            return False, similarity_score
        
    def compare_codes (self):
        #If the multiplication is not 0 then they are similar with a score of their multiplication/2
        if self.syntax_compilation_comparaison()*self.similarity_comparaison()[1] != 0:
            return True, (self.syntax_compilation_comparaison()*self.similarity_comparaison()[1])/2
        return False, 'Not Similar'