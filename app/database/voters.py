from database.db_tables import get_connection
from database.db_queries import __add_voter__, __get_voter__, \
    __get_all_voters__, __remove_voter__
from database.models import Voter


def add_voter(email: str, survey_id: str) -> None:
    """Adds email given to the allowed voters at survey given\n
    Args:\n
        email (str)\n
        survey_id (str)\n
    """
    conn = get_connection()
    __add_voter__(conn, email, survey_id)


def get_voter(email: str, survey_id: str) -> Voter:
    """Returns models.voter of voters with email given in survey given

    Args:
        emali (str)
        survey_id (str)
    Returns:
        Voter (models.voter)
    """
    conn = get_connection()
    return __get_voter__(conn, email, survey_id)
    

def get_all_voters(survey_id: str) -> list[Voter]:
    """This methods returns a list of Voter objects
    who vote in survey given

    Args:
        survey_id (str)
    Returns:
        list[Voter]
    """
    conn=get_connection()
    return __get_all_voters__(conn, survey_id)


def remove_voter(survey_id: str, email: str) -> None:
    """Removes voter with email specified from survey specified
    Args:
        survey_id (str)
        email (str)
    """
    conn = get_connection()
    return __remove_voter__(conn, survey_id, email)