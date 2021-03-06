from app.request import posting
from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Post,Comment
from .. import db
from .forms import PostForm, CommentForm
from flask_login import login_required, current_user
from ..email import mail_message



# Views
@main.route('/')
def index():

   
    posts = Post.query.order_by(Post.date_posted.desc()).limit(3).all()

    title = 'Welcome to The best Blog Website Online'
    postings=posting()
    return render_template('index.html', title=title, posts = posts,postings=postings)


@main.route('/post/new', methods =['GET','POST'])
@login_required
def new_post():
    if current_user.id:
        post_form = PostForm()
        if post_form.validate_on_submit():
            title = post_form.title.data
            text = post_form.text.data

            users = User.query.all()

            new_post = Post(title=title,text=text,post=current_user)

            new_post.save_post()

            for user in users:
                if user.subscription:
                    mail_message("New Post","email/new_post",user.email,user=user)

            return redirect(url_for('.index'))

    else:
        return redirect(url_for('.index'))

    title = 'New post'
    return render_template('new_post.html',title=title,post_form=post_form)

@main.route('/posts')
def all_posts():
    posts = Post.query.order_by(Post.date_posted.desc()).all()

    title = 'Blog posts'

    return render_template('posts.html', title = title, posts = posts)

@main.route('/post/<int:id>',methods=['GET','POST'])
def post(id):
    form = CommentForm()
    post = Post.get_post(id)


    if form.validate_on_submit():
        comment = form.text.data

        new_comment = Comment(comment = comment,post = post.id)

        new_comment.save_comment()


    comments = Comment.get_comments(post)

    title = f'{post.title}'
    return render_template('post.html',title = title, post = post, form = form, comments = comments)

@main.route('/delete_comment/<id>/<post_id>',methods = ['GET','POST'])
def delete_comment(id,post_id):
    comment = Comment.query.filter_by(id = id).first()

    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for('main.post',id = post_id))

@main.route('/delete_post/<id>',methods = ['GET','POST'])
def delete_post(id):
    post = Post.query.filter_by(id = id).first()

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('main.all_posts'))

@main.route('/subscribe/<id>')
def subscribe(id):
    user = User.query.filter_by(id = id).first()

    user.subscription = True

    db.session.commit()

    return redirect(url_for('main.index'))

@main.route('/post/update/<id>',methods = ['GET','POST'])
def update_post(id):
    form = PostForm()

    post = Post.query.filter_by(id = id).first()

    form.title.data = post.title
    form.text.data = post.text

    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data

        post.title = title
        post.text = text

        db.session.commit()

        return redirect(url_for('main.post',id=post.id))
    
    return render_template('update.html',form = form)