import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blog'

     # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    UPLOADED_PHOTOS_DEST ='app/static/photos'



class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://udyrauduwnzwqi:cfe7be4372aa8830489cae94c5d7c4bba41a00c7eb55cddb8f3bd7bd8300db99@ec2-3-218-47-9.compute-1.amazonaws.com:5432/d84utev4keet55'


class TestConfig(Config):
  
    pass


class DevConfig(Config):
  

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
