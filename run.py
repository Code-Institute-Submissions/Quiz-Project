import os
import json
from flask import Flask, redirect, render_template, request, flash, url_for


app = Flask(__name__)
app.secret_key = "some_secert"

def add_user(username):
    """
    Adds "Username" to Users
    """
    with open("data/users.txt", "a") as users:
        users.write("{0}\n".format(username))

def get_userlist():
    """
    Stops "Username" being used twice
    """
    user_list = []
    
    with open("data/users.txt", "r") as users:
        user_list = [user.strip("\n") for user in users]
        
    return user_list

def get_questions():
    """
    Gets "Questions" from json file
    """
    questions = []
    with open("data/questions.json", "r") as quiz_data:
        questions = json.load(quiz_data)
    return questions
    
def get_question_number():
    """
    Gets "Question Number" to start of quiz
    """
    questions = get_questions()
    question_number = questions[0]["index"]
    
    return question_number
    
def number_of_questions():
    """
    Gets "Number of Questions" for end of quiz and "score out of"
    """
    questions = get_questions()
    number_of_question = len(questions)
    
    return number_of_question
    
def get_question(question_number):
    """
    Gets "Question" for quiz using "Question Number"
    """
    questions = get_questions()
    for obj in questions:
        if obj["index"] == question_number:
            question = obj
            
    return question
    
def get_right_answer(question_number):
    """
    Gets correct answer to "Question"
     """
    questions = get_questions()
    answer = questions[question_number]["answer"]
    
    return answer
    
def get_choices(question_number):
    """
    Gets available "Choices" for "Question"
    """
    questions = get_questions()
    choices = questions[question_number]["choices"]
    
    return choices
    
def wrong_guesses_open(username):
    """
    Opens Wrong Guesses File and Wipes for next Question
    """
    with open("data/{0}_guesses.txt".format(username), "w") as guesses:
        guesses.write("")
    
def wrong_guess(username, guess, choices, wrong_guesses):
    """
    Adds incorrect guess to wrong guesses or shows alerts user it was invalid 
    """
    if guess in choices:
        with open("data/{0}_guesses.txt".format(username), "a") as guesses:
            guesses.write("{0}, ".format(guess))
    else:
        flash("Invalid Guess, Try Again!")
        
def get_wrong_guesses(username):
    """
    Gets Wrong Guess for User 
    """
    with open("data/{0}_guesses.txt".format(username), "r") as guesses:
        wrong_guesses = guesses.read()
        
        return wrong_guesses
        
def remove_wrong_guesses(username):
    """
    Removes wrong guesses file for user
    """
    os.remove("data/{0}_guesses.txt".format(username))

def add_to_scoreboard(username, score):
    """
    Adds Users score to scoreboard file
    """
    with open("data/scoreboard.json", "r+") as scoreboard:
        users = json.load(scoreboard)
        
    user = {}
    user["username"] = username
    user["score"] = score
    users.append(user)
    
    with open("data/scoreboard.json", "r+") as scoreboard:
        json.dump(users, scoreboard, indent=4)
            
def get_scoreboard():
    """
    Gets all scores and sorts them into highest first but Only Top 5
    """
    with open("data/scoreboard.json", "r") as scores:
        all_scores = json.load(scores)
        
    top_scores = sorted(all_scores, key=lambda x:x["score"], reverse=True)[:5]
    return top_scores

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Quiz Homepage with username entry and quiz start
    """
    question_number = get_question_number()
    users = get_userlist()
    
    if request.method == "POST":
        username = request.form["username"]
        if username in users:
            flash("The username '{0}' is unavailable, Try Again!".format(username))
        else:
            add_user(username)
            wrong_guesses_open(username)
            return redirect(url_for("quiz", username=username,
                                            question_number=question_number,
                                            score=0,
                                            guesses=3))
        
    return render_template("index.html", users=users)
    
@app.route("/<username>/<int:question_number>/<int:score>/<int:guesses>", methods=["GET", "POST"])
def quiz(username, question_number, score, guesses):
    """
    Playing Quiz steps through questions after a correct guess or 3 incorrect guesses
    """
    question = get_question(question_number)
    answer = get_right_answer(question_number)
    choices = get_choices(question_number)
    no_of_questions = number_of_questions()
    wrong_guesses = get_wrong_guesses(username)
   
    if request.method == "POST":
        # Checks guesses are above 1 to continue guessing question 
        if guesses != 1:
            guess = request.form["guess"].title()
            if guess != answer:
                wrong_guess(username, guess, choices, wrong_guesses)
                guesses -= 1
                flash("Incorrect!")
                return redirect(url_for("quiz", username=username,
                                                question_number=question_number,
                                                score=score,
                                                guesses=guesses,
                                                wrong_guesses=wrong_guesses))
            else:
                score += 1
                flash("Correct!")
                # End of questions 
                if question_number == (no_of_questions - 1):
                    add_to_scoreboard(username, score)
                    return redirect(url_for("quiz_end", username=username,
                                                            score=score))
                # Continue to Next Question
                else:
                    wrong_guesses_open(username)
                    return redirect(url_for("quiz", username=username,
                                                    score=score,
                                                    question_number=question_number+1,
                                                    guesses=3))
        # Last guess 
        else:
            guess = request.form["guess"].title()
            if guess != answer:
                flash("Next Question!")
                # End of questions 
                if question_number == (no_of_questions - 1):
                    add_to_scoreboard(username, score)
                    return redirect(url_for("quiz_end", username=username,
                                                            score=score))
                # Continue to Next Question
                else:
                    wrong_guesses_open(username)
                    return redirect(url_for("quiz", username=username,
                                                    score=score,
                                                    question_number=question_number+1,
                                                    guesses=3))
            else:
                score += 1
                flash("Correct!")
                # End of questions
                if question_number == (no_of_questions - 1):
                    add_to_scoreboard(username, score)
                    return redirect(url_for("quiz_end", username=username,
                                                            score=score))
                # Continue to Next Question
                else:
                    wrong_guesses_open(username)
                    return redirect(url_for("quiz", username=username,
                                                    score=score,
                                                    question_number=question_number+1,
                                                    guesses=3))
           
    return render_template("quiz.html", username=username,
                                        question=question,
                                        guesses=guesses,
                                        wrong_guesses=wrong_guesses,
                                        no_of_questions=no_of_questions)

@app.route("/quiz_end/<username>/<int:score>")
def quiz_end(username, score):
    """
    End of Quiz with Users score
    """
    no_of_questions = number_of_questions()
    remove_wrong_guesses(username)
    
    return render_template("quiz_end.html", username=username,
                                            score=score,
                                            no_of_questions=no_of_questions)

@app.route("/leaderboard")
def leaderboard():
    """
    Leaderboard shows Top 5 scores
    """
    top_scores = get_scoreboard()
    
    return render_template("leaderboard.html", leaderboard=top_scores)
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")))