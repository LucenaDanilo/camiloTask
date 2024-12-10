import os

# Configurações de credenciais
CREDENTIALS_PATH = 'credentials.json'
SHEET_URL = "https://docs.google.com/spreadsheets/d/14Ra7VNhBaFVyBk3Y9w67AenAQJ58NvlY7tD8d9m_agM/edit?gid=0#gid=0"

def get_credentials_path():
    return os.path.join(os.path.dirname(__file__), '..', CREDENTIALS_PATH)