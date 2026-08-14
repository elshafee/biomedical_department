import os
from sqlalchemy import text
from main import app, db

def alter_db():
    with app.app_context():
        try:
            db.session.execute(text("ALTER TABLE documents ADD COLUMN sender_position TEXT;"))
            db.session.commit()
            print("Successfully added sender_position column!")
        except Exception as e:
            print(f"Error (maybe it already exists?): {e}")

if __name__ == "__main__":
    alter_db()
