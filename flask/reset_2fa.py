import pyotp
from main import app, db
from models import User
import sys

def reset_2fa(email=None):
    with app.app_context():
        if email:
            users = User.query.filter_by(email=email).all()
        else:
            users = User.query.all()
            
        if not users:
            print("No users found.")
            return

        for user in users:
            user.totp_secret = pyotp.random_base32()
            user.is_setup = False
            print(f"Reset 2FA for: {user.email}")
            
        db.session.commit()
        print("Done.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        reset_2fa(sys.argv[1])
    else:
        reset_2fa()
