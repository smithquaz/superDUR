from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class PatientForm(FlaskForm):
    nric = IntegerField('Username', validators=[DataRequired()])
    medication = StringField('Medication', validators = [DataRequired(), ])

    submit = SubmitField('Check DDI')