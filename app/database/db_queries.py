import shortuuid
from werkzeug.security import generate_password_hash
from PIL.Image import Image
from PIL import Image as ImageLoader
import json
from database.db_files import save_candidate_img, save_share
from database.models import User
from database.models import Survey
from database.models import Voter
from database.models import Candidate
from database.db_tables import USERS_TABLE_NAME, VOTERS_TABLE_NAME,\
                        SURVEYS_TABLE_NAME, CANDIDATE_TABLE_NAME


def __add_user__(conn, email: str,
                f_name: str, s_name: str, share2: Image,
                password: str, server_code: str,
                email_size_limit: int = -1,
                f_name_size_limit: int = -1,
                s_name_size_limit: int = -1,
                ):
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

    
    share_path = save_share(share2)
    hashed_pswd = generate_password_hash(password, method="scrypt", salt_length=128)
    hashed_code = generate_password_hash(server_code, method="scrypt", salt_length=128)
    curr.execute(f'INSERT INTO {USERS_TABLE_NAME} (email, f_name, s_name, share_path, pass, server_code) \
                 VALUES (?, ?, ?, ?, ?, ?) ', (email, f_name, s_name, share_path, hashed_pswd, hashed_code))
    conn.commit()
    conn.close()


def __get_user__(conn, email):
    curr = conn.cursor()

    curr.execute(F'SELECT * FROM {USERS_TABLE_NAME} WHERE email = ?', (email,))
    rows = curr.fetchall()
    if len(rows) > 1:
        raise MemoryError(f"More than one user with {email}")
    if len(rows) == 0:
        return None
    row = rows[0]
    conn.close()
    return User(row[0], row[1], row[2], row[3], row[4], row[5])
    

def __add_survey__(conn, name: str, start_day: int, start_month: int, start_year: int, start_hour: int,
                    end_day: int, end_month: int, end_year: int, end_hour: int, owner_mail, name_length_limit = -1):
    curr = conn.cursor()
    from database.users import get_user
    if get_user(owner_mail) is None:
        raise ValueError(f"email \"{owner_mail}\" doesn't exist")
    id_ = shortuuid.uuid()
    # YYYY-MM-DD HH:MM 

    start_time = f'{start_year:04d}-{start_month:02d}-{start_day:02d} {start_hour:02d}:00'
    end_time = f'{end_year:04d}-{end_month:02d}-{end_day:02d} {end_hour:02d}:00'
    if name_length_limit != -1 and len(name) > name_length_limit:
        return ValueError(f"survey name {name} longer than allowed length ({name_length_limit})")
    curr.execute(f'INSERT INTO {SURVEYS_TABLE_NAME} (id, name, start, end, owner) VALUES (?, ?, ?, ?, ?) ', (id_, name, start_time, end_time, owner_mail,))
    conn.commit()
    conn.close()
    return id_


def __get_survey__(conn, survey_id: str) -> Survey:
    curr=conn.cursor()

    curr.execute(f'SELECT * FROM {SURVEYS_TABLE_NAME} WHERE id = ?', (survey_id,))
    rows = curr.fetchall()
    if len(rows) > 1:
        raise MemoryError(f"More than one user with {survey_id}")
    if len(rows) == 0:
        return None
    row = rows[0]
    conn.close()
    return Survey(row[0], row[1], row[2], row[3], row[4])


def __get_surveys__(conn, email: str) -> list[Survey]:
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {SURVEYS_TABLE_NAME} WHERE owner = ?', (email,))
    rows = cur.fetchall()
    if len(rows) == 0:
        return []
    result = []
    for row in rows:
        survey = Survey(row[0], row[1], row[2], row[3], row[4])
        result.append(survey)
    conn.close()
    return result


def __get_participating_surveys__(conn, email: str) -> list[Voter]:
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {VOTERS_TABLE_NAME} where user = ?', (email,))
    rows = cur.fetchall()
    if len(rows) == 0:
        return []
    result = []
    for row in rows:
        voter = Voter(row[0], row[1], row[2])
        result.append(voter)
    conn.close()
    return result


def __delete_survey__(conn, id: str) -> None:
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {SURVEYS_TABLE_NAME} WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def __get_voter__(conn, email: str, survey_id: str) -> Voter:
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {VOTERS_TABLE_NAME} WHERE user = ? AND survey_id = ?'
                , (email, survey_id))
    rows = cur.fetchall()
    if len(rows) == 0:
        return None
    if len(rows) > 1:
        raise MemoryError(f"More than one voter {email} at survey {survey_id}")
    row = rows[0]
    conn.close()
    return Voter(row[0], row[1], row[2])



def __add_voter__(conn, email: str, survey_id: str) -> None:
    cur = conn.cursor()
    from database.surveys import get_survey

    if get_survey(survey_id) is None:
        raise ValueError(f"Survey {survey_id} given does not exist")
    
    from database.voters import get_voter
    if get_voter(email, survey_id) is not None:
        raise ValueError(f"Voter {email} already exists in survey {survey_id}")
    
    cur.execute(f"INSERT INTO {VOTERS_TABLE_NAME} (survey_id, user, voted) VALUES (?, ?, ?)",
                 (survey_id, email, False))
    conn.commit()
    conn.close()

