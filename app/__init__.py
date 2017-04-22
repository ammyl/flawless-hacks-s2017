from flask import Flask, request, render_template, redirect, url_for


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
    newStory = Story
    newStory.mainCharacter = name
    return render_template('welcome.html')

@app.route('/1',methods=['GET'])
def page1():
    return render_template('page1.html')

if __name__ == "__main__":
    app.run(debug=True)
