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

    if (len(responses) != question_id):
        flash(f"Bad question ID: {question_id}.")
        return redirect(f"/question/{len(responses)}")

    return render_template(
        "question.html", question_num=question_id, question=question)
    
@app.route("/answer", methods=["POST"])
def handle_question():
    choice = request.form['answer']
    responses.append(choice)

    if (len(responses) == len(survey.questions)):
        return redirect("/finished")
    else:
        return redirect(f"/question/{len(responses)}")

@app.route("/finished")
def show_gratitude():
    return "Thanks!"