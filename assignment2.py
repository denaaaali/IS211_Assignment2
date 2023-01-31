import argparse
import urllib.request
import logging
import datetime
import csv

def downloadData(url):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')
    return response
    

def processData(file_content):
    print(file_content)
    people = {}
    reader = csv.reader(file_content.splitlines(), delimiter=',')
    heading = next(reader, None)
    format = "%d/%m/%Y"
    logger = logging.getLogger("assignment2")
    for rownum, row in enumerate(reader):
        print(row)
        id = row[0]
        name = row[1]
        birthday = row[2]
        try:
            date = datetime.datetime.strptime(birthday, format)
            people[id] = (name, date)
        except ValueError:
            logger.error("Error processing line #'%d' for ID #'%s'", rownum, id)
    return people


def displayPerson(id, personData):
    id = str(id)
    if id in personData:
        name, birthday = personData[id]
        print("Person %s is %s with a birthday of %s"%(id, name, birthday))
    else:
        print("No user found with that id")

def main(url):
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    csvData = downloadData(args.url)

logger = logging.getLogger('assignment2')
logger.setLevel(logging.INFO)

handler = logging.FileHandler('errors.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger.addHandler(handler)

#idk what goes after csvData = so i put --url cause im scared
personData = processData(csvData)

while True:
    user_input = int(input("Please enter an ID to lookup: "))

    if user_input <= 0:
        break

    else:
        displayPerson(user_input, personData)