import json
import os
import pickle

import google_auth_oauthlib.flow
from google.oauth2 import service_account
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials

import Verify_Video
import Video
import getCreds

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]


def generate_new_creds():
    file = "/Users/ojasvsingh/PycharmProjects/pythonProject/client_secret_745615777065-kmkhddlcbvgbk14tsd9i0i0k2i15fg78.apps.googleusercontent.com.json"
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        file, SCOPES)
    credentials = flow.run_console()
    with open("creds.pickle", 'wb') as f:
        pickle.dump(credentials, f)
    return credentials


def get_stored_creds():
    with open("creds.pickle", 'rb') as f:
        return pickle.load(f)


def get_creds():
    if not os.path.exists("creds.pickle"):
        return generate_new_creds()
    creds = get_stored_creds()
    if creds.valid:
        return creds
    return generate_new_creds()


def run():
    # creds_json = getCreds.get_cred()
    # access_token = getCreds.get_access_token()
    # creds = Credentials(
    #     access_token,
    #     refresh_token=creds_json.get("refresh_token"),
    #     token_uri=creds_json.get("token_uri"),
    #     client_id=creds_json.get('client_id'),
    #     client_secret=creds_json.get('client_secret'),
    #     scopes=SCOPES
    # )

    credentials = get_creds()

    # credentials = service_account.Credentials.from_service_account_file(
    #     "/Users/ojasvsingh/PycharmProjects/pythonProject/client_secret_745615777065-kmkhddlcbvgbk14tsd9i0i0k2i15fg78.apps.googleusercontent.com.json", scopes=SCOPES)
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
    request = youtube.videos().list(
        part="contentDetails,status,topicDetails,localizations",
        myRating="like"
    )
    response = request.execute()
    print(response)
    return response

def create_video_from_ytube_response(resp: json) -> Video.Video:
    return None

if __name__ == '__main__':
    resp = run()
    video = create_video_from_ytube_response(resp)
    video.insert_video()
    # save video to db
    # compare total videos at last fetch and total videos now to get how many new videos added. Add pagination and insert all of them in db
    verified = Verify_Video.verify_list(resp.get('items'))
    print(verified)
