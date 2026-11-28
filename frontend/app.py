from flask import Flask, render_template, request, redirect, url_for
from backend.database import get_questions, select_categories
import random

app = Flask(__name__)

# home page route
@app.route('/', methods=['GET', 'POST'])
def home():
    
    # creating category list for dropdown menu
    categories = []
    for i in select_categories():
        categories.append(i)
        
    # select category
    if request.method == "POST":
        selected_category = request.form["category"]
        
        return redirect(url_for('study', category=selected_category))
    return render_template('homepage.html', categories=select_categories())


# flashcard page route
@app.route('/study/<category>', methods=['GET', 'POST'])
def study(category):

    # filter through questions based on category
    questions = get_questions(category)

    question_index_number = 0
    result = None

    if request.method == "POST":
        # the question that is currently on screen (comes from the hidden input in studypage.html)
        question_index_number = int(request.form["question_number_index"])

        # "answer" is the name of the answer buttons in studypage.html. This only exists if an answer button was clicked.
        if "answer" in request.form:
            user_answer = request.form["answer"]
            
            #correct or incorrect logic
            if user_answer == questions[question_index_number][2]:
                result = "Correct!"
            else:
                result = "Incorrect!"

        # "next" is the name of the Next button in studypage.html. This only exists if the Next button was clicked.
        elif "next" in request.form:
            question_index_number += 1

    # no questions left, so the quiz is over
    if question_index_number >= len(questions):
        return render_template('finished.html', category=category)

    correct_answer = questions[question_index_number][2]
    
    answer_choices = [] 

    #random incorrect answer
    incorrect_answers = []
    for q in questions:
        incorrect_answers.append(q[2])
    incorrect_answers.remove(correct_answer)
    
    #shuffle 3 incorrect answers
    shuffled_incorrect_answers = random.sample(incorrect_answers, k=3)
    
    #randomize order of correct and incorrect answers
    answer_choices = [correct_answer] + shuffled_incorrect_answers
    random.shuffle(answer_choices)
    
    return render_template('studypage.html', questions=questions, answer_choices=answer_choices, result=result, category=category, question_index_number=question_index_number)


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
# cd "C:\Users\brian\OneDrive\Documents\GitHub\Flashcard Project"
# .\venv\Scripts\activate
# python -m frontend.app