import time
import backend
from send_email import send_email
import sqlite3


URL = "https://programmer100.pythonanywhere.com/tours/"

while True:
	scraped = backend.scrape(URL)
	extracted = backend.extract(scraped)
	
	print(extracted)
	if extracted != "No upcoming tours":
		row = backend.read(extracted)
		if not row:
			backend.store(extracted)
			send_email(message=f"""Subject: New Tour Found
{extracted}""",
			           receiver="testcasepython123@gmail.com")
	time.sleep(2)
