import sqlite3

users_table_init_query = """
    CREATE TABLE users(
        email TEXT PRIMARY KEY,
        f_name TEXT,
        s_name TEXT,
        share_path TEXT,
        pass TEXT
    )
"""

survey_table_init_query = """
    CREATE TABLE surveys(
        id TEXT PRIMARY KEY,
        name TEXT,
        start date,
        end date,
        owner TEXT,
        FOREIGN KEY (owner) REFERENCES users (email)
    )
"""

user_survey_table_init_query = """
    CREATE TABLE usersInSurvey(
        survey_id TEXT,
        user TEXT,
        voted boolean,
        FOREIGN KEY (survey_id) REFERENCES surveys (id),
         PRIMARY KEY (survey_id, user)
    )
"""

candidate_table_init_query = """
    CREATE TABLE candidateInSurvey(
        candidate_id TEXT,
        survey_id TEXT,
        cand_name TEXT,
        cand_desc TEXT,
        image_path TEXT,
        FOREIGN KEY (survey_id) REFERENCES surveys (id),
        PRIMARY KEY (candidate_id, survey_id)
    )

"""

def init_tables():
    conn = sqlite3.connect("./database/database.db")
    curr = conn.cursor()
    curr.execute(users_table_init_query)
    curr.execute(survey_table_init_query)
    curr.execute(user_survey_table_init_query)
    curr.execute(candidate_table_init_query)
