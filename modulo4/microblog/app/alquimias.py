from app import db
from app.models.models import User, Post

def create_user(username, email, password, foto, bio):
    user = User(username=username, email=email, password=password, foto=foto, bio=bio)
    db.session.add(user)
    db.session.commit()

def create_post(body, user):
    post = Post(body=body, user=user)
    db.session.add(post)
    db.session.commit()

def get_timeline():
    return Post.query.order_by(Post.timestamp.desc()).limit(5).all()