import requests
import xml.etree.ElementTree as ET

from postgreSQL_db_getter import postgreSQL_db_getter
from card import card
from account import account
from vulnerability import vulnerability

def get_incident_card(id) -> card:
	assets_id = []
	vulnerabilities_id = []
	incident_card, assets_id, vulnerabilities_id = postgreSQL_db_getter(id)

	#print(vulnerabilities_id)
	for i in assets_id:
		resp = requests.get('https://d5d9e0b83lurt901t9ue.apigw.yandexcloud.net/get-asset-by-id', params={'asset-id': f'{i}'})
		r = resp.json()["result"]
		incident_card.accounts.append(account(r['account_name'], r['hostname'], r['equipment_type']))

		name = "./xml/asset_" + i + "_vuln_report.xml"
		
		tree = ET.parse(name)
		root = tree.getroot()
		
		for element in root:
			if element.tag == 'vulnerabilities':
				for vulner in element:
					vuln = vulnerability()
					for i in vulner:
						if i.tag == 'title':
							vuln.title = i.text
						if i.tag == 'short_description':
							vuln.short_description = i.text
						if i.tag == 'description':
							vuln.description = i.text
						if i.tag == 'how_to_fix':
							vuln.how_to_fix = i.text
						if i.tag == 'links':
							vuln.links = i.text
						if i.tag == 'publication_date':
							vuln.publication_date = i.text
						if i.tag == 'cvss':
							vuln.cvss = i.text
						if i.tag == 'cvss3':
							vuln.cvss3 = i.text
						if i.tag == 'global_id':
							vuln.global_id = i.text
					#print(vuln)
					if vuln.global_id in vulnerabilities_id:
						incident_card.vulnerabilities.append(vuln)
						vulnerabilities_id.remove(vuln.global_id)
	return incident_card