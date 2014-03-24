__author__ = 'Irrevocable Cascade'

from urllib import request
import json

domain = 'http://ran-json.c.ergebnis-dienst.de'
race_entry = '/match/ma2188374/'
driver_info = '/person/pe'
team_info = '/team/te'
race_url = domain + race_entry

response = request.urlopen(race_url)
race_data = json.loads(response.read().decode('utf-8'))

race_data = race_data['match']['match_result']
drivers = []
ids = []

# Filter race_date so we only get person_id and team_id, then add the name and team strings based on the ids.
for entry in race_data:
    driver = {}
    for item in entry:
        if item == "person_id":
            driver[item] = entry[item]
            response = request.urlopen(domain + driver_info + str(entry[item]))
            person_data = json.loads(response.read().decode('utf-8'))
            driver["person_name"] = person_data["firstname"] + ' ' + person_data["surname"]
            driver["country"] = person_data["country"]
            ids.append(entry[item])

        if item == "team_id":
            driver[item] = entry[item]
            response = request.urlopen(domain + team_info + str(entry[item]))
            team_data = json.loads(response.read().decode('utf-8'))
            driver["team_name"] = team_data["name"]

    drivers.append(driver)

# Get a list of unique person_ids
person_ids = list(set(ids))
drivers_clean = []

# Remove the duplicates
for entry in drivers:
    for item in entry:
        if item == 'person_id' and entry[item] in person_ids:
            drivers_clean.append(entry)
            person_ids.remove(entry[item])

with open('driver_mapping.json', 'wb') as fp:
    fp.write(json.dumps(drivers_clean, sort_keys=True, indent=1).encode('utf-8'))


