from flask import Flask, request, url_for, render_template
import random

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

personne = ''
spaces3 = 

@app.route('/')
def hello_person():
        return render_template('index.html')
        % (url_for('greet'),)

@app.route('/greet', methods=['POST'])
def greet():
    global personne
    personne = request.form["person"]
    greet = random.choice(["Welcome", "Hello", "Greetings", "Hi"])
    return render_template('greet.html')
    % (greet, personne, url_for('intro'))


@app.route('/intro')
def intro():
    global personne
    global spaces3
    return render_template('intro.html')
% (personne, intro, url_for('static', filename='option1'), url_for('static', filename='option2'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
        
@app.route('/static/option1')
def option1():
    return render_template('option1.html')
    % (option1)


@app.route('/static/option2')
def option2():
    global personne
    return render_template('option2.html')
    return """
    """ % (option2, personne)

if __name__ == '__main__':
    app.run()