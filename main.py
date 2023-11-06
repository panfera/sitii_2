from get_incident_card import get_incident_card


import sys

if __name__ == "__main__":
	incident_card = get_incident_card(sys.argv[1]) #205063 231830
	print(incident_card)