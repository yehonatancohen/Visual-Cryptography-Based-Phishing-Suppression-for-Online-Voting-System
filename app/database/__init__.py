"""
    users and surveys database manager
    IMPORT AND USE THIS AND ONLY THIS
"""
from database.db_tables import init_tables
from database.surveys import add_survey, get_survey, get_user_surveys, delete_survey \
                            , SURVEY_NAME_LENGTH_LIMIT
from database.users import add_user, get_user, does_user_exist, \
                    validate_user, get_share, \
                    EMAIL_SIZE_LIMIT, S_NAME_SIZE_LIMIT, F_NAME_SIZE_LIMIT, SEC_QUESTION_SIZE_LIMIT
from database.voters import add_voter, get_voter, get_all_voters, remove_voter