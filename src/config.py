import os

# Configurações de credenciais
CREDENTIALS_PATH = 'credentials.json'
SHEET_URL = "https://docs.google.com/spreadsheets/xxxxcamiloxxxxxxx"

def get_credentials_path():
    return os.path.join(os.path.dirname(__file__), '..', CREDENTIALS_PATH)