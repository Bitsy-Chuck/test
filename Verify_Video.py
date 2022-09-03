# check method overloading to use name verify
def verify_list(video_meta: list):
    return all(map(verify, video_meta))


def verify(video_meta: dict):
    is_licensed = check_if_licensed_content(video_meta.get('contentDetails').get('licensedContent'))
    duration_in_range = check_duration_in_range(video_meta.get('contentDetails').get('duration'))
    privacy_status_valid = check_valid_privacy_status(video_meta.get('status').get('privacyStatus'))
    made_for_kids = check_made_for_kids(video_meta.get('status').get('madeForKids'))
    valid_license = check_license(video_meta.get('status').get('license'))
    return not is_licensed and duration_in_range and privacy_status_valid and made_for_kids and valid_license


def check_if_licensed_content(val: bool) -> bool:
    return val


def check_duration_in_range(val: str) -> bool:
    return True


def check_valid_privacy_status(val: str) -> bool:
    return val.lower() == 'public'

def check_made_for_kids(val: bool) -> bool:
    return True

def check_license(val: str) -> bool:
    return True # "license": "youtube",

