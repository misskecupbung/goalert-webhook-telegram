"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv


class Config(object):
    """
    Reading configuration from environment variables or .env.
    """

    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))
    TELEGRAM_TOKEN = environ.get("TELEGRAM_TOKEN", False)
    GOALERT_URL = environ.get("GOALERT_URL", False)
    DEBUG = environ.get("DEBUG", False)
    PORT = int(environ.get("PORT", 5001))
    HOST = environ.get("HOST", "0.0.0.0")
