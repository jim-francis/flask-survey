from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "nge4ev"

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_homepage():
    survey_title = satisfaction_survey.title
    survey_instructions = satisfaction_survey.instructions
    return render_template('home.html', survey_title=survey_title, survey_instructions=survey_instructions)