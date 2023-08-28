import database.db_tables as db_tables
import database.models as models
import database.db_queries as db_queries

EMAIL_SIZE_LIMIT = 150
F_NAME_SIZE_LIMIT = 100
S_NAME_SIZE_LIMIT = 100


def init_tables():
    db_tables.init_tables()

def add_user(email, f_name, s_name, share2, password):
    conn = db_tables.get_connection()
    db_queries.__add_user__(conn, email, f_name, s_name, share2, password,
                                  email_size_limit=EMAIL_SIZE_LIMIT, 
                                  f_name_size_limit=F_NAME_SIZE_LIMIT,
                                  s_name_size_limit=S_NAME_SIZE_LIMIT)
    