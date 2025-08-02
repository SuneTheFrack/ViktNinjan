import os
import json
from google.oauth2 import service_account
import gspread

def get_sheets_service():
    service_account_info = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])
    creds = service_account.Credentials.from_service_account_info(service_account_info)
    gc = gspread.authorize(creds)
    
    sheet_id = os.environ["SHEET_ID"]
    sh = gc.open_by_key(sheet_id)
    
    return sh, sheet_id  # OBS! returnera båda
