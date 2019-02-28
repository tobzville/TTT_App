import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

client = gspread.authorize(credentials)

sheet = client.open('HelloWorld').sheet1

data = sheet.get_all_records()
#sheet.update_acell('A1', 'First name')

print(data)
