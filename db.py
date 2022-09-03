import sys

import psycopg2

import Constants
import Video

_conn_map = None
_cur = None


def get_new_connection():
    return psycopg2.connect(
        host="localhost",
        database="ytube",
        user="postgres",
        password="")


def get_connection():
    global _conn_map
    if _conn_map is None:
        _conn_map = get_new_connection()
    return _conn_map


def get_cursor():
    global _cur
    if _cur is None:
        conn = get_connection()
        _cur = conn.cursor()
    return _cur


def print_psycopg2_exception(err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    # get the line number when exception occured
    line_num = traceback.tb_lineno
    # print the connect() error
    print("\npsycopg2 ERROR:", err, "on line number:", line_num)
    print("psycopg2 traceback:", traceback, "-- type:", err_type)

    # psycopg2 extensions.Diagnostics object attribute
    print("\nextensions.Diagnostics:", err.diag)

    # print the pgcode and pgerror exceptions
    print("pgerror:", err.pgerror)
    print("pgcode:", err.pgcode, "\n")


def get_unmerged_videos():



def get_records(category: str, subcategory: str) -> Video.Video:
    query = """
        select * from videos where
         is_processed = false and 
         duration <= %s and 
         category = %s and 
         subcategory = %s
         order by duration desc
        """
    cur = get_cursor()
    cur.execute(query, (Constants.DEFAULT_VIDEO_DURATION, category, subcategory))
    result = cur.fetch()
    return result
