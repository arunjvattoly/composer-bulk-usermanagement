# Composer User Management
Add/Update/Delete Airflow users into Cloud Composer from Google Sheets.


## Setup:
- Activate virtual env (Optional)
  ```bash
  source your_env/bin/activate  # On Linux/macOS
  your_env\Scripts\activate     # On Windows
  ```
- Clone GitHub repo
- Install Following pypi packages,
  * pip install google-api-python-client
  * pip install gspread

## Update usermanagement.py
Step 1. Make a copy of this Template: https://docs.google.com/spreadsheets/d/1iXBx8pIit6h4WzyUEIFV-n4T48QZ5ole41OKEIsCGX0/template/preview

Step 2. Make sure Service Account is added as a user in Airflow UI https://cloud.google.com/composer/docs/composer-2/access-airflow-api#long-service-account-email

Step 3. Grant Service Account `Viewer` permission to the Google Sheet created in Step 1

Step 4. Update `SHEET_ID` with your Google sheet ID created in Step 1.
  
Step 5. Update `JSON_KEY` with your valid JSON KEY from the Service Account
  
Step 6. Update `COMPOSER_WEBSERVER_URL` with Composer webserver URL


