from werkzeug.security import generate_password_hash
import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

username = "admin"
password = "admin123"
full_name = "System Administrator"
email = "admin@ecocycle.com"

DATABASE_URL = os.environ.get('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set. Please create a PostgreSQL database in Replit.")

conn = psycopg.connect(DATABASE_URL)
c = conn.cursor()
password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
c.execute("INSERT INTO admins (username, password_hash, full_name, email) VALUES (%s, %s, %s, %s)",
             (username, password_hash, full_name, email))
conn.commit()
conn.close()

print("✅ Admin created successfully! Username:", username, "Password:", password)
