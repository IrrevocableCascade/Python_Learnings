__author__ = 'Benjamin'

__author__ = 'Benjamin'

from urllib import request
import json


domain = 'http://ran-json.c.ergebnis-dienst.de'
race_result = '/match/ma1710560/'
driver_info = '/person/pe'
team_info = '/team/te'
race_url = domain + race_result

response = request.urlopen(race_url)
race_data = json.loads(response.read().decode('utf-8'))

race_data = race_data['match']['match_result']
drivers = []
count = 1
ids = []

for result in race_data:
	driver = {}
	for item in result:
		if item == "person_id":
			driver[item] = result[item]
			response = request.urlopen(domain + driver_info + str(result[item]))
			person_data = json.loads(response.read().decode('utf-8'))
			driver["person_name"] = person_data["firstname"] + ' ' + person_data["surname"]
			ids.append(result[item])

		if item == "team_id":
			driver[item] = result[item]
			response = request.urlopen(domain + team_info + str(result[item]))
			team_data = json.loads(response.read().decode('utf-8'))
			driver["team_name"] = team_data["name"]

	drivers.append(driver)

	count += 1

person_ids = list(set(ids))
drivers_clean = []

for entry in drivers:
	for item in entry:
		if item == 'person_id' and entry[item] in person_ids:
			drivers_clean.append(entry)
			person_ids.remove(entry[item])

with open('driver_mapping.json', 'wb') as fp:
	fp.write(json.dumps(drivers_clean, sort_keys=True, indent=1).encode('utf-8'))


