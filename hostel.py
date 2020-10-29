import requests, csv, os
from bs4 import BeautifulSoup

csv_file = open('hostel_details.csv', 'w', newline='')
writer = csv.DictWriter(csv_file, fieldnames=['Hostel Name', 'Hostel Address',])
writer.writeheader()

def extractHostel(city):
	for p in range(1, 10):
		url = "https://www.gopgo.in/{0}/pgo-properties?city_id=689\
		&latitude=12.971599&longitude=77.594563&search_by=city_id&page=10\
		&total_properties=3625&city_id=689&latitude=12.971599&longitude=77.594563\
		&search_by=city_id&page={1}&total_properties=3625".format(city, p)

		r = requests.get(url).content
		soup = BeautifulSoup(r,'lxml')

		hostel_details = soup.find_all('div', {'class': 'proptery-hostels-details'})

		for hostel in hostel_details:
			hostel_name = hostel.find('h2', {'class': 'proptery-hostels-name-l-title'})
			hostel_address = hostel.find('div', {'class': 'proptery-hostels-p'})
			
			hostel_name = hostel_name.text if hostel_name else ''
			hostel_address = hostel_address.text if hostel_address else ''

			hostel_detail = {
					'Hostel Name': hostel_name,
					'Hostel Address': hostel_address,
			}

			writer.writerow(hostel_detail)

extractHostel('chennai')
extractHostel('bengaluru')