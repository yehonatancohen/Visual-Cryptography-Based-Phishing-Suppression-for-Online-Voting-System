from database.db_tables import get_connection
from database.db_queries import __add_voter__, __get_voter__, \
    __get_all_voters__, __remove_voter__, __voter_vote__, __get_participating_surveys__
from database.models import Voter


def add_voter(email: str, survey_id: str) -> None:
    """Adds email given to the allowed voters at survey given\n
    Args:\n
        email (str)\n
        survey_id (str)\n
    """
    conn = get_connection()
    __add_voter__(conn, email, survey_id)


def add_voters(emails: list[str], survey_id: str) -> None:
    """Adds ALL emails given to the allowed voters at survey given\n
    Args:\n
        emails (list[str])\n
        survey_id (str)\n
    """
    for email in emails:
        add_voter(email, survey_id)

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


def voter_vote(email: str, survey_id: str, candidate_id: int) -> bool:
    """returns true if voter with email given has not voted yet 
    and voting was successfull
    Args:
        email (str)
        survey_id (str)
        candidate_id (int)
    Returns:
        bool: True if successfull
    """
    conn = get_connection()
    return __voter_vote__(conn, email, survey_id, candidate_id)

def get_participating_surveys(email: str) -> list[Voter]:
    """Returns all surveys where email given is allowed to vote.

    Args:
        email (str)

    Returns:
        list[Survey]
    """
    conn = get_connection()
    return __get_participating_surveys__(conn, email)

def get_all_surveys_per_voter(voter_email: str) -> list[dict]:
    """
    Args:
        voter_email (str)

    Returns:
        A list where each entry (one entry for each survey a user participates in) contains
            a dictionary with "survey_id", "survey_name", "start_date", "end_date", "has_user_voted"
            
    """
    voter_objects = get_participating_surveys(voter_email)
    result = []
    from .surveys import get_survey
    for voter in voter_objects:
        voted = False
        if voter.has_voted == 1:
            voted = True
        survey = get_survey(voter.survey_id)
        dict = {"survey_id":survey.id,
                "survey_name":survey.name,
                "start_date":survey.start_date,
                "end_date": survey.end_date,
                "has_user_voted": voted}
        result.append(dict)
    return result
    
    