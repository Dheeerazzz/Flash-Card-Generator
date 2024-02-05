from transformers import pipeline
from PyPDF2 import PdfReader
import pandas as pd
import numpy as np
import torch

if torch.cuda.is_available():
        device = torch.cuda.current_device()
        print(f"GPU ({torch.cuda.get_device_name(device)}) is available and being used.")
else:
        print("No GPU available. Using CPU.")


questions_dir = "C:\\Users\\rishi\\OneDrive\\Desktop\\projects\\Venuratech\\Flash-Card-Generator\\files\\generated_questions.csv"
context_dir = "C:\\Users\\rishi\\OneDrive\\Desktop\\projects\\Venuratech\\Flash-Card-Generator\\flashcard_answer_project\\processed_reproduction.txt"

qa_pipeline = pipeline('question-answering', model='distilbert-base-cased-distilled-squad', \
                        tokenizer='distilbert-base-cased-distilled-squad')
qa_pipeline1 = pipeline('question-answering', model='deepset/roberta-base-squad2', \
                        tokenizer='deepset/roberta-base-squad2')

def read_context(context_dir):
    text_file = open(context_dir, "r")
    text = text_file.read()
    return text


def get_answer(context, question):
    # Use the pre-trained model to get the answer
    result = qa_pipeline(context=context, question=question)
    answer = result['answer']
    return answer

def get_answer_1(context,question):
    result = qa_pipeline(context=context, question=question)
    answer = result['answer']
    return answer

def save_answers(context_dir,questions_dir):
    context = read_context(context_dir)
    print(context)
    df = pd.read_csv(questions_dir)
    questions = df.values.flatten()[15:]
    questions_saved=[]
    distilbert_answers = []
    roberta_answers = []
    for question in questions:
        #print(question)
        answer = get_answer(context,question)
        answer_1 = get_answer_1(context,question)
        questions_saved.append(question)
        distilbert_answers.append(answer)
        roberta_answers.append(answer_1)
        print(f"Que : {question}\nD_A : {answer}\nR_A : {answer_1}")
        dic = {
             'questions' : np.array(questions_saved),
            'distilbert_answers' : np.array(distilbert_answers),
            'roberta_answers' : np.array(roberta_answers)
        }
        pd.DataFrame(dic).to_csv("C:\\Users\\rishi\\OneDrive\\Desktop\\projects\\Venuratech\\Flash-Card-Generator\\files\\generated_answers.csv")
        print("answer saved")

    return "All are saved"

print(save_answers(context_dir,questions_dir))
#print(read_context(context_dir))

