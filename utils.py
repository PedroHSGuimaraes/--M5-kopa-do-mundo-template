from datetime import datetime
from rest_framework.views import Response, status
from exceptions import *


def data_processing(**data: dict):
    first_word_cup = datetime(1930, 1, 1)
    last_word_cup = datetime(2022, 1, 1)

    data_first_cup = datetime.strptime(data["first_cup"], "%Y-%m-%d")

    delta_year_cup = data_first_cup.year - first_word_cup.year
    delta_all_data_cup = (last_word_cup.year - data_first_cup.year) / 4

    if data["titles"] < 0:
        data_error = {"error": "titles cannot be negative"}
        return data_error

    if data_first_cup.year < first_word_cup.year or delta_year_cup % 4 != 0:
        data_error = {"error": "there was no world cup this year"}
        return data_error

    if data["titles"] > delta_all_data_cup:
        data_error = {"error": "impossible to have more titles than disputed cups"}
        return data_error
