from flask import Blueprint, flash, redirect, url_for, render_template, current_app as app
from flask_wtf import FlaskForm, RecaptchaField
from flask_babel import lazy_gettext, gettext
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

from newsroom.auth import get_auth_user_by_email
from newsroom.email import send_new_signup_email

blueprint = Blueprint('register', __name__)


class RegisterEOIForm(FlaskForm):
    name = StringField(lazy_gettext('Name'), validators=[DataRequired(), Length(1, 128)])
    company = StringField(lazy_gettext('Employer'), validators=[DataRequired()])
    position = StringField(lazy_gettext('Position held / Title'))
    email = StringField(lazy_gettext('Email'), validators=[DataRequired(), Length(1, 128), Email()])
    country = StringField(lazy_gettext('Country'), validators=[DataRequired()])
    referred_by = TextAreaField(lazy_gettext('How did you hear about us? (Referral, social media, web search)'))

    consent_login = BooleanField(lazy_gettext('I consent to'), validators=[])
    consent_alerts = BooleanField(lazy_gettext('I consent to'), validators=[])
    consent_reporting = BooleanField(lazy_gettext('I consent to'), validators=[])
    consent_terms = BooleanField(lazy_gettext('I agree to'), validators=[])

    recaptcha = RecaptchaField()


@blueprint.route('/register', methods=['GET', 'POST'])
def eoi():
    form = RegisterEOIForm()
    if form.validate_on_submit():
        new_user = form.data
        new_user.pop('csrf_token', None)

        user = get_auth_user_by_email(form.email.data)

        if user is not None:
            flash(gettext('Account already exists.'), 'danger')
            return redirect(url_for('auth.login'))

        send_new_signup_email(user=new_user)
        return render_template('signup_success.html'), 200
    return render_template(
        'register.html',
        form=form,
        sitekey=app.config['RECAPTCHA_PUBLIC_KEY'],
        terms=app.config['TERMS_AND_CONDITIONS']
    )
