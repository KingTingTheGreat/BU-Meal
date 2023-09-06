import os
import sys
import time
import requests
import http.cookiejar as cookiejar
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

DATA_URL = os.getenv('DATA_URL')
LOGIN_URL = os.getenv('LOGIN_URL')

# URL = os.getenv('URL')
URL = 'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1693958515?ModuleName=current_balance_meal_and_pt.pl'

USERNAME, PASSWORD = os.getenv('USERNAME'), os.getenv('PASSWORD')

login_payload = {
    'j_username': USERNAME,
    'j_password': PASSWORD
}

headers = {
    'User-Agent': os.getenv('USER_AGENT')
}

# session = requests.Session()
# # session.get(URL)
# session.auth = (USERNAME, PASSWORD)
# response = session.post(URL, data=login_payload)

# response = session.get(URL)
    
cookiejar = cookiejar.CookieJar()

with requests.Session() as session:
    session.cookies = cookiejar
    session.auth = (USERNAME, PASSWORD)

    # response = session.get(URL)

    response = session.post(DATA_URL, 
                            auth = session.auth,
                            allow_redirects=True,
                            headers=headers,
                            cookies = session.cookies, 
                            data=login_payload)
    # cookies = dict(response.cookies)
    # response = session.get(URL, cookies=cookies)
    # response = session.get(URL)
    # response = session.get(URL, headers=headers, cookies=session.cookies)
    # other_response = session.get(DATA_URL,
    #                             auth=session.auth,
    #                             headers=headers, 
    #                             cookies=session.cookies)
    # for line in response.iter_lines():
    #     print(line)

    nxt_response = session.get(response.url, auth=session.auth, headers=headers, cookies=session.cookies)

    print(response.text)
    print(nxt_response.text)


with open('data.html', 'w') as f:
    f.write(response.text)

# print(response.text)




# # Fill in your details here to be posted to the login form.
# payload = {
#     'j_username': USERNAME,
#     'j_password': PASSWORD
# }

# # Use 'with' to ensure the session context is closed after use.
# with requests.Session() as s:
#     p = s.post(URL, data=payload)
#     # print the html returned or something more intelligent to see if it's a successful login page.
#     print(p.text)

#     # An authorised request.
#     r = s.get(URL)
#     print(r.text)
#         # etc...

# soup = BeautifulSoup(response.text, 'html.parser')
