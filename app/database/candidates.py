from database.db_tables import get_connection
from database.db_queries import __add_candidate__, __get_candidate__, \
                            __get_all_candidates__, __remove_candidate__
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


def remove_candidate(survey_id: str, candidate_id: int) -> None:
    """removes candidate given from survey given
    Args:
        survey_id (str)
        candidate_id (int)
    Returns:
        None
    """
    conn = get_connection()
    __remove_candidate__(conn, survey_id, candidate_id)


def get_candidates_results_per_servey(survey_id: str, get_in_precentage=True) -> list[dict]:
    """
    Args:
        survey_id (str)
        optional Args:
            get_in_precentage (boolean): if true, cand_results will be a precentage of the total votes
                if false, will returns the amount of votes per candidate.
    Returns:
        list[dict]: each entry in the list is a dictionary representing a candidate with the values
                    "candidate_id", "candidate_results", "candidate_name"

                    note that "candidate_results" is a precentage!
    """
    from .surveys import get_results
    survey_results = get_results(survey_id)
    total_votes = sum(int(val) for val in survey_results.values())
    results = [] 
    for cand_id in survey_results.keys():
        candidate = get_candidate(survey_id, cand_id)
        if get_in_precentage:
            cand_results = (float(candidate.votes) / float(total_votes)) * 100
        else:
            cand_results = candidate.votes
        dict = {
            "candidate_id": cand_id,
            "candidate_results": cand_results,
            "candidate_name": candidate.cand_name
        }
        results.append(dict)
    return results
    