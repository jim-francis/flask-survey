from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "nge4ev"

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_homepage():
    survey_title = survey.title
    survey_instructions = survey.instructions
    return render_template('home.html', survey_title=survey_title, survey_instructions=survey_instructions)

@app.route('/question/<question_id>')
def ask_question(question_id):
    # question_to_ask = satisfaction_survey.questions
    question_id = len(responses)
    question = survey.questions[question_id]
    return render_template(
        "question.html", question_num=question_id, question=question)
    