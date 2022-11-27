# -*- coding: utf-8 -*-
def geo_log():

    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]


    result_list = []
    for visit in geo_logs:
        if 'Россия' in list(visit.values())[0]:
            result_list.append(visit)
    return result_list

if __name__ == '__main__':
    print(geo_log())

