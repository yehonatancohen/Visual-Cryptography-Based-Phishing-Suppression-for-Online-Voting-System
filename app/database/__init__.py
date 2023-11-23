"""
    users and surveys database manager
    IMPORT AND USE THIS AND ONLY THIS

"""
# CONSTANTS
from database.surveys import SURVEY_NAME_LENGTH_LIMIT
from database.users import EMAIL_SIZE_LIMIT
from database.users import S_NAME_SIZE_LIMIT
from database.users import F_NAME_SIZE_LIMIT


# initial database table
from database.db_tables import init_tables

# surveys CRUD (create, read, update, delete) operations
from database.surveys import add_survey
from database.surveys import get_survey
from database.surveys import get_user_surveys # user owned surveys
from database.surveys import delete_survey
from database.surveys import get_results
from database.surveys import requirements_to_vote

from database.surveys import update_start_date
from database.surveys import update_end_date

# user CRUD operations
from database.users import add_user
from database.users import get_user
from database.users import does_user_exist
from database.users import get_surveys_related_to_user

# user validation
from database.users import validate_user
from database.users import validate_user_share
from database.users import get_share

# voter CRUD operations
from database.voters import add_voter
from database.voters import add_voters
from database.voters import get_voter
from database.voters import get_all_voters
from database.voters import remove_voter

# voter & survey operations
from database.voters import voter_vote
from database.voters import get_participating_surveys
from database.voters import get_all_surveys_per_voter

# candidate CRUD operations
from database.candidates import add_candidate
from database.candidates import get_candidate
from database.candidates import get_all_candidates
from database.candidates import remove_candidate
from database.candidates import get_candidates_results_per_servey