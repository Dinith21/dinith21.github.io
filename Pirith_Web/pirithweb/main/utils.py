from flask_mail import Message
from pirithweb import mail
from pirithweb.models import User
from pirithweb.main.forms import ContactForm

def send_contact_email():
    form = ContactForm()
    msg = Message(form.title.data, sender='Din.FlaskBlog@gmail.com', recipients='Din.FlaskBlog@gmail.com')
    msg.body = f'''Message from {user.username} ({form.email.data}):
{form.content.data}
'''
    mail.send(msg)
