# Composer User Management
Add/Update/Delete Airflow users into Cloud Composer from Google Sheets.


## Setup:
Step 1. Activate virtual env (Optional)
  ```bash
  source your_env/bin/activate  # On Linux/macOS
  your_env\Scripts\activate     # On Windows
  ```
Step 2. Clone GitHub repo

Step 3. Install Following pypi packages,
  * ```bash
    pip install google-api-python-client
    ```
  * ```bash
    pip install gspread
    ```
Step 4. Make a copy of this Template: https://docs.google.com/spreadsheets/d/1iXBx8pIit6h4WzyUEIFV-n4T48QZ5ole41OKEIsCGX0/template/preview

Step 5. Make sure Service Account is added as a user in Airflow UI https://cloud.google.com/composer/docs/composer-2/access-airflow-api#long-service-account-email

Step 6. Grant Service Account `Viewer` permission to the Google Sheet created in Step 4.

## Update usermanagement.py

Step 1. Update `SHEET_ID` with your Google sheet ID created in Step 4 of Setup.

Step 2. Update `JSON_KEY` with your valid JSON KEY from the Service Account

Step 3. Update `COMPOSER_WEBSERVER_URL` with Composer webserver URL


