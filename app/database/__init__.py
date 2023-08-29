"""
    users and surveys database manager
    IMPORT AND USE THIS AND ONLY THIS
"""
from database.db_tables import init_tables
from database.surveys import add_survey, get_survey, get_user_surveys
from database.users import add_user, get_user, does_user_exist, \
                    validate_user, get_share
