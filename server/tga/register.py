from flask import Blueprint
from flask_babel import lazy_gettext
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

from newsroom.auth.forms import SignupForm

blueprint = Blueprint('register', __name__)


class RegisterEOIForm(SignupForm):
    company = StringField(lazy_gettext('Organisation / Institute'), validators=[DataRequired()])
    occupation = StringField(lazy_gettext('Position held / Title'))
    consent_login = BooleanField(lazy_gettext('I consent to'), validators=[])
    consent_alerts = BooleanField(lazy_gettext('I consent to'), validators=[])
    consent_reporting = BooleanField(lazy_gettext('I consent to'), validators=[])
    consent_terms = BooleanField(lazy_gettext('I agree to'), validators=[])


def init_app(app):
    app.signup_form_class = RegisterEOIForm
