from database.db_tables import get_connection
from database.db_queries import __add_candidate__
from PIL.Image import Image

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
