# Practical Python Project - The Quiz of All Things 

## Overview

### What is the Project?

This project is a Quiz Guessing Game where you can use a Player Name to make a unique game. The project is made using Python3 and Flask Framework.

### What can you do?

The project lets you choose a player name unless it is already taken. You start the Quiz with your player name and answer the questions in turn. Each question has 4 choices and you have 3 guesses, 
if you make a guess which is incorrect but is in the choices your guesses decrease by 1 and the wrong guess is display for you. If you make a guess thats not in the choices that is an invalid guess and
an error message will be displayed. If your guess is correct or you run out of guesses, you will proceed to the next question. A correct guess is worth 1 point otherwise you get nothing!

When the Quiz is finished you can see you score out of the questions provided. You can also head over to the leaderboard to see how you rank to other players and if you decide that you didn't score enough,
head back to the start and try again.

###  How does it function?

The project is made with Python 3 and the Flask framework which deals with the routing and file I/O.

(Add more about the function how username can't be used twice due to leaderboard, how the scoring works )

## Technology Used

- [Bootstrap](http://getbootstrap.com/)
    - **Bootstrap** is used to give a responsive layout.
- [Start Bootstrap](https://startbootstrap.com/)
    - **Start Bootstrap** is a site which provides themes and templates.
- [Flask](http://flask.pocoo.org/)
    - **Flask** is a microframework for Python.
 
## Testing

Testing can be found in [test_run.py](/test_run.py/)(add more tests for username and add to scoreboard)

(Add more about manual test and what type of progam tests I have done (test suite))

## References

### Content

The questions are based on information from a book called "Information is Beautiful" by David McCandless. 


