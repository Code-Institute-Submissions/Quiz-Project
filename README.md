# Practical Python Project - The Quiz of All Things 

## Overview

### What is the Project?

My project is a Quiz Guessing Game where you can use a Player Name to make a unique game. The project is made using Python3 and Flask Framework.

### What can you do?

My project lets you choose a player name unless it is already taken. You start the Quiz with your player name and answer the questions in turn. Each question has 4 choices and you have 3 guesses, 
if you make a guess which is incorrect but is in the choices your guesses decrease by 1 and the wrong guess is display for you. If you make a guess thats not in the choices that is an invalid guess and
an error message will be displayed. If your guess is correct or you run out of guesses, you will proceed to the next question. A correct guess is worth 1 point otherwise you get nothing!

When the Quiz is finished you can see you score out of the questions provided. You can also head over to the leaderboard to see how you rank to other players and if you decide that you didn't score enough,
head back to the start and try again.

###  How does it function?

My project uses the Flask framework to deal with the Routing and file I/O. From the Homepage the user enters a username to play the quiz. The username is used to make a unique quiz for each user,
therefore it can not be used twice. The username is entered on a userlist and if another user tries to use the same name the quiz will alert the user that the username is unavailable. The quiz uses
the username to personalise the quiz page, also is used to create unique files for wrong guesses and scoreboard entry. The quiz uses a counter to increment the score as the user guesses the correct answer
and scoreboard stores each users score at the end of the quiz with the username and score as values. The leaderboard is sorted into the top five scores and is displayed in a table using the username and score.

## Technology Used

- [Bootstrap](http://getbootstrap.com/)
    - **Bootstrap** is used to give a responsive layout.
- [Start Bootstrap](https://startbootstrap.com/)
    - **Start Bootstrap** is a site which provides themes and templates.
- [Flask](http://flask.pocoo.org/)
    - **Flask** is a microframework for Python.
 
## Testing

I developed the Quiz using Test Driven Development approach to build the Quiz in stages and testing each stage. For the testing I used Python Unit Test Framework with a Test suite 
which can be found in [test_run.py](/test_run.py/)

As I developed the Quiz I did manual tests to check the Quiz was working as designed and displaying it correctly. I had to test the scoring manually as the score is incremented through routing
to the next question and is only stored at the end of the of Quiz. 

## References

### Content

The questions are based on information from a book called "Information is Beautiful" by David McCandless. 