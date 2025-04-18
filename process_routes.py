import requests
import json
key = 'ed3b168b-3bc9-4a90-b03b-13df2aece788'
data = requests.post(f'https://routing.api.2gis.com/public_transport/2.0?key={key}',
                  headers= {'Content-Type': 'application/json'},
                  json = {
	"locale": "ru",
	"source":
	{
		"name": "Точка А",
		"point":
		{
			"lat": 43.403809,
			"lon": 39.983555
		}
	},
	"target":
	{
		"name": "Точка Б",
		"point":
		{
			"lat": 43.414713,
			"lon": 39.950758
		}
	},
	"transport": ["bus", "tram", "trolleybus"]
}).json()


routes = []
for route in data:
	if route['pedestrian']:
		route['workload'] = 0
		continue
	movements = []
	for mov in route['movements']:
		if mov['type'] == 'walkway':
			mov['workload'] = 0
			continue
		stations = mov['platforms']
		if not stations:
			mov['workload'] = 0
			continue
		stations = stations['names']
		station_workloads = []
		for q in stations:
			q = q.replace(' (по требованию)', '')
			workload = requests.post('http://127.0.0.1:8000/count_people', json={'station_name': q}).json()
			workload = workload['number_of_people']
			station_workloads.append(workload)
		mov['workload'] = sum(station_workloads)/len(station_workloads) # Берётся среднее по загруженности промежуточных станций
		movements.append(mov)
	route['movements'] = movements
	route['workload'] = sum([i['workload'] for i in movements])/len(movements)
	routes.append(route)


with open('workloads.json', 'w', encoding='utf-8') as f:
	json.dump(routes, f, indent=4, ensure_ascii=False)



