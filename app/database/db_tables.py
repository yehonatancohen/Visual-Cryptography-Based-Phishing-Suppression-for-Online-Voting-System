import psycopg2 as pg;
import os
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
        start timestamp,
        _end timestamp,
        owner TEXT,
        FOREIGN KEY (owner) REFERENCES {USERS_TABLE_NAME} (email)
    )
"""

user_survey_table_init_query = f"""
    CREATE TABLE {VOTERS_TABLE_NAME}(
        survey_id varchar(255),
        _user varchar(255),
        voted boolean,
        FOREIGN KEY (survey_id) REFERENCES {SURVEYS_TABLE_NAME} (id),
         PRIMARY KEY (survey_id, _user)
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

def get_connection():
    return pg.connect(os.environ['DB_HOST'])

def init_tables():
    """Create tables
    """
    # Connect to the database
    conn = get_connection();

    curr = conn.cursor()
    curr.execute(users_table_init_query)
    curr.execute(survey_table_init_query)
    curr.execute(user_survey_table_init_query)
    curr.execute(candidate_table_init_query)
    conn.commit()
    conn.close()

"""conn=get_connection()
curr=conn.cursor()
curr.execute(candidate_table_init_query)
conn.commit()
conn.close()"""