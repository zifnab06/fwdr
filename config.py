import os

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "False") == "True"
MONGODB_SETTINGS = {
    "db": os.environ.get("MONGODB_DB", "forward"),
    "host": os.environ.get("MONGODB_HOST", "localhost"),
    "port": int(os.environ.get("MONGODB_PORT", "27017")),
}

BASIC_AUTH_USERNAME = os.environ.get("ADMIN_USERNAME")
BASIC_AUTH_PASSWORD = os.environ.get("ADMIN_PASSWORD")
