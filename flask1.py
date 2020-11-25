from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Connor Carnes',
        'title':  'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Kenneth Carnes',
        'title':  'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 30, 2018'
    }
    
]


@app.route("/")     # example of multiple routes
@app.route("/home") # example of multiple routes
def home():
    return render_template('home.html', posts=posts)
    
@app.route("/about")
def about():
    return render_template('about.html', title='About')
    

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=8080)
    