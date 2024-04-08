import pathlib
from newsroom.web.default_settings import (
    BLUEPRINTS as DEFAULT_BLUEPRINTS,
    env,
    strtobool,
    CLIENT_CONFIG,
    CORE_APPS as DEFAULT_CORE_APPS,
)

SERVER_PATH = pathlib.Path(__file__).resolve().parent
CLIENT_PATH = SERVER_PATH.parent.joinpath("client")

SITE_NAME = "360info.org"
COPYRIGHT_HOLDER = "360info"
SHOW_USER_REGISTER = True
SIGNUP_EMAIL_RECIPIENTS = "info@360info.org"
HIDE_LOGIN = strtobool(env("HIDE_LOGIN", "True"))
GOOGLE_LOGIN = False
CONTACT_ADDRESS = "https://360info.org/about-us/contact-us/"
TERMS_AND_CONDITIONS = "/page/terms"

CORE_APPS = [
    app
    for app in DEFAULT_CORE_APPS
    if app
    not in [
        "newsroom.monitoring",
        "newsroom.auth.oauth",
        "newsroom.oauth_clients",
    ]
] + ["tga.register"]

BLUEPRINTS = ["tga.register"] + [
    blueprint
    for blueprint in DEFAULT_BLUEPRINTS
    if blueprint
    not in [
        "newsroom.design",
        "newsroom.monitoring",
        "newsroom.oauth_clients",
        "newsroom.auth_server.oauth2",
    ]
]

LANGUAGES = ["en"]
DEFAULT_LANGUAGE = "en"
NEWS_API_ENABLED = True
WATERMARK_IMAGE = None

# Client configuration
CLIENT_CONFIG.update(
    {
        "display_abstract": True,
        "display_credits": True,
    }
)

CLIENT_LOCALE_FORMATS = {
    "en": {  # defaults
        "TIME_FORMAT": "HH:mm",
        "DATE_FORMAT": "DD/MM/YYYY",
        "COVERAGE_DATE_TIME_FORMAT": "HH:mm DD/MM",
        "COVERAGE_DATE_FORMAT": "DD/MM",
        "DATE_FORMAT_HEADER": "EEEE, MMMM d, yyyy",
    },
}

COMPANY_TYPES = [
    dict(
        id="news_media",
        name="News Media",
    ),
    dict(
        id="education",
        name="Education",
    ),
    dict(
        id="research",
        name="Research",
    ),
    dict(
        id="government_public_sector",
        name="Government/Public Sector",
    ),
    dict(
        id="ngo",
        name="Non-Profit/NGO",
    ),
    dict(
        id="other",
        name="Other",
    ),
]

PUBLIC_DASHBOARD = True
