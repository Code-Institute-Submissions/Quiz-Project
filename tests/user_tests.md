### User Testing

As I deployed a new feature, I did manual tests to check the UI and UX worked as expected.
Below is a list of features and the tests I carried out:

- Create New Player
    - On homepage or navigate to Start
    - Try submit with empty player name and required input error stops submit
    - Try submit with player name already in user list and submit displays error message "The username 'player name' is unavailable, Try Again!"
    - Try submit with player name that is not in user list and submits redirects user to Quiz

- Guessing
    - On Quiz page
    - Try make a guess with empty input and required input error stops submit
    - Try make a guess not using the choices and submit displays error message "Invalid Guess, Try Again!"
    - Try make a guess by clicking on a choices and submit will check choice against answer 
    - Wrong answer will display message "Incorrect" and decrease guesses by 1
    - Wrong answer with one guess remaining with redirect user to next question and display message "Next Question"
    - Right answer will redirect to next question and display message "Correct"
    
- Interactive Choices
    - On Quiz page
    - Clicking on a choice will fill guess text
    - Clicking on another choice will change guess text to new answer

- Wrong Guesses
    - On Quiz page
    - Try making a guess not using the choices and submit will not add to wrong guesses
    - Try making a guess with a wrong answer and submit will put wrong answer will be added to wrong guesses

- Question Number
    - On Quiz page
    - Question number will increase as user answers question to inform user of progress
 
- User Score
    - On Quiz End page
    - Users score is displayed to inform them of how well they did

- Leaderboard
    - On Leaderboard page
    - User can compare their score to leaderboard and see where they rank