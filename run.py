import os
import json
from flask import Flask, redirect, render_template, request, flash, url_for

app = Flask(__name__)
app.secret_key = "some_secert"

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

def wrong_guess(username, guess, choices, wrong_guesses):
    
    if guess in choices:
        wrong_guesses.append(guess)
    else:
        flash("Invalid Guess, Try Again!")

    return wrong_guesses

def set_scoreboard(username, question_number, score):
    
    with open("data/{0}.txt".format(username), "a") as user_file:
        user_file.writelines("({0}) Question {1}: {2}\n".format(
            username,
            (question_number + 1),
            score))
    
@app.route("/", methods=["GET", "POST"])
def index():
    
    # Quiz Homepage with username entry
    question_number = get_question_number()
    
    if request.method == "POST":
        username = request.form["username"]
        with open("data/users.txt", "a") as users:
            users.writelines(username + "\n")
        return redirect(url_for("quiz", username=username, question_number=question_number))
        
    return render_template("index.html")
    
@app.route("/<username>/<int:question_number>", methods=["GET", "POST"])
def quiz(username, question_number):
    
    question = get_question(question_number)
    answer = get_right_answer(question_number)
    choices = get_choices(question_number)
    wrong_guesses = []
   
   
    if request.method == "POST":
        guess = request.form["guess"].title()
        if guess == answer:
            score = 1
            set_scoreboard(username, question_number, score)
            if question_number == 2:
                return redirect("/leaderboard")
            else:
                return redirect(url_for("quiz", username=username, question_number=question_number+1))
        elif guess != answer:
           
            wrong_guess(username, guess, choices, wrong_guesses)
        else:
            score = 0
            set_scoreboard(username, question_number, score)
            if question_number == 2:
                return redirect("/leaderboard")
            else:
                return redirect(url_for("quiz", username=username, question_number=question_number+1))
        
            
    return render_template("quiz.html", username=username, question=question, wrong_guesses=wrong_guesses)
    
@app.route("/leaderboard")
def leaderboard():
    
    return render_template("leaderboard.html")



if __name__ == "__main__":
    app.run(host= os.environ.get("IP"),
    port= int(os.environ.get("PORT")),
    debug= True)