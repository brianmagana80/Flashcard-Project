from database import get_questions 
from flashcards import study_session

study_session(get_questions)

# insert_history = ("""INSERT INTO history (question_id, attempt_result) 
#                      VALUES (%(question_id)s, %(attempt_result)s)""")

