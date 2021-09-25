from flask import render_template
from . import main
from flask_login import login_required



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to The best Blog Website Online'
    return render_template('index.html', title=title)

@main.route('/blog/<int:blog_id>')
@login_required
def blog(blog_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('blog.html',id = blog_id)