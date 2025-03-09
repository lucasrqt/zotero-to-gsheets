#!/usr/bin/env python3

import argparse
import configs
import parser
import utils

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="A simple CLI tool for parsing and extracting notes from Zotero notes to be put on a Google spreadsheet.")
    parser.add_argument("--dotenv", type=str, default=configs.DOTENV, help="Path to the .env file containing the environment variables")
    return parser.parse_args()

def main():
    args = parse_args()
    env_loader = utils.EnvLoader(args.dotenv)
    env_loader.load_env()

    zotero_api_key = env_loader.get_zotero_api_key()
    zotero_user_id = env_loader.get_zotero_user_id()
    google_api_path = env_loader.get_google_api_path()
    gsheet_link = env_loader.get_gsheet_link()

    zotero_library = utils.get_zotero_library(zotero_user_id, zotero_api_key)
    gsheet_client = utils.get_gsheet_client(google_api_path)
    gsheet_worksheet = utils.get_gsheet_worksheet(gsheet_client, gsheet_link)

if __name__ == "__main__":
    main()