from flask import *
app= Flask(__name__)
app.secret_key='mysecretkey'

@app.route('/')
def homepage():
    return(render_template("homepage.html"))

@app.route('/signup')
def signup():
    return(render_template("signup.html"))

@app.route('/signin')
def signin():
    return(render_template("signin.html"))

@app.route('/bookpage')
def bookpage():
    return(render_template("bookpage.html"))

@app.route('/welcome')
def welcome():
    return(render_template("welcome.html"))

@app.route('/book')
def book():
    return(render_template("book.html"))

@app.route('/search_res', methods = ['POST', 'GET'])
def search_res():
	result = request.form 
	return(render_template("search_res.html", result=result))

    
@app.errorhandler(404)
def pgntfnd(y):
    return(render_template("error404.html"))

if (__name__ == '__main__'):
    app.run(debug=True)
