from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    subscription = db.Column(db.Boolean)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    posts = db.relationship('Post',backref = 'post',lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'post_id',lazy = 'dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.name}'



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'



class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String())
    text = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)

    comments = db.relationship('Comment',backref = 'post_id',lazy = 'dynamic')


    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def get_post(id):
        post = Post.query.filter_by(id=id).first()
        return post



class Comment(db.Model):
    __tablename__= 'comments'

    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.String(1000))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post = db.Column(db.Integer,db.ForeignKey('posts.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post):
        comments = Comment.query.filter_by(post=post.id).all()
        return comments
