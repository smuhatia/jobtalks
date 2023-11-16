from flask import Flask, jsonify, request, render_template, redirect, url_for
import json
import requests
from flask_app.tables.stories import engine, Story
from sqlalchemy.orm import Session

app = Flask(__name__)

@app.route("/home_page", strict_slashes=False, methods=['GET', 'POST'])
def home_page():
    """Grab name and job experience from post request"""
    if request.method == "GET":
        return render_template("8-5.html")
    
    if request.method == "POST":
        name_jina = request.form['name_jina']
        job_experience = request.form['job_experience']

        with Session(engine) as session:
            experience = Story(name_jina=name_jina, job_experience=job_experience)
            session.add(experience)
            session.commit()

        return render_template("8-5.html")
    

@app.route("/exp", strict_slashes=False)
def list_experiences():
    # return jsonify(f"List of experiences entered by users")
    stories = []
    with Session(engine) as session:
        all_stories = session.query(Story).all()

        # all_stories is a list of Story() instances

        for story in all_stories:
            stories.append([story.id, story.name_jina, story.job_experience])
        
        return render_template("exp.html", stories=stories)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)