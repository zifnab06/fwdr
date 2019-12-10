from flask_admin import Admin
from flask_mongoengine import MongoEngine
from flask_basicauth import BasicAuth

admin = Admin()
basic_auth = BasicAuth()
mongoengine = MongoEngine()

def init_app(app):
    admin.init_app(app)
    basic_auth.init_app(app)
    mongoengine.init_app(app)
