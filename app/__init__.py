from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__) 

class Story:
    class Characters:
        '''
        mainCharacter = "Cinderella"
        animals = "mice"
        stepMother = ""
        sisters = ["sister1", "sister2"]
        '''
        "this is the main character's name, gender and pronoun below"
        name = ""
        gender = ""
        pronoun = ""
        "this is the name of the great-granddaughter"
        girlName = ""
        
    class Phrases:
        adjs = ["kind", "", "", "", ""]
        adverb1 = "swift programming abilities"
        verbs = ["", "", "", ""]
        noun = ["", "", "", ""]
    
    

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('welcome.html')

@app.route('/page1',methods=['GET', 'POST'])
# , result=request.form['char_name']
def page1():
    newStory = Story
    newStory.Characters.mainCharacter = request.args['char_name']
    # newStory.Characters.mainCharacter = request.args[charName]

    return render_template('page1.html', newStory = newStory)

def page2():
    

    return render_template('page2.html')

if __name__ == "__main__":
    app.run(debug=True)