def __get_all_voters__(conn, survey_id: str) -> list[Voter]:
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {VOTERS_TABLE_NAME} WHERE survey_id = ?', (survey_id, ))
    rows = cur.fetchall()
    result = []
    for row in rows:
        voter = Voter(row[0], row[1], row[2])
        result.append(voter)
    conn.close()
    return result


def __remove_voter__(conn, survey_id: str, email: str) -> None:
    cur = conn.cursor()
    from database.voters import get_voter
    if get_voter(email, survey_id) is None:
        raise ValueError(f'No voter {email} at survey {survey_id}')
    
    cur.execute(f'DELETE FROM {VOTERS_TABLE_NAME} WHERE survey_id = ? AND user = ?',
                (survey_id, email, ))
    conn.commit()
    conn.close()
    

def __add_candidate__(conn, survey_id: str, name: str, desc: str, image: Image = None,
                      candidate_desc_size_limit = -1) -> None:
    cur = conn.cursor()
    from database.surveys import get_survey
    if get_survey(survey_id) is None:
        return ValueError(f'Survey {survey_id} does not exist')
    
    if candidate_desc_size_limit != -1 and len(desc) > candidate_desc_size_limit:
        raise ValueError(f"First name larger the allowed length \
                         (len({desc}) = {len(desc)} > {candidate_desc_size_limit})")
    img_path = ""
    if image is not None:
        img_path = save_candidate_img(image)
    
    cur.execute(f'INSERT INTO {CANDIDATE_TABLE_NAME} (candidate_id, survey_id, cand_name, cand_desc, image_path, votes)\
                VALUES (\
                (SELECT IFNULL(MAX(candidate_id), 0) + 1 FROM {CANDIDATE_TABLE_NAME} WHERE survey_id = ?), \
                ?, ?, ?, ?, 0)', (survey_id, survey_id, name, desc, img_path,))
    
    conn.commit()
    conn.close()


def __get_candidate__(conn, survey_id: str, candidate_id: int) -> Candidate:
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {CANDIDATE_TABLE_NAME} WHERE survey_id = ? AND candidate_id = ?'
                ,(survey_id, candidate_id))
    rows = cur.fetchall()
    if len(rows) == 0:
        return None
    if len(rows) > 1:
        raise MemoryError(f"More than one candidate {candidate_id} at survey {survey_id}")
    row = rows[0]
    conn.close()
    return Candidate(row[0], row[1], row[2], row[3], row[4], row[5])


def __get_all_candidates__(conn, survey_id: str) -> list[Candidate]:
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {CANDIDATE_TABLE_NAME} WHERE survey_id = ?'
                ,(survey_id, ))
    rows = cur.fetchall()
    result = []
    for row in rows:
        candidate = Candidate(row[0], row[1], row[2], row[3], row[4], row[5])
        result.append(candidate)
    conn.close()
    return result
    

def __remove_candidate__(conn, survey_id: str, candidate_id: int) -> None:
    cur = conn.cursor()
    from database.candidates import get_candidate
    if get_candidate(survey_id, candidate_id) is None:
        raise ValueError(f"candidate {candidate_id} does not exist in survey {survey_id}")
    cur.execute(f'DELETE FROM {CANDIDATE_TABLE_NAME} WHERE survey_id = ? AND candidate_id = ?'
                ,(survey_id, candidate_id, ))
    conn.commit()
    conn.close()



def __voter_vote__(conn, email: str, survey_id: str, candidate_id: int) -> bool:
    cur = conn.cursor()
    from database.voters import get_voter
    voter = get_voter(email, survey_id)
    if voter is None or voter.has_voted == 1:
        return False
    
    from database.candidates import get_candidate
    if get_candidate(survey_id, candidate_id) is None:
        raise ValueError(f"Candidate {candidate_id} does not exist is survey {survey_id}")

    cur.execute(f'SELECT votes from {CANDIDATE_TABLE_NAME} where survey_id = ? AND candidate_id = ?',
                (survey_id, candidate_id, ))
    new_votes = int(cur.fetchall()[0][0]) + 1
    cur.execute(f'UPDATE {CANDIDATE_TABLE_NAME} SET votes = ? WHERE survey_id = ? AND candidate_id = ?',
                (new_votes, survey_id, candidate_id,))
    cur.execute(f'UPDATE {VOTERS_TABLE_NAME} SET voted = ? WHERE user = ? AND survey_id = ?',
                (1, email, survey_id))
    conn.commit()
    conn.close()
    return True


def __get_results__(conn, survey_id):
    cur = conn.cursor()
    cur.execute(f'SELECT candidate_id, votes FROM {CANDIDATE_TABLE_NAME} WHERE survey_id = ?',
                (survey_id, ))
    rows = cur.fetchall()
    results = {}
    for row in rows:
        json_obj = json.loads('{"'+str(row[0])+'":"'+str(row[1])+'"}')
        results = {**results, **json_obj}

    return results
