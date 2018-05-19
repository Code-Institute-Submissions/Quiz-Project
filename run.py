import os
import json
from flask import Flask, redirect, render_template, request, flash, url_for

app = Flask(__name__)

def get_questions():
    
    questions = []
    with open("data/questions.json", "r") as quiz_data:
        questions = json.load(quiz_data)
    return questions
    
def get_question_number():
    
    questions = get_questions()
    question_number = questions[0]["index"]
    
    return question_number
    
def number_of_questions():
    
    questions = get_questions()
    number_of_question = len(questions)
    
    return number_of_question
    
def get_question(question_number):
    
    question = []
    with open("data/questions.json", "r") as quiz_data:
        questions = json.load(quiz_data)
        for obj in questions:
            if obj["index"] == question_number:
                question = obj
            
    return question
    
def get_right_answer(question_number):
    
    questions = get_questions()
    answer = questions[question_number]["answer"]
    
    return answer
    
def get_choices(question_number):
    
    questions = get_questions()
    choices = questions[question_number]["choices"]
    
    return choices



if __name__ == "__main__":
    app.run(host= os.environ.get("IP"),
    port= int(os.environ.get("PORT")),
    debug= True)