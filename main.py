from flask import Flask, render_template
import os
app = Flask(__name__)
skills1 = {('html',80),('python', 90),('css', 75)}


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', pagetitle= 'Home page', page_head= 'HOME PAGE',
                          description= 'WELCOME TO MY PAGE'  )
@app.route('/about')
def about():
    return render_template('about.html', pagetitle= 'About page',page_head= 'About ME', 
                            description= 'I`m Ali Walid',
                            description2= 'I`m 13 years old and this my first projet')

@app.route('/skills')
def skills():
    return render_template('skills.html', pagetitle= 'Skills page', page_head='My skills',
                                   description= 'this is my skills',
                                   skills= skills1,
                                   custom_css= 'skills')
if __name__ == '__main__':
    app.run(debug = True)
