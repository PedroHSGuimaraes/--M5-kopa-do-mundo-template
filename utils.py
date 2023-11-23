from datetime import datetime, timedelta
from exceptions import *


def data_processing(data: dict) -> str:
    if data["titles"] < 0:
        raise NegativeTitlesError

    first_cup_year = int(data["first_cup"][:4])
    if first_cup_year < 1930 or (first_cup_year - 1930) % 4 != 0:
        raise InvalidYearCupError

    current_year = datetime.now().year
    max_possible_titles = (current_year - first_cup_year) // 4 + 1

    if data["titles"] > max_possible_titles:
        raise ImpossibleTitlesError

    return f"{data['name']} - Data Processed Successfully!"
