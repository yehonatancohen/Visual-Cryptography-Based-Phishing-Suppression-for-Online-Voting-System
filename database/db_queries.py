import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from PIL.Image import Image
import database.db_files as db_files
from database.models import User

def __add_user__(conn, email: str, f_name: str, s_name: str, share2: Image, password: str,
              email_size_limit: int = -1, f_name_size_limit: int = -1, s_name_size_limit: int = -1):
    curr = conn.cursor()

    try:
        if not isinstance(share2, Image):
            raise AttributeError()
    except AttributeError:
        raise AttributeError(f"image given is not a PIL image")
    
    if email_size_limit != -1 and len(email) > email_size_limit:
        raise ValueError(f"First name larger the allowed length (len({email}) = {len(email)} > {email_size_limit})")
    
    if f_name_size_limit != -1 and len(f_name) > f_name_size_limit:
        raise ValueError(f"First name larger the allowed length (len({f_name}) = {len(f_name)} > {f_name_size_limit})")
    
    if s_name_size_limit != -1 and len(s_name) > s_name_size_limit:
        raise ValueError(f"Sur name larger the allowed length (len({s_name}) = {len(s_name)} > {s_name_size_limit})\n")
    
    share_path = db_files.save_img(share2)
    hashed_pswd = generate_password_hash(password, method="scrypt", salt_length=128)
    curr.execute('INSERT INTO users (email, f_name, s_name, share_path, pass) VALUES (?, ?, ?, ?, ?) ', (email, f_name, s_name, share_path, hashed_pswd,))
    conn.commit()
    conn.close()


def __get_user__(conn, email):
    curr = conn.cursor()

    curr.execute('SELECT * FROM users WHERE email = ?', (email,))
    rows = curr.fetchall()
    if len(rows) > 1:
        raise MemoryError(f"More than one user with {email}")
    row = rows[0]
    return User(row[0], row[1], row[2], row[3], row[4])
    