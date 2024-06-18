from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/contact_two')
def about_two():
    return render_template('contact_two.html')


@app.route('/contact_three')
def about_three():
    return render_template('contact_three.html')


@app.route('/about')
def about_1():
    return render_template('about.html')


@app.route('/diplom')
def diplom():
    return render_template('diplom.html')


@app.route('/gram')
def gram():
    return render_template('gram.html')



