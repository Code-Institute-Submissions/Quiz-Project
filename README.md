# Practical Python Project - The Quiz of All Things 

My project is a Quiz Guessing Game where you guess answers to questions about
all sorts of things. It's multiple choice so it should be easy, but don't let it
catch you out the answers aren't always as simple as you think. When you're done
don't forget to check out the leaderboard to see where you rank against your 
friends.

## UX

My project is designed to be fun and simple, users want to be excited to play and
can choose a name to play the quiz. The questions are different and interesting
with multiple choices and guesses so anyone can play. Users can also head over to
the leaderboard to see how you rank to other players.

As a User I would want:
- to use my own username for the game, so its unique to me
- to be told how the game works and any rules, so I know how to play
- to be entertained by the questions, to keep me entertained
- to have a range of different questions, to keep me interested
- to know what question I am in the game, so I know how many are left
- to see the answers clearly, so I can answer the question
- to know what answers I have picked, so I don't pick it twice
- to know how many guesses I have for a question, so I know how many are left
- my score to be recorded, to be able to view my score
- to be able to compare my score to other users, to see how well I did
- to be able to see the score of my last attempt, to compare to the highscores


Mock ups can be viewed for each page below:
- [Index](/mock-ups/Index.jpg)
- [Quiz](/mock-ups/Quiz.jpg/)
- [Leaderboard](/mock-ups/Leaderboard.jpg/)

## Features

### Existing Features

Currently these are the features that are implemented and how each feature 
provides UX:

- Userlist - allows user to create a player name
    - New Player - must be unique name    
- Quiz 
    - Multiple Choice - allows user to pick from 4 set choices 
    - Interactive Choices - allows user to click answer they want to guess
    - Wrong Guesses - informs user of previous wrong guesses
    - Question Number - informs user of question number
- Leaderboard - informs the user of their score and how it ranks against other players

### Planned Features

- Database
    - to store the data in a structured persistent database

## Technology Used

- [Python](https://www.python.org/)
    - **Python** is used to create the backend using Flask.
- [Flask](http://flask.pocoo.org/)
    - **Flask** is a microframework for Python.
- [Bootstrap](http://getbootstrap.com/)
    - **Bootstrap** is used to give a responsive layout.
- [Start Bootstrap](https://startbootstrap.com/)
    - **Start Bootstrap** is a site which provides themes and templates.
- [JQuery](https://jquery.com)
    - **JQuery** is used to give better UX.

## Testing

I developed the Quiz using Test Driven Development approach to build the Quiz 
in stages and testing each stage. For the testing I used Python Unit Test Framework
with a Test suite which can be found in [test_run.py](/tests/test_run.py/)

The tests can be run by using the following command:

    1. cd tests
    2. python3 test_run.py

As I developed the Quiz I did manual tests to check the Quiz was working as
designed and displaying correctly. They can be found in [User Tests](/tests/user_tests.md/).

I have also tested my project for responsiveness and on different browsers which
is detailed in [Browser Tests](/tests/browser_tests.pdf/)

## Deployment

### Heroku 

My project is deployed on [Heroku](https://www.heroku.com/) hosting platform and
can be viewed at [Quiz Of All Things](https://quiz-project-pp.herokuapp.com/)

When deploying the project I needed to:

- Include a Procfile which tells Heroku what type of app it is and what to run
- Include a requirements.txt to tell Heroku what dependencies need installing
- Scale the dynos which Heroku uses to help run apps
- Set the Config Vars for the IP, PORT

### Local

To run locally you need to clone the repository

    - git clone https://github.com/TMcNally17/Quiz-Project.git

You need to install the dependencies in requirements.txt 

    - pip install -r requirements.txt

Run the project

    - python3 run.py

## Credit

### Content

The questions are based on information from a book called "Information is Beautiful" by David McCandless. 