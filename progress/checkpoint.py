import requests
import os
import re

BASE_URL = 'http://161.97.171.137:8802'
UID_FILE = 'user.txt'

def _get_user_id ():
    UID_PATH = os.path.join ('..', UID_FILE)
    if not os.path.exists (UID_PATH):
        try:
            UID_PATH = UID_FILE
            assert os.path.exists (UID_PATH)
        except AssertionError:
            print (f"⚠️ Error: '{UID_FILE}' not found! Make sure you haven't deleted it.")
            return None
    user_id = None
    with open (UID_PATH, encoding = 'utf8') as fin:
        for line in fin:
            match = re.search (r'^\s*USER\s*=\s*(.*)', line)
            if match:
                user_id = match.group (1)
                break
    if user_id is None:
        print (f'⚠️ Error: Please open {UID_FILE} and set your user name there (e.g. USER=John Smith)')
        return None
    return user_id


def checkpoint (session_id, checkpoint_id, user_id = None):
    if user_id is None:
        user_id = _get_user_id ()
    if user_id is None:
        print ('checkpoint function failed')
        return
    payload = {'user_id': user_id, 'session_id': session_id, 'checkpoint_id': checkpoint_id}
    try:
        response = requests.post (f'{BASE_URL}/api/checkpoint', json = payload, timeout = 5)
        if response.status_code == 200:
            print (f"✅ Checkpoint {checkpoint_id} for session '{session_id}' registered successfully!")
        else:
            print (f"❌ Server returned error status: {response.status_code} ({response.text})")
    except requests.exceptions.RequestException:
        # We catch exceptions softly so that a server crash does not interrupt the student's notebook execution
        print ('⚠️ Warning: Could not connect to the progress server. Check your internet connection.')