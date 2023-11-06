from dataclasses import dataclass
from datetime import datetime

@dataclass
class account:
	account_name: str
	hostname: str
	equipment_type: str
	def __repr__(self):
		return f"({self.account_name}, {self.hostname}, {self.equipment_type})"