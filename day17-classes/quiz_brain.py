class QuizBrain:
  def __init__(self, questions_list):
    self.question_number = 0
    self.questions_list = questions_list
    self.score = 0

  def next_question(self):
    current_question = self.questions_list[self.question_number]
    self.question_number += 1
    submitted_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    self.check_answer(submitted_answer, current_question.answer)

  def still_has_questions(self):
    #this line below will return a boolean
    return self.question_number < len(self.questions_list)

  def check_answer(self, answer, correct_answer):
    if answer.lower() == correct_answer.lower():
      self.score += 1
      print(f"Correct! You now have {self.score}/{self.question_number} points")
    else:
      print(f"Sorry that's incorrect...The answer was {correct_answer}")