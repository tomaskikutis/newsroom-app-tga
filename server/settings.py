import pathlib
from newsroom.web.default_settings import BLUEPRINTS, env, strtobool, CLIENT_CONFIG

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
NEWS_API_ENABLED = True
WATERMARK_IMAGE = None

# Client configuration
CLIENT_CONFIG.update({
    'display_abstract': True,
    'display_credits': True,
})

DATE_FORMAT_HEADER = 'EEEE, MMMM d, yyyy'
