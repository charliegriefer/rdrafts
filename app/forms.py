from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import InputRequired, Length, URL
from flask.ext.pagedown.fields import PageDownField


# frontend thread form
class ThreadForm(Form):

    subreddit = TextField('Subreddit', validators=[InputRequired()])

    title = TextField(
        'Title',
        validators=[
            InputRequired(),
            Length(
                max=300,
                message="Title cannot be longer than 300 characters"
            )
        ]
    )

    body = PageDownField(
        'Body',
        validators=[
            InputRequired(),
            Length(
                max=5000,
                message="Description cannot be longer than 5000 characters"
            )
        ]
    )

    verification = TextField(
        'Verification Link',
        validators=[
            InputRequired(),
            URL(require_tld=True)
        ]
    )

    submit = SubmitField('Preview')


# subreddit form
class SubredditForm(Form):

    subreddit = TextField('Subreddit', validators=[InputRequired()])
    submit = SubmitField('Next')


# title form
class TitleForm(Form):

    title = TextField(
        'Title',
        validators=[
            InputRequired(),
            Length(
                max=300,
                message="Title cannot be longer than 300 characters"
            )
        ]
    )
    submit = SubmitField('Next')


# body form
class BodyForm(Form):

    body = PageDownField(
        'Body',
        validators=[
            InputRequired(),
            Length(
                max=5000,
                message="Description cannot be longer than 5000 characters"
            )
        ]
    )
    submit = SubmitField('Next')


# verification form
class VerificationForm(Form):

    verification = TextField(
        'Verification Link',
        validators=[
            InputRequired(),
            URL(require_tld=True)
        ]
    )
    submit = SubmitField('Next')


# delete thread form
class DeleteThreadForm(Form):
    submit = SubmitField('Confirm Delete')


# captcha form
class CaptchaForm(Form):
    captcha_response = TextField(
        '',
        validators=[
            InputRequired()
        ]
    )
    submit = SubmitField('Submit AMA')
