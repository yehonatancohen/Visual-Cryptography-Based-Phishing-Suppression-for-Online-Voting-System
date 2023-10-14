import sqlite3

DB_PATH = "./app/database/database.db"
USERS_TABLE_NAME = 'users'
SURVEYS_TABLE_NAME = 'surveys'
VOTERS_TABLE_NAME = 'voters'
CANDIDATE_TABLE_NAME = 'candidates'

users_table_init_query = f"""
    CREATE TABLE {USERS_TABLE_NAME}(
        email TEXT PRIMARY KEY,
        f_name TEXT,
        s_name TEXT,
        share_path TEXT,
        pass TEXT,
        server_code TEXT
    )
"""

survey_table_init_query = f"""
    CREATE TABLE {SURVEYS_TABLE_NAME}(
        id TEXT PRIMARY KEY,
        name TEXT,
        start date,
        end date,
        owner TEXT,
        FOREIGN KEY (owner) REFERENCES {USERS_TABLE_NAME} (email)
    )
"""

user_survey_table_init_query = f"""
    CREATE TABLE {VOTERS_TABLE_NAME}(
        survey_id TEXT,
        user TEXT,
        voted boolean,
        FOREIGN KEY (survey_id) REFERENCES {SURVEYS_TABLE_NAME} (id),
         PRIMARY KEY (survey_id, user)
    )
"""

candidate_table_init_query = f"""
    CREATE TABLE {CANDIDATE_TABLE_NAME}(
        candidate_id INTEGER,
        survey_id TEXT,
        cand_name TEXT,
        cand_desc TEXT,
        image_path TEXT,
        votes INTEGER,
        FOREIGN KEY (survey_id) REFERENCES {SURVEYS_TABLE_NAME} (id),
        PRIMARY KEY (candidate_id, survey_id)
    )

"""

def init_tables():
    """Create tables
    """
    conn = sqlite3.connect(DB_PATH)
    curr = conn.cursor()
    curr.execute(users_table_init_query)
    curr.execute(survey_table_init_query)
    curr.execute(user_survey_table_init_query)
    curr.execute(candidate_table_init_query)
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_PATH)