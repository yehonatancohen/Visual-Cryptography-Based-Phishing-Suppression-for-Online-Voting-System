from PIL.Image import Image
from PIL import Image as Image2
from werkzeug.security import check_password_hash
import database.models as models
import database.db_queries as db_queries
import database.db_tables as db_tables
from .db_files import get_img_from_bucket
EMAIL_SIZE_LIMIT = 150
F_NAME_SIZE_LIMIT = 100
S_NAME_SIZE_LIMIT = 100

def add_user(email: str, f_name: str, s_name: str, share2: Image,
            password: str, server_code: str) -> None:
    """This methods creates a user\n
    Args:
        email (str): up to {EMAIL_SIZE_LIMIT} chars
        f_name (str): up to {F_NAME_SIZE_LIMIT} chars
        s_name (str): up to {S_NAME_SIZE_LIMIT} chars
        share2 (PIL Image file): The seconds share to be saved
        password (str): The plain password to be hashed and saved
        server_code (str): The server generated code that appears inside the captcha
    """
    conn = db_tables.get_connection()
    if get_user(email) is not None:
        return ValueError("Email is already registerd")
    db_queries.__add_user__(conn, email, f_name, s_name, share2, password, server_code,  
                            email_size_limit=EMAIL_SIZE_LIMIT, 
                            f_name_size_limit=F_NAME_SIZE_LIMIT,
                            s_name_size_limit=S_NAME_SIZE_LIMIT,
                            )


def get_user(email: str) -> models.User:
    """This method returns a Model.User
    Args:
        email (str)
    Returns:
        models.User: A model to describe the user saved
        None of email does not exist
    """
    conn = db_tables.get_connection()
    return db_queries.__get_user__(conn, email)


def does_user_exist(email: str) -> bool:
    """ Returns true if a user with email given exists
    Args:
        email (str)
    Returns:
        bool
    """
    if get_user(email) is None:
        return False
    return True


def validate_user(email: str, password: str, server_code: str) -> bool:
    """Returns true if plain password given is matching to the password stored
    and the plain server code given is a match to the saved one.
    for user with email given
    Args:
        email (str)
        password (str)
        server_code (str)
    Returns:
        bool
    """
    user = get_user(email)
    if user is None:
        raise ValueError(f"email \"{email}\" doesn't exist")
    password = check_password_hash(user.hashed_password, password)
    code = check_password_hash(user.hashed_server_code, server_code)
    return (password and code)
    

def validate_user_share(email: str, server_code: str) -> bool:
    """ Returns true if the plain server code given is a match to the saved one.
    for user with email given

    Args:
        email (str)
        server_code (str)

    Returns:
        bool
    """
    user = get_user(email)
    if user is None:
        raise ValueError(f"email \"{email}\" doesn't exist")
    codeVarify = check_password_hash(user.hashed_server_code, server_code)
    return codeVarify


def get_share(email: str) -> Image:
    """Returns a PIL image file containing the given user's share 2
    Args:
        email (str)
    Returns:
        Image
    """
    user = get_user(email)
    if user is None:
        raise ValueError(f"email \"{email}\" doesn't exist")
    share = get_img_from_bucket(user.share_path)
    return share

def get_surveys_related_to_user(user_email: str) -> list[dict]:
    """
    Args:
        user_email (str)

    Returns:
        list[dict]: A list where each entry (one entry for each survey a user participates in AND the user owns) contains
            a dictionary with "survey_id", "survey_name", "start_date", "end_date", "has_user_voted", "is_owner"
    """
    from .voters import get_all_surveys_per_voter
    list1 = get_all_surveys_per_voter(user_email)
    [li.__setitem__("is_owner", False) for li in list1]
    
    from .surveys import get_user_surveys
    owned = get_user_surveys(user_email)
    result = list1



    for survey in owned:
        # Check for duplicate surveys
        existsInResult = False
        for li in result:
            if survey.id == li['survey_id']:
                existsInResult = True
                li['is_owner'] = True
                break
        if existsInResult: continue

        dict = {"survey_id":survey.id,
                "survey_name":survey.name,
                "start_date":survey.start_date,
                "end_date": survey.end_date,
                "is_owner": True
                }
        result.append(dict)
    return result