from PIL.Image import Image
from PIL import Image as Image2
from werkzeug.security import check_password_hash
import database.models as models
import database.db_queries as db_queries
import database.db_tables as db_tables

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
    share = Image2.open(user.share_path)
    return share

