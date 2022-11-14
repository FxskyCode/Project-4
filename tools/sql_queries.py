from config.sql_connection import engine
import pandas as pd

def get_everything ():
    query = """SELECT * FROM office;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_everything_from_character (name):
    query = f"""SELECT * 
    FROM office
    WHERE speaker = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def get_just_dialogue (name):
    query = f"""SELECT line 
    FROM office
    WHERE speaker = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def insert_one_row (season, episode, title, scene, speaker, line):
    query = f"""INSERT INTO reddit.office
        (season, episode, title, scene, speaker, line) 
            VALUES ('{season}','{episode}','{title}','{scene}','{speaker}','{line}');
    """
    engine.execute(query)
    return f"Correctly introduced!"

