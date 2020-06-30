from flask import render_template, url_for, flash, redirect, Blueprint, abort, request
from pirithweb.models import Post, User
from pirithweb.main.forms import ContactForm
from pirithweb.main.utils import send_contact_email

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('main/home.html')

@main.route("/about")
def about():
    return render_template('main/about.html', title='About')

@main.route("/help")
def help():
    return render_template('main/help.html', title='Help')

@main.route("/contact", methods=['GET', 'POST'])
def contact():
    # form = ContactForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     send_contact_email(user)
    #     flash('Your message has been sent. Thank you!', 'success')
    #     return redirect(url_for('main.home'))
    return render_template('errors/construction.html', title='Contact')

@main.route("/announcements")
def announcements():
    return render_template('errors/construction.html', title='Announcements')
