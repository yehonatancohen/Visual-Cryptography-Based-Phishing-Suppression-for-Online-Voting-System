import shortuuid
from werkzeug.security import generate_password_hash
from PIL.Image import Image
import database.db_files as db_files
from database.models import User
from database.models import Survey


def __add_user__(conn, email: str,
                f_name: str, s_name: str, share2: Image,
                password: str, server_code: str, sec_question: str,
                email_size_limit: int = -1,
                f_name_size_limit: int = -1,
                s_name_size_limit: int = -1):
    curr = conn.cursor()

    try:
        if not isinstance(share2, Image):
            raise AttributeError()
    except AttributeError:
        raise AttributeError("image given is not a PIL image")
    
    if email_size_limit != -1 and len(email) > email_size_limit:
        raise ValueError(f"First name larger the allowed length \
                         (len({email}) = {len(email)} > {email_size_limit})")
    
    if f_name_size_limit != -1 and len(f_name) > f_name_size_limit:
        raise ValueError(f"First name larger the allowed length \
                         (len({f_name}) = {len(f_name)} > {f_name_size_limit})")
    
    if s_name_size_limit != -1 and len(s_name) > s_name_size_limit:
        raise ValueError(f"Sur name larger the allowed length \
                         (len({s_name}) = {len(s_name)} > {s_name_size_limit})\n")
    
    share_path = db_files.save_img(share2)
    hashed_pswd = generate_password_hash(password, method="scrypt", salt_length=128)
    hashed_code = generate_password_hash(server_code, method="scrypt", salt_length=128)
    curr.execute('INSERT INTO users (email, f_name, s_name, share_path, pass, server_code, sec_question) \
                 VALUES (?, ?, ?, ?, ?, ?, ?) ', (email, f_name, s_name, share_path, hashed_pswd, hashed_code, sec_question))
    conn.commit()
    conn.close()
    return id


def __get_user__(conn, email):
    curr = conn.cursor()

    curr.execute('SELECT * FROM users WHERE email = ?', (email,))
    rows = curr.fetchall()
    if len(rows) > 1:
        raise MemoryError(f"More than one user with {email}")
    if len(rows) == 0:
        return None
    row = rows[0]
    return User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    

def __add_survey__(conn, name: str, start_day: int, start_month: int, start_year: int,
                    end_day: int, end_month: int, end_year: int, owner_mail, name_length_limit = -1):
    curr = conn.cursor()
    from database.users import get_user
    if get_user(owner_mail) is None:
        raise ValueError(f"email \"{owner_mail}\" doesn't exist")
    id_ = shortuuid.uuid()
    start_date = f'{start_year:04d}-{start_month:02d}-{start_day:02d}'
    end_date = f'{end_year:04d}-{end_month:02d}-{end_day:02d}'
    if name_length_limit != -1 and len(name) > name_length_limit:
        return ValueError(f"survey name {name} longer than allowed length ({name_length_limit})")
    curr.execute('INSERT INTO surveys (id, name, start, end, owner) VALUES (?, ?, ?, ?, ?) ', (id_, name, start_date, end_date, owner_mail,))
    conn.commit()
    conn.close()
    return id_


def __get_survey__(conn, survey_id: str) -> Survey:
    curr=conn.cursor()

    curr.execute('SELECT * FROM surveys WHERE id = ?', (survey_id,))
    rows = curr.fetchall()
    if len(rows) > 1:
        raise MemoryError(f"More than one user with {survey_id}")
    if len(rows) == 0:
        return None
    row = rows[0]
    return Survey(row[0], row[1], row[2], row[3], row[4])