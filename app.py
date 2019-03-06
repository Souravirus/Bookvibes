from flask import *
import pymysql
app= Flask(__name__)
app.secret_key='mysecretkey'

host="127.0.0.1"
user="root"
password=""
db="bookvibes"
con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
cur=con.cursor()

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
	data = request.form['search']
	cur.execute("select book1, book2, book3, book4, book5 from book where book_name='"+data+"'"+" limit 1")
	result = cur.fetchall()
	return(render_template("search_res.html", result=result, content_type='application/json'))

    
@app.errorhandler(404)
def pgntfnd(y):
    return(render_template("error404.html"))

if (__name__ == '__main__'):
    app.run(debug=True)
