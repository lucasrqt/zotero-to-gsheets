from pyzotero import zotero
import gspread
import dotenv
import os

def get_zotero_library(user_id: str, api_key: str, library_type: str = "user"):
    if user_id is None:
        raise ValueError("user_id cannot be None")
    if api_key is None:
        raise ValueError("api_key cannot be None")
    
    return zotero.Zotero(user_id, library_type, api_key)


def get_gsheet_client(key_path: str):
    if key_path is None:
        raise ValueError("key_path cannot be None")
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"File not found: {key_path}")

    return gspread.service_account(filename=key_path)


def get_gsheet_worksheet(client: gspread.Client, sheet_link: str):
    if client is None:
        raise ValueError("client cannot be None")
    if sheet_link is None:
        raise ValueError("sheet_link cannot be None")

    return client.open_by_url(sheet_link)


class EnvLoader():
    _dotenv_path = None
    _zotero_api_key = None
    _zotero_user_id = None
    _google_api_path = None
    _gsheet_link = None
    _env = None

    def __init__(self, dotenv_path: str):
        if dotenv_path is None:
            raise ValueError("dotenv_path cannot be None")
        elif not os.path.exists(dotenv_path):
            raise FileNotFoundError(f"File not found: {dotenv_path}")
        
        self._dotenv_path = dotenv_path

    def load_env(self):
        self._env = dotenv.dotenv_values(self._dotenv_path)

    def get_zotero_api_key(self):
        if self._env is None:
            raise ValueError("Environment variables not loaded")
        if "ZOTERO_API_KEY" not in self._env:
            raise KeyError("ZOTERO_API_KEY not found in environment variables")
        
        return self._env["ZOTERO_API_KEY"]
    
    def get_zotero_user_id(self):
        if self._env is None:
            raise ValueError("Environment variables not loaded")
        if "ZOTERO_USER_ID" not in self._env:
            raise KeyError("ZOTERO_USER_ID not found in environment variables")
        
        return self._env["ZOTERO_USER_ID"]
    
    def get_google_api_path(self):
        if self._env is None:
            raise ValueError("Environment variables not loaded")
        if "GOOGLE_API_PATH" not in self._env:
            raise KeyError("GOOGLE_API_PATH not found in environment variables")
        
        return self._env["GOOGLE_API_PATH"]
    
    def get_gsheet_link(self):
        if self._env is None:
            raise ValueError("Environment variables not loaded")
        if "SPREAD_SHEET_LINK" not in self._env:
            raise KeyError("SPREAD_SHEET_LINK not found in environment variables")
        
        return self._env["SPREAD_SHEET_LINK"]