from itsdangerous import URLSafeTimedSerializer as Serializer, BadSignature, SignatureExpired
from flask_mail import Message, Mail
from flask import Flask, url_for
import os

# This is to prove email verification in an app context 
app = Flask(__name__)

app.config.update(
    SECRET_KEY= os.environ.get("SECRET_KEY"),
    MAIL_SERVER= os.environ.get("MAIL_SERVER"),
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME= os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD= os.environ.get("MAIL_PASSWORD"),
    MAIL_DEFAULT_SENDER= os.environ.get("MAIL_USERNAME")
)

mail = Mail(app)

# Insert a mail for test
email = ''

def generate_verification_token(email):
    serializer = Serializer(app.config['SECRET_KEY'], salt='email-verify')
    token = serializer.dumps(email, salt='email-verify')
    return token

@app.route('/verify/<token>')
def verify_email(token):
    try:
        serializer = Serializer(app.config['SECRET_KEY'], salt='email-verify')
        email = serializer.loads(token, salt='email-verify', max_age=48*60*60)
        return 'Email verified successfully!'
    except BadSignature:
        return 'Link caducado: Invalid token', 404
    except SignatureExpired:
        return 'Link caducado: Token expired', 404
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return 'Error: Something went wrong', 500

@app.route('/register')
def register():
    token = generate_verification_token(email)
    verify_url = url_for('verify_email', token=token, _external=True)
    msg = Message("Por favor verifica tu correo electronico", recipients=[email])
    msg.body = f'El link de verificacion es: {verify_url}'
    
    try:
        mail.send(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
    
    return 'Check your email for the verification link'

if __name__ == '__main__':
    app.run(debug=True)

# Manual testing block for sending an email
with app.app_context():
    token = generate_verification_token(email)
    verify_url = url_for('verify_email', token=token, _external=True)
    msg = Message("Por favor verifica tu correo electronico", recipients=[email])
    msg.body = f'El link de verificacion es: {verify_url}'
    
    try:
        mail.send(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
