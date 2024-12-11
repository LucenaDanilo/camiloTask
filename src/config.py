import os

# Configurações de credenciais
CREDENTIALS_PATH = 'credentials.json'
SHEET_URL = "https://docs.google.com/spreadsheets/d/11N_M2EDoSP7N9ULJl8qgiWp2H22j9cXNSjR1AYt2cos/edit?usp=sharing"

def get_credentials_path():
    return os.path.join(os.path.dirname(__file__), '..', CREDENTIALS_PATH)