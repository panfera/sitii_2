from dataclasses import dataclass
from datetime import datetime

from account import account
from vulnerability import vulnerability

@dataclass
class card:
	name: str
	name_type: str
	events_count: int
	crit_rate: float
	accounts: list[account]
	vulnerabilities: list[vulnerability]
	start_date: datetime
	end_date: datetime

	def __repr__(self):
		return f"""\
Название: {self.name}
Тип: {self.name_type}
Количество событий, составляющих инцидент: {self.events_count}
Критичность: {self.crit_rate}
Названия учетных записей и хостов и типы связанных активов: {self.accounts}
Предполагаемые проэксплуатированные уязвимости: {self.vulnerabilities} 
Время: от {self.start_date} до {self.end_date}
"""