from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to The best Blog Website Online'
    return render_template('index.html', title=title)

@app.route('/blog/<int:blog_id>')
def blog(blog_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('blog.html',id = blog_id)