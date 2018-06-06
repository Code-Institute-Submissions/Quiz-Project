import unittest
import run

class test_quiz(unittest.TestCase):
    
    # Test suite
    
    def test_get_questions(self):
        
        # Test to get questions from question file
        
        questions = run.get_questions()
        self.assertEqual((questions[0]), {
           "index": 0,
           "number": 1,
           "question": "What is the capital of the Austria?",
           "choices": ["Paris", "Vienna", "Prague", "Venice"],
           "answer": "Vienna"
            })
        self.assertNotIn("question 4", questions)
        
    def test_get_question_number(self):
        
        # Test to get question number to start of quiz
        
        question_number = run.get_question_number()
        
        self.assertEqual(question_number, 0)
        
    def test_get_question(self):
        
        # Test that get question with the question number will return correct question
        
        question = run.get_question(0)
        
        self.assertEqual(question, {
            "index": 0,
            "number": 1,
            "question": "What is the capital of the Austria?",
            "choices": ["Paris", "Vienna", "Prague", "Venice"],
            "answer": "Vienna"
            })
    
    def test_get_right_answer(self):
        
        # Test to get the right answer to question using question number
        
        answer = run.get_right_answer(0)
        answer_1 = run.get_right_answer(1)
        
        self.assertEqual(answer, "Vienna")
        self.assertNotEqual(answer_1, "Germany")
        
        
    def test_get_choices(self):
        
        # Test to get the choices to question using question number
        
        choices = run.get_choices(0)
        
        self.assertEqual(choices, ["Paris", "Vienna", "Prague", "Venice"])
        self.assertNotEqual(choices, ["Germany", "Belgium", "Croatia", "Switzerland"])
        
    
    def test_right_answer(self):
        
        # Test that right answer to question will increase score by 1
        
        answer = run.get_right_answer(0)
        guess = "Vienna"
        
        self.assertEqual(answer, guess)