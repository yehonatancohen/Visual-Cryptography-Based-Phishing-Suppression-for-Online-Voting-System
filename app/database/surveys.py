from database.db_queries import __get_survey__, __add_survey__, __get_surveys__, \
                                __get_results__, __delete_survey__, __update_survey_start_time__, __update_survey_end_time__
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
                end_day: int, end_month: int, end_year: int,  owner_email: str,
                start_hour = 0, start_minute = 0, end_hour = 0, end_minute = 0) -> str:
    """This methods creates a survey with a unique id and retuns the id.
    Args:
        name (str): 
        start_day (int): 
        start_month (int): 
        start_year (int): 
        end_day (int): 
        end_month (int): 
        end_year (int): 
        owner_email (str): 
        start_hour (int, optional): Defaults to 0.
        start_minute (int, optional): Defaults to 0.
        end_hour (int, optional): Defaults to 0.
        end_minute (int, optional): efaults to 0.
    Returns:
        str: Survey id
    """
    conn = get_connection()
    return __add_survey__(conn, name, start_day, start_month, start_year, start_hour, start_minute,
                   end_day, end_month, end_year, end_hour, end_minute,owner_email, SURVEY_NAME_LENGTH_LIMIT)
    

def get_user_surveys(email: str) -> list[Survey]:
    """Returns all surveys where email given is their owner
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


def get_results(survey_id: str) -> dict:
    """returns dictionary: { candidate_id: votes }
    Args:
        survey_id (str)
    Returns:
        dict
    """
    conn = get_connection()
    return __get_results__(conn, survey_id)
    

def requirements_to_vote(survey_id: str, voter_email: str) -> dict:
    """

    Args:
        survey_id (str): 
        voter_email (str):

    Returns:
        dict: contain "survey_name", "start_date", "end_date", "has_user_voted"
    """
    from .voters import get_voter
    voter = get_voter(voter_email, survey_id)
    from .surveys import get_survey
    survey = get_survey(survey_id)

    has_voted = False
    if voter.has_voted == 1:
        has_voted = True
    result = {"survey_name": survey.name,
              "start_date": survey.start_date,
              "end_date": survey.end_date,
              "has_user_voted": has_voted}
    return result

def update_start_date(survey_id: str, start_year: int, start_month: int, start_day: int, start_hour: int, start_minute: int):
    """This method updates the start date of the survey according to ALL the parameters given
    Args:
        survey_id (str)
        start_year (int)
        start_month (int)
        start_day (int)
        start_hour (int)
        start_minute (int)
    """
    conn = get_connection()
    __update_survey_start_time__(conn, survey_id, start_year, start_month, start_day, start_hour, start_minute)

def update_end_date(survey_id: str, end_year: int, end_month: int, end_day: int, end_hour: int, end_minute: int):
    """This method updates the end date of the survey according to ALL the parameters given

    Args:
        survey_id (str)
        end_year (int)
        end_month (int)
        end_day (int)
        end_hour (int)
        end_minute (int)
    """
    conn = get_connection()
    __update_survey_end_time__(conn, survey_id, end_year, end_month, end_day, end_hour, end_minute)