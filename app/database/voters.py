from database.db_tables import get_connection
from database.db_queries import __add_voter__, __get_voter__

def add_voter(email: str, survey_id: str):
    """Adds email given to the allowed voters at survey given\n
    Args:\n
        email (str)\n
        survey_id (str)\n
    """
    conn = get_connection()
    __add_voter__(conn, email, survey_id)


def get_voter(email: str, survey_id: str):
    """Returns models.voter of voters with email given in survey given

    Args:
        emali (str)
        survey_id (str)
    Returns:
        Voter (models.voter)
    """
    conn = get_connection()
    return __get_voter__(conn, email, survey_id)
    