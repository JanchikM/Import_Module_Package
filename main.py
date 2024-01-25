from datetime import datetime

from application.people import get_employees
from application.salary import calculate_salary


def print_date():
    print('Текущая дата и время: ', datetime.now())


if __name__ == '__main__':
    print_date()
    calculate_salary()
    get_employees()
