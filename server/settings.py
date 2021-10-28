import pathlib
from newsroom.web.default_settings import BLUEPRINTS, env, strtobool

SERVER_PATH = pathlib.Path(__file__).resolve().parent
CLIENT_PATH = SERVER_PATH.parent.joinpath("client")

SITE_NAME = 'Newshub 360™'
COPYRIGHT_HOLDER = '360™'
SHOW_USER_REGISTER = True
SIGNUP_EMAIL_RECIPIENTS = 'info@360info.org'
HIDE_LOGIN = strtobool(env('HIDE_LOGIN', 'True'))
CONTACT_ADDRESS = '/contact_us'

BLUEPRINTS.extend([
    'tga.register',
])

LANGUAGES = ['en']
DEFAULT_LANGUAGE = 'en'
