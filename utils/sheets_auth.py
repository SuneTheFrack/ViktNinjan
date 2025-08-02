from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import os

def get_sheets_service():
    creds = service_account.Credentials.from_service_account_info(
        json.loads(os.environ["SERVICE_ACCOUNT_JSON"]),
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return build("sheets", "v4", credentials=creds)
