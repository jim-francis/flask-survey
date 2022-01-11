from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "nge4ev"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

RESPONSES = "responses"

@app.route('/')
def show_homepage():
    survey_title = survey.title
    survey_instructions = survey.instructions
    return render_template('home.html', survey_title=survey_title, survey_instructions=survey_instructions)

@app.route('/start', methods=["POST"])
def start_survery():
    session[RESPONSES] = []
    return redirect("/question/0")

@app.route('/question/<question_id>')
def ask_question(question_id):
    # question_to_ask = satisfaction_survey.questions
    responses = session.get(RESPONSES)
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
    responses = session[RESPONSES]
    responses.append(choice)
    session[RESPONSES] = responses

    if (responses is None):
        return redirect("/")
    if (len(responses) == len(survey.questions)):
        return redirect("/finished")
    else:
        return redirect(f"/question/{len(responses)}")

@app.route("/finished")
def show_gratitude():
    return "Thanks!"