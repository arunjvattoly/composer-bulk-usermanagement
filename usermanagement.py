import gspread
from google.oauth2.service_account import Credentials 
import google.auth
from google.auth.transport.requests import AuthorizedSession 
from typing import Any
import json
import os

# Step 1. Replace with your Google sheet ID
SHEET_ID = '123testdkYty3fsdfsdfsffdsfsdf24D9bONke0'
# Step 2. Replace with your valid JSON KEY from the Service Account
JSON_KEY="service-account-key.json"
# Step 3. Replace with Composer webserver URL
COMPOSER_WEBSERVER_URL='https://123456-test-url-dot-us-east1.composer.googleusercontent.com'

# Google Sheets setup
scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly','https://www.googleapis.com/auth/cloud-platform']
creds = Credentials.from_service_account_file(
    JSON_KEY, scopes=scopes)

# Open sheet by ID
client = gspread.authorize(creds)
sheet = client.open_by_key(SHEET_ID).sheet1  # Get the first sheet
print('Reading user details from sheet: {}'.format(sheet.title))

#Composer Setup
web_server_url = COMPOSER_WEBSERVER_URL
endpoint = f"api/v1/users"
base_url = f"{COMPOSER_WEBSERVER_URL}/{endpoint}"

def make_composer_web_server_request(
    url: str, method: str = "GET", data: dict = None, headers: dict = None, **kwargs: Any
) -> google.auth.transport.Response:
    """
    Make a request to Cloud Composer 2 environment's web server.
    Args:
      url: The URL to fetch.
      method: The request method to use ('GET', 'OPTIONS', 'HEAD', 'POST', 'PUT',
        'PATCH', 'DELETE')
      data: JSON payload
      headers: header information
      **kwargs: Any of the parameters defined for the request function:
                https://github.com/requests/requests/blob/master/requests/api.py
                  If no timeout is provided, it is set to 90 by default.
    """

    authed_session = AuthorizedSession(creds)

    # Set the default timeout, if missing
    if "timeout" not in kwargs:
        kwargs["timeout"] = 90

    return authed_session.request(method, url, data, headers, **kwargs)

# Function to process each user row


def process_user(row):
    first_name, last_name, email, role, action = row
    username = email  # Username is the same as email

    headers = {'Content-Type': 'application/json'}
    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'username': username,
        'roles': [{'name': role}]
    }

    json_data = json.dumps(user_data)
    if action == 'ADD':
        response = make_composer_web_server_request(
            base_url, method="POST", data=json_data, headers=headers)
    elif action == 'UPDATE':
        response = make_composer_web_server_request(
            f"{base_url}/{username}", method="PATCH", data=json_data, headers=headers)
    elif action == 'DELETE':
        response = make_composer_web_server_request(
            f"{base_url}/{username}", method="DELETE", headers=headers)
    else:
        print(f"Invalid action for user {username}: {action}")
        return

    # Response handling
    if response.status_code == 200:
        print(f"Successfully {action}ed user {username}")
    elif response.status_code == 204:  # Check for 204 specifically
        print(f"Successfully DELETEed user {username}")
    else:
        print(f"Error {action}ing user {username}: {response.text}")

# Read user data from the sheet (assuming header row)
all_records = sheet.get_all_records()

# Process each user
for user_data in all_records:
    process_user(list(user_data.values()))  # Convert OrderedDict to list
