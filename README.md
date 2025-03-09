# zotero-to-gsheets
Python script to upload Zotero notes to a google spreadsheet.

## Installation

1. Create a virtual environment by using `python3 -m venv <venv_name>` where `<venv_name>` is the name of your virtual environment.
1. Activate the virtual environment: `source <venv_name>/bin/activate`.
1. Install the needed packages with: `pip install -r requirements.txt`
1. Configure your environment. Create a file name `.env` that will contain :
    ```
    ZOTERO_API_KEY="your_zotero_api_key"
    ZOTERO_USER_ID="<your_zotero_user_id>"
    GOOGLE_API_PATH="<google_api_creds_filepath>"
    SPREAD_SHEET_LINK="<spreadsheet_link>"
    ```
    Follow the docs of [pyzotero](https://pyzotero.readthedocs.io/en/latest/#) and [gspread](https://docs.gspread.org/en/latest/index.html) to get the needed elements.
1. Play with the script to adapt to your needs !