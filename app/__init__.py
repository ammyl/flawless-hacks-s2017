from flask import Flask, request, render_template, redirect, url_for
import sys
import os
from os import listdir
from os.path import isfile, join


app = Flask(__name__) 

class Story:
    class Characters:
        mainCharacter = "Cinderella"
        animals = "mice"
        stepMother = ""
        sisters = ["sister1", "sister2"]
    class Phrases:
        adjs = ["kind", "", "", "", ""]
        adverb1 = "swift programming abilities"
        verbs = ["", "", "", ""]
        noun = ["", "", "", ""]
        
    

@app.route('/', methods=['GET'])
def home():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run(debug=True)
