from flask import Flask, request, render_template, redirect, url_for
from Story import *
from clarifaiTags import *

app = Flask(__name__) 
    

newStory = Story

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('welcome.html')

@app.route('/page1',methods=['GET', 'POST'])
def page1():
    newStory.Characters.name = request.args['char_name']
    newStory.Characters.gender = request.args['char_gender']
    return render_template('page1.html', newStory = newStory)

@app.route('/page2',methods=['GET', 'POST'])
def page2():
    newStory

    return render_template('page2.html', newStory = newStory)

@app.route('/page3',methods=['GET', 'POST'])
def page3():
    #print(clarifaiTags.tags(file))
    return render_template('page3.html', newStory = newStory)

@app.route('/page4',methods=['GET', 'POST'])
def page4():
    return render_template('page4.html', newStory = newStory)

@app.route('/page5',methods=['GET', 'POST'])
def page5():
    return render_template('page5.html', newStory = newStory)

@app.route('/page6',methods=['GET', 'POST'])
def page6():
    return render_template('page6.html', newStory = newStory)

@app.route('/page7',methods=['GET', 'POST'])
def page7():
    return render_template('page7.html', newStory = newStory)



if __name__ == "__main__":
    app.run(debug=True)
