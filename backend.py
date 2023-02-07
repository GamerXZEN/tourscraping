import requests
import selectorlib
import sqlite3

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 Safari/537.36'}
CONNECTION = sqlite3.connect("data.db")

def scrape(url):
	"""
Scrape the page source from the URL
"""
	response = requests.get(url, headers=HEADERS)
	source = response.text
	return source


def extract(source):
	"""
Extracts the source
	"""
	extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
	value = extractor.extract(source)["tours"]
	return value


def store(extracted_info):
	"""

	:param extracted_info:
	"""
	row = str(extracted_info).split(", ")
	cursor = CONNECTION.cursor()
	cursor.execute("INSERT INTO Events VALUES(?,?,?)", row)
	CONNECTION.commit()


def read(extracted):
	"""

	"""
	row = str(extracted).split(", ")
	band, city, date = row[0], row[1], row[2]
	cursor = CONNECTION.cursor()
	cursor.execute("SELECT * FROM Events WHERE band=? AND city=? AND "
	               "date=?", (band, city, date))
	rows = cursor.fetchall()
	return rows
