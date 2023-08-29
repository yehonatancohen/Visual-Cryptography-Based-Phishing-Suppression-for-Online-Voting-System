from database.db_queries import __get_survey__, __add_survey__, __get_surveys__, __delete_survey__
from database.db_tables import get_connection
from database.models import Survey

SURVEY_NAME_LENGTH_LIMIT = 150

def get_survey(survey_id: str) -> Survey:
    """this methods returns models.survey with the appropriate id
    Args:
        survey_id (str): The unique survey_id received when creating the survey
    Returns:
        Survey
    """
    conn = get_connection()
    sur = __get_survey__(conn, survey_id)
    return sur


def add_survey(name: str, start_day: int, start_month: int, start_year: int,
                end_day: int, end_month: int, end_year: int, owner_email: str) -> str:
    """This methods creates a survey with a unique id and retuns the id.
    Args:
        name (str): _description_
        start_day (int): _description_
        start_month (int): _description_
        start_year (int): _description_
        end_day (int): _description_
        end_month (int): _description_
        end_year (int): _description_
        owner_email (str): _description_
    Returns:
        str: survey id
    """
    conn = get_connection()
    return __add_survey__(conn, name, start_day, start_month, start_year,
                   end_day, end_month, end_year, owner_email, SURVEY_NAME_LENGTH_LIMIT)
    

def get_user_surveys(email: str) -> list[Survey]:
    """Returns all survey's where email given is their owner
    Args:
        email (str)

    Returns:
        surveys (list(models.survey))
    """
    conn = get_connection()
    return __get_surveys__(conn, email)


def delete_survey(id: str) -> None:
    """This method receives a survey id and removes it from the database
    Args:
        id (str)
    Returns:
        None
    """
    conn = get_connection()
    __delete_survey__(conn, id)
