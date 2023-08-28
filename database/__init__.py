import database.db_tables as db_tables
import database.models as models
import database.db_queries as db_queries
from PIL.Image import Image
EMAIL_SIZE_LIMIT = 150
F_NAME_SIZE_LIMIT = 100
S_NAME_SIZE_LIMIT = 100


def init_tables():
    db_tables.init_tables()

def add_user(email, f_name, s_name, share2: Image, password) -> None:
    f"""This methods creates a user
    Args:
        email (str): up to {EMAIL_SIZE_LIMIT} chars
        f_name (str): up to {F_NAME_SIZE_LIMIT} chars
        s_name (str): up to {S_NAME_SIZE_LIMIT} chars
        share2 (PIL Image file): The seconds share to be saved
        password (str): The plain password to be hashed and saved
    """
    conn = db_tables.get_connection()
    db_queries.__add_user__(conn, email, f_name, s_name, share2, password,
                                  email_size_limit=EMAIL_SIZE_LIMIT, 
                                  f_name_size_limit=F_NAME_SIZE_LIMIT,
                                  s_name_size_limit=S_NAME_SIZE_LIMIT)
    
def get_user(email: str) -> models.User:
    """This method returns a Model.User
    Args:
        email (str)
    Returns:
        models.User: A model to describe the user saved
    """
    conn = db_tables.get_connection()
    return db_queries.__get_user__(conn, email)