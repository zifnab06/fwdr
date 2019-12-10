from mongoengine import Document, StringField


class Forward(Document):
    source = StringField(required=True)
    dest = StringField(required=True, regex="\w+:(\/?\/?)[^\s]+")
