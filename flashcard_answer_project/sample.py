from transformers import pipeline
from PyPDF2 import PdfReader
import pandas as pd
import numpy as np
import torch
#
if torch.cuda.is_available():
        device = torch.cuda.current_device()
        print(f"GPU ({torch.cuda.get_device_name(device)}) is available and being used.")
else:
        print("No GPU available. Using CPU.")

data_dir = "Venuratech\\flashcards_project\\data\\NEET PREVIOUS YEAR  (2019) - Sheet1.csv"
pdf_dir = "C:\\Users\\rishi\\OneDrive\\Desktop\\projects\\Venuratech\\ncert_pdf\\lebo101.pdf"

# Load pre-trained model and tokenizer
qa_pipeline = pipeline('question-answering', model='distilbert-base-cased-distilled-squad', \
                        tokenizer='distilbert-base-cased-distilled-squad')

def get_answer(context, question):
    # Use the pre-trained model to get the answer
    result = qa_pipeline(context=context, question=question)
    answer = result['answer']
    return answer
def get_context_and_questions(data_dir):
    data = pd.read_csv(data_dir)
    questions = data['QUESTION'].values
    contexts = data['EXPLANATION'].values
    context = ''.join(list(contexts))
    questions= list(questions)
    return [context,questions]

def read_pdf(dir):
    reader = PdfReader(dir)
    #context = []
    #number_of_pages = len(reader.pages)
    #for i in range(number_of_pages):
    page = reader.pages[5]
    print(f"Extracting page no: {4+1}")
    text = page.extract_text()
    #context.append(text)
    print(f"content have been extracted")
    return text

# Example usage
#context_and_questions = get_context_and_questions(data_dir)
#context = context_and_questions[0]
#questions = context_and_questions[1]
#i = 1
#answers = []
#for question in questions:
#    answer = get_answer(context,question)
#    answers.append(answer)
#data = pd.read_csv(data_dir)
#data["model_generated_answers"] = pd.DataFrame(np.array(answers))
#data.to_csv(data_dir)
#print('saved')
context = read_pdf(pdf_dir)
question = "what is the capability of each cell in sprogenous tissue?"
question1 = "What is inside of microsporangium?"
question2 = "what happens when anthers mature and dehydrate?"
question3  = "The process of formation of microspores from a pollen mother cell is called as?"


print(context)
answer = get_answer(context,question)
answer1 = get_answer(context,question1)
answer2 = get_answer(context,question2)
answer3 = get_answer(context,question3)
print("\n QUESTION AND ANSWERS\n")
print(f"Q : {question}\nA : {answer}")
print(f"Q : {question1}\nA : {answer1}")
print(f"Q : {question2}\nA : {answer2}")     
print(f"Q : {question3}\nA : {answer3}")


print(read_pdf(pdf_dir))
