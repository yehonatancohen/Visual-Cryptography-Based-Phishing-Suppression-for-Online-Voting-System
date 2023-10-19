"""
    users and surveys database manager
    IMPORT AND USE THIS AND ONLY THIS
"""
from database.db_tables import init_tables
from database.surveys import add_survey, get_survey, get_user_surveys, delete_survey \
                            , SURVEY_NAME_LENGTH_LIMIT, get_results, requirements_to_vote
from database.users import add_user, get_user, does_user_exist, \
                    validate_user, get_share, \
                    EMAIL_SIZE_LIMIT, S_NAME_SIZE_LIMIT, F_NAME_SIZE_LIMIT
from database.voters import add_voter, get_voter, get_all_voters, remove_voter, \
                            add_voters, voter_vote, get_participating_surveys, \
                            get_all_surveys_per_voter, get_surveys_related_to_user
from database.candidates import add_candidate, get_candidate, get_all_candidates, \
                                 remove_candidate, get_candidates_results_per_servey