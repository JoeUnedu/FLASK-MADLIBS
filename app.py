""" MadLibs Application Server """

from flask import Flask, request, render_template
from stories import story, Story

app = Flask(__name__)


@app.route("/")
def welcome():
    """ Welcome  request borrowed from index.html  , put prompt from story class """

    return render_template("index.html", prompts = story.prompts)


@app.route("/story")
def story_page():

    #  ans hold the  key value pair 
    ans = {}
    for prompt in story.prompts:
        # let put entered value promt into the ans.
        ans[prompt] = "<b>" + \
            request.args.get(prompt, "") + "</b>"

    #  get to generate our story  and replace string  with string
    story_is_generate = story.generate(ans).strip("\n").replace("  ", " ")

    return render_template("story.html", my_story= story_is_generate)