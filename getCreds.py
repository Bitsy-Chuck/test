import sqlite3
import json
import os.path


config_path = os.path.expanduser('~/.config/gcloud/')
def get_access_token():
    path = config_path
        # The name of the database to process
    filename = 'access_tokens.db'
    path += filename
    if os.path.exists(path) is False:
        print('Error: File does not exist')
        print('File:', path)
        exit(1)
    conn = sqlite3.connect(path)
    cursor = conn.execute('SELECT * FROM access_tokens order by token_expiry desc')
    rows = cursor.fetchall()
    if len(rows) == 0:
        print('Error: Empty database')
        exit(1)
    # Note: This section is not displaying the access_token (row[1]) because it is too long
    return rows[0][1]

def get_cred():
    path = config_path
    # The name of the database to process
    filename = 'credentials.db'
    path += filename
    if os.path.exists(path) is False:
        print('Error: File does not exist')
        print('File:', path)
        exit(1)
    conn = sqlite3.connect(path)
    cursor = conn.execute('SELECT * FROM credentials')
    rows = cursor.fetchall()
    if len(rows) == 0:
        print('Error: Empty database. Do gcloud auth application-default login')
        exit(1)
    return json.loads(rows[0][1])
