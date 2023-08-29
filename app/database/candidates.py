from database.db_tables import get_connection
from database.db_queries import __add_candidate__, __get_candidate__, \
                            __get_all_candidates__
from PIL.Image import Image
from database.models import Candidate

CANDIDATE_DESC_SIZE_LIMIT = 400

def add_candidate(survey_id: str, name: str, desc: str, image: Image = None) -> None:
    """adds a candidate with parameters given to survey given\n
        Can accept a candidate without an image. 
    Args:
        survey_id (str)
        name (str)
        desc (str)
        image (str)
    """
    conn = get_connection()
    __add_candidate__(conn, survey_id, name, desc, image, CANDIDATE_DESC_SIZE_LIMIT)


def get_candidate(survey_id: str, candidate_id: int) -> Candidate:
    """returns models.Candidate object with candidate given from survey given
    Args:
        survey_id (str)
        candidate_id (int)
    Returns:
        Candidate
    """
    conn = get_connection()
    return __get_candidate__(conn, survey_id, candidate_id)


def get_all_candidates(survey_id: str) -> list[Candidate]:
    """returns a list of all candidates in survey given\n
    Args:
        survey_id (str)
    Returns:
        list[Candidate]:
    """
    conn = get_connection()
    return __get_all_candidates__(conn, survey_id)