from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import emoji


x = emoji.emojize('Python is my love :red_heart::fire:')


n = datetime.datetime.now()


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(n)
    print(x)

