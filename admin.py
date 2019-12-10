from flask import redirect
from flask_admin.contrib.mongoengine import ModelView

from exceptions import AuthException
from extensions import admin, basic_auth
from models import Forward


class SecureModelView(ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException("Not authenticated")
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())

class ForwardModel(SecureModelView):
    pass


admin.add_view(ForwardModel(Forward))
